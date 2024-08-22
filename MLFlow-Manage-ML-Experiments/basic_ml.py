import mlflow
import argparse
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

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
    r2 = r2_score(actual, predict) # R² Score from 0 - 1, the closer to 1 the better the model.
    return rmse, mae, r2

def main(alpha, l1_ratio, random_state):
    df = load_data()
    TARGET = "quality"
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, test_size=0.2)
    # The dataset is then split into 80% training and 20% testing sets w a fixed random seed (random_state=6) for reproducibility.

    mlflow.set_experiment("ML-Model-1")
    with mlflow.start_run():
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_param("random_state", random_state)

        # Create an instance of the ElasticNet model
        model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
        # Training the model
        model.fit(X_train,y_train)
        # Testing the model        
        y_pred = model.predict(X_test)
        # Evaluation Testing Metrics via rmse, mae, r2-score
        rmse, mae, r2 = eval_function(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2-score", r2)

        # Use a single row from the DataFrame to avoid the feature name warning
        input_example = X_test.iloc[[0]]
        mlflow.sklearn.log_model(model, "trained_model", input_example=input_example)
        # mlflow.sklearn.log_model(model,"trained_model", input_example) 
        # The trained ElasticNet model is serialized and logged as an artifact in the MLflow run.
        print("MLFlow Run Completed")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha", "-a", type=float, default=0.2)
    args.add_argument("--l1_ratio", "-l1", type=float, default=0.3)
    args.add_argument("--random_state", "-r", type=int, default=6)
    parsed_args = args.parse_args()

    print(f"Input Arguments: {parsed_args.alpha}, {parsed_args.l1_ratio}, and {parsed_args.random_state}")
    # Hyperparameters to configure the ElasticNet model.
    # parsed_args.param1
    main(parsed_args.alpha, parsed_args.l1_ratio, parsed_args.random_state)
