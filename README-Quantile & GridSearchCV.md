# Quantile
Formula quantile by using the dataset below.
Original Dataset:
    Income
0    30000
1    50000
2    60000
3  1000000
4    45000
5    20000
6    70000
7   500000

5th Percentile for Income: 27500.0
95th Percentile for Income: 775000.0

=====================

The formula behind the `quantile` function is based on the idea of interpolation between sorted data points to find the value at a specific percentile. Here's how it works, using your dataset as an example:

### Original Dataset

    Income
0    30000
1    50000
2    60000
3  1000000
4    45000
5    20000
6    70000
7   500000

### Step-by-Step Calculation of Percentiles

#### Step 1: Sort the Data
First, you need to sort the `Income` data in ascending order:

    Income
0    20000
1    30000
2    45000
3    50000
4    60000
5    70000
6   500000
7  1000000

#### Step 2: Calculate the Ranks
Next, you calculate the rank for the desired quantile. For a quantile `q`, the rank `R` can be calculated as:

 R = (n - 1) * q 

Where:
-  n  is the number of data points (in this case,  n = 8 )
-  q  is the quantile (for the 5th percentile,  q = 0.05 ; for the 95th percentile,  q = 0.95 )

##### For the 5th Percentile (q = 0.05):
 R = (8 - 1) * 0.05 = 7 * 0.05 = 0.35 

##### For the 95th Percentile (q = 0.95):
 R = (8 - 1) * 0.95 = 7 * 0.95 = 6.65 

#### Step 3: Determine the Position in the Sorted Data

- 5th Percentile (R = 0.35):
  -  R = 0.35  falls between the 0th and 1st data points in the sorted list. The value at this rank is calculated by linear interpolation between these points.

- 95th Percentile (R = 6.65):
  -  R = 6.65  falls between the 6th and 7th data points. The value at this rank is also calculated by linear interpolation.

#### Step 4: Interpolate (if necessary)

- Interpolation Formula:
  - If  R  is not an integer, the quantile is interpolated between the 'TWO' nearest data points:
  
   {Quantile Value} = (1 - R) * {Value at floor(R)} + R * {Value at ceil(R)} 

- 5th Percentile:
  - For  R = 0.35 :
    - Floor of  R = 0  → Value = 20,000
    - Ceil of  R = 1  → Value = 30,000
    - Interpolation:
    
    {5th Percentile Value} = 
        (1 - 0.35) * 20000 + 0.35 * 30000 = 
        0.65 * 20000 + 0.35 * 30000 = 
        13000 + 10500 = 23500 + 4000 = 27500
    
- 95th Percentile:
  - For  R = 6.65 :
    - Floor of  R = 6  → Value = 500,000
    - Ceil of  R = 7  → Value = 1,000,000
    - Interpolation:
    
    {95th Percentile Value} = 
        (1 - 0.65) * 500000 + 0.65 * 1000000 = 
        0.35 * 500000 + 0.65 * 1000000 = 
        175000 + 650000 = 775000
    

### Summary

- The 5th percentile value of `Income` is `27,500`.
- The 95th percentile value of `Income` is `775,000`.

The percentile values are determined by linearly interpolating between the closest ranks in the sorted data. This method ensures that the quantile reflects the distribution of the data accurately.

# GridSearchCV
The code snippet you've provided involves the use of Scikit-learn's `GridSearchCV` for hyperparameter tuning of machine learning models like `RandomForestClassifier`, `LogisticRegression`, and `DecisionTreeClassifier`.

### Official Documentation for the Usage

1. **RandomForestClassifier**:
   - Official documentation for `RandomForestClassifier`: [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
   - Official documentation for the hyperparameters (`n_estimators`, `max_depth`, `criterion`, `max_leaf_nodes`): These parameters are described in the above link.

2. **LogisticRegression**:
   - Official documentation for `LogisticRegression`: [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
   - Official documentation for the hyperparameters (`C`, `penalty`, `solver`): These parameters are described in the above link.

3. **DecisionTreeClassifier**:
   - Official documentation for `DecisionTreeClassifier`: [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
   - Official documentation for the hyperparameters (`max_depth`, `criterion`): These parameters are described in the above link.

4. **GridSearchCV**:
   - Official documentation for `GridSearchCV`: [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
   - This class is used to exhaustively search over a specified parameter grid for an estimator (like the ones mentioned above). It is useful for tuning hyperparameters to find the best model.

### Explanation of the Code

- **RandomForestClassifier**: 
  - The `RandomForestClassifier` is an ensemble learning method for classification that operates by constructing multiple decision trees during training and outputting the mode of the classes (classification) of the individual trees.
  - The `param_grid_forest` dictionary specifies the hyperparameters that will be tuned using `GridSearchCV`.

- **LogisticRegression**:
  - The `LogisticRegression` model is used for binary or multinomial logistic regression. It is a linear model that uses the logistic function to model a binary dependent variable.
  - The `param_grid_log` dictionary specifies the hyperparameters that will be tuned using `GridSearchCV`.

- **DecisionTreeClassifier**:
  - The `DecisionTreeClassifier` is a non-parametric supervised learning method used for classification and regression. It creates a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.
  - The `param_grid_tree` dictionary specifies the hyperparameters that will be tuned using `GridSearchCV`.

- **GridSearchCV**:
  - `GridSearchCV` performs an exhaustive search over specified parameter values for an estimator. It combines cross-validation and a grid search of parameter combinations to find the best model.

The above links provide detailed information about each estimator, the parameters you can tune, and how `GridSearchCV` works. This should cover all aspects of the code snippet you provided.
