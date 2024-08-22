import mlflow
import argparse
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

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

def main(random_state):
    df = load_data()
    TARGET = "quality"
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, test_size=0.2)

    # Define the parameter grid
    param_grid = {
        'alpha': [0.2, 0.000005, 0.1, 0.5, 1.0, 5.0, 10.0],
        'l1_ratio': [0.3, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
    }

    # Initialize the ElasticNet model
    model = ElasticNet(random_state=random_state)

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
        mlflow.log_param("alpha", best_params['alpha'])
        mlflow.log_param("l1_ratio", best_params['l1_ratio'])
        mlflow.log_param("random_state", random_state)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2-score", r2)

        input_example = X_test.iloc[[0]]
        mlflow.sklearn.log_model(best_model, "trained_model", input_example=input_example)

        print("MLFlow Run Completed")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--random_state", "-r", type=int, default=6)
    parsed_args = args.parse_args()
    print(f"Input Arguments: {parsed_args.random_state}")
    main(parsed_args.random_state)
