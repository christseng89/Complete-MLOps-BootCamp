import whylogs as why
import pandas as pd
import datetime
import os
from whylogs.api.writer.whylabs import WhyLabsWriter
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn import neighbors
from whylogs.core.schema import DatasetSchema
from whylogs.core.segmentation_partition import segment_on_column
from whylogs import log_classification_metrics
import warnings

# Suppress specific FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning, module="whylogs")

MODEL_6 = "model-6"
MODEL_7 = "model-7"

# Set WhyLabs environment variables
def set_whylabs_env(dataset_id):
    os.environ["WHYLABS_DEFAULT_ORG_ID"] = "org-rE7D6t"
    os.environ["WHYLABS_API_KEY"] = "1YQ18PUd8J.f6TZX0zvGOOxjcINzP3xWoquAPaXSM7KZ9CtaklkLAuKLlILxuzHF:org-rE7D6t"
    os.environ["WHYLABS_DEFAULT_DATASET_ID"] = dataset_id

# Load Iris dataset and train the KNN model
def train_knn_model():
    df_iris = load_iris(as_frame=True)
    X, y = df_iris.data, df_iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    knn = neighbors.KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    print(f"Model accuracy: {accuracy}")
    return knn, df_iris

# Load datasets from URLs
def load_datasets(urls, feature_names):
    datasets, targets = [], []
    for url in urls:
        data = pd.read_csv(url)
        X = data[feature_names]
        y = data['target']
        datasets.append(X)
        targets.append(y)
    return datasets, targets

# Get predictions and append to DataFrame
def predict_and_append(dfs, knn, class_names):
    for df in dfs:
        y_pred = knn.predict(df.iloc[:, :4])
        y_prob = knn.predict_proba(df.iloc[:, :4])
        df['cls_output'] = [class_names[pred] for pred in y_pred]
        df['prob_output'] = [max(prob) for prob in y_prob]

# Log data profiles and classification metrics to WhyLabs
def log_profiles_and_metrics(dfs, targets, model_id, segment_column=None):
    set_whylabs_env(model_id)
    writer = WhyLabsWriter()
    for i, (df, target) in enumerate(zip(dfs, targets)):
        df['ground_truth'] = target
        dt = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(days=i)
        
        profile = why.log(df).profile()
        
        profile.set_dataset_timestamp(dt)
        writer.write(file=profile.view())

        if segment_column:
            segmented_results = log_classification_metrics(
                df,
                target_column="ground_truth",
                prediction_column="cls_output",
                schema=DatasetSchema(segments=segment_on_column(segment_column))
            )
            segmented_results.set_dataset_timestamp(dt)
            segmented_results.writer("whylabs").write()

    print("Model ID", model_id, "logged successfully")

# Main execution flow
def main():
    # Step 1: Train KNN model
    knn, df_iris = train_knn_model()
    
    # Step 2: Load datasets
    urls_no_state = [
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_1_no_drift.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_2_no_drift.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_3_no_drift.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_4_drift_0s.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_5_drift.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_6_drift.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_7_no_drift.csv'
    ]

    urls_with_state = [
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_8_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_9_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_10_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_11_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_12_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_13_statefl_1.csv',
        'https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/ML-Monitoring-WhyLogs/datasets/iris_14_statefl_1.csv'
    ]

    feature_names_no_state = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    feature_names_with_state = feature_names_no_state + ['state']

    datasets_no_state, targets_no_state = load_datasets(urls_no_state, feature_names_no_state)
    datasets_with_state, targets_with_state = load_datasets(urls_with_state, feature_names_with_state)

    # Step 3: Get predictions and append to DataFrames
    class_names = ['setosa', 'versicolor', 'virginica']
    predict_and_append(datasets_no_state, knn, class_names)
    predict_and_append(datasets_with_state, knn, class_names)

    # Step 4: Log datasets without state to model-6
    log_profiles_and_metrics(datasets_no_state, targets_no_state, MODEL_6)

    # Step 5: Log datasets with state to model-7
    log_profiles_and_metrics(datasets_with_state, targets_with_state, MODEL_7, segment_column="state")

    # Step 6: Create and log reference profile
    ref_profile = why.log(df_iris.data).profile()
    writer = WhyLabsWriter().option(reference_profile_name="iris_training_profile")
    writer.write(file=ref_profile.view())

if __name__ == "__main__":
    main()
