import whylogs as why
import pandas as pd
import os
from whylogs.viz import NotebookProfileVisualizer
from whylogs.viz.drift.column_drift_algorithms import calculate_drift_scores
from whylogs.core.constraints import (
    Constraints,
    ConstraintsBuilder,
    MetricsSelector,
    MetricConstraint
)

# Set environment variables for WhyLabs
os.environ["WHYLABS_DEFAULT_ORG_ID"] = "org-rE7D6t"
os.environ["WHYLABS_API_KEY"] = "1YQ18PUd8J.f6TZX0zvGOOxjcINzP3xWoquAPaXSM7KZ9CtaklkLAuKLlILxuzHF:org-rE7D6t"
os.environ["WHYLABS_DEFAULT_DATASET_ID"] = "model-7"

# Import data batches
urls = [
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_8_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_9_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_10_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_11_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_12_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_13_statefl_1.csv',
    'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_14_statefl_1.csv'
]

# Load the data batches into a list of DataFrames
batch_data = [pd.read_csv(url) for url in urls]

# Iris feature names
feature_names = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)',
    'state'
]

# Separate features and targets
X_batches = [batch[feature_names] for batch in batch_data]
y_batches = [batch['target'] for batch in batch_data]

# Create profiles of batches
profile_views = [why.log(X_batch).view() for X_batch in X_batches]

# Compare profiles
visualization = NotebookProfileVisualizer()
visualization.set_profiles(target_profile_view=profile_views[0], reference_profile_view=profile_views[5])
visualization.summary_drift_report()
visualization.double_histogram(feature_name="petal length (cm)")
visualization.double_histogram(feature_name="petal width (cm)")

def print_formatted_scores(scores, indent=0):
    """
    Recursively print the score dictionary in a formatted way, handling unknown structures.
    """
    for key, value in scores.items():
        print(' ' * indent + f"{key}:")
        
        if isinstance(value, dict):  # If the value is another dictionary, recurse into it
            print_formatted_scores(value, indent + 2)
        else:
            if isinstance(value, float):  # Format floats with precision
                print(' ' * (indent + 2) + f"{value:.6f}")
            else:
                print(' ' * (indent + 2) + str(value))

# Calculate drift scores
scores = calculate_drift_scores(target_view=profile_views[0], reference_view=profile_views[5], with_thresholds=True)
print_formatted_scores(scores, 0)  # Pass an integer for the indent parameter
print('\n')

# Data Quality Validation function
def validate_features(profile_view, verbose=False):
    builder = ConstraintsBuilder(profile_view)

    # Define constraints for validating data
    features_constraints = {
        "petal length (cm)": (0, 15),
        "petal width (cm)": (0, 15),
        "sepal length (cm)": (0, 15),
        "sepal width (cm)": (0, 15)
    }

    for feature, (min_val, max_val) in features_constraints.items():
        builder.add_constraint(MetricConstraint(
            name=f"{feature} > {min_val} and < {max_val}",
            condition=lambda x, min_val=min_val, max_val=max_val: x.min > min_val and x.max < max_val,
            metric_selector=MetricsSelector(
                metric_name='distribution',
                column_name=feature
            )
        ))

    # Build the constraints and return the report
    constraints = builder.build()

    if verbose:
        print('Constrains Report:', constraints.generate_constraints_report())

    return constraints

# Validate and visualize constraints for the profiles
for profile_view in [profile_views[1], profile_views[3]]:
    const = validate_features(profile_view, True)
    visualization = NotebookProfileVisualizer()
    visualization.constraints_report(const, cell_height=300)
    constraints_valid = const.validate()
    print('Constrains Valid:', constraints_valid, "\n")

# Convert profile view to pandas DataFrame for the last batch
print(profile_views[3].to_pandas())
