import mlflow
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import ElasticNet, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.exceptions import ConvergenceWarning
import warnings

warnings.filterwarnings("ignore", category=ConvergenceWarning)

def load_data():
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    try:
        df = pd.read_csv(URL, sep=";")
        return df
    except Exception as e:
        raise e

def eval_function(actual, predict):
    rmse = root_mean_squared_error(actual, predict)
    mae = mean_absolute_error(actual, predict)
    r2 = r2_score(actual, predict)
    return rmse, mae, r2

def main(random_state, model_type="elasticnet"):
    df = load_data()
    TARGET = "quality"
    X = df.drop(columns=TARGET)
    y = df[TARGET]

    # Scaling features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Adding polynomial features
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X_scaled)

    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, random_state=random_state, test_size=0.2)

    if model_type == "elasticnet":
        # Define the parameter grid for ElasticNet
        param_grid = {
            'alpha': [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 0.1, 0.5, 1.0, 5.0, 10.0],
            'l1_ratio': [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0],
            'max_iter': [1000, 5000, 10000]  # Increase the number of iterations
        }
        model = ElasticNet(random_state=random_state)
    elif model_type == "randomforest":
        # Define the parameter grid for RandomForestRegressor
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        model = RandomForestRegressor(random_state=random_state)
    elif model_type == "ridge":
        # Define the parameter grid for Ridge Regression
        param_grid = {
            'alpha': [1e-3, 1e-2, 0.1, 0.5, 1.0, 5.0, 10.0],
            'max_iter': [1000, 5000, 10000]  # Increase the number of iterations
        }
        model = Ridge(random_state=random_state)
    else:
        raise ValueError("Invalid model_type. Choose 'elasticnet', 'ridge', or 'randomforest'.")

    # Perform grid search with cross-validation
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2', verbose=1)
    grid_search.fit(X_train, y_train)

    # Get the best parameters and the corresponding model
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_

    print(f"Best Parameters: {best_params}")

    # Evaluate on the test set
    y_pred = best_model.predict(X_test)
    rmse, mae, r2 = eval_function(y_test, y_pred)

    print(f"RMSE: {rmse}, MAE: {mae}, R2-Score: {r2}")

    # Log parameters and metrics with MLflow
    mlflow.set_experiment("ML-Model-1")
    with mlflow.start_run():
        mlflow.log_params(best_params)
        mlflow.log_param("random_state", random_state)
        mlflow.log_param("model_type", model_type)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2-score", r2)

        input_example = X_test[0].reshape(1, -1)
        mlflow.sklearn.log_model(best_model, "trained_model", input_example=input_example)

        print("MLFlow Run Completed")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--random_state", "-r", type=int, default=6)
    args.add_argument("--model_type", "-m", type=str, default="elasticnet", choices=["elasticnet", "ridge", "randomforest"])
    parsed_args = args.parse_args()
    print(f"Input Arguments: {parsed_args.random_state}, Model Type: {parsed_args.model_type}")
    main(parsed_args.random_state, parsed_args.model_type)
