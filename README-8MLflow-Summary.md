# MLflow Summary

## MLflow Install
cd MLFlow-Manage-ML-Experiments
mlflow-venv\Scripts\activate
pip install setuptools
pip install mlflow --user --no-warn-script-location
mlflow --version

### MLflow tracking server UI
https://mlflow.org/docs/latest/tracking.html

mlflow ui
python basic-ml.py 

http://127.0.0.1:5000/ => ML-Model-1 => Run Name (...)

python loan_prediction.py
http://127.0.0.1:5000/ => Loan_prediction => Run Name (5 names) => Compare

### MLflow projects
https://mlflow.org/docs/latest/projects.html

mlflow run --experiment-name Loan_prediction .
mlflow run https://github.com... --experiment-name Loan_prediction

### MLflow models (REST API)
https://mlflow.org/docs/latest/models.html#example-using-the-custom-sktime-flavor

mlflow.sklearn.log_model(model, name, input_example=input_example)

// mlflow models serve -m runs:/<RUN_ID>/<model> --no-conda --port 9000 => "runs:/<RUN_ID>/<model>" from the Artifacts
mlflow models serve -m runs:/a9f8b05dd54c42dda1a81d9fc8d9abcd/GradientBoostingClassifier --no-conda --port 9000

// Postman => MLflow => Test Model Gradient Boosting Classifier

### MLflow registry (MySQL)
https://mlflow.org/docs/latest/model-registry.html
pip install mysqlclient

// Create Schema db_mlflow

rd mlruns /s
mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri mysql://root:t1216$Chris@localhost/db_mlflow --default-artifact-root mlruns
    ...
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO:waitress:Serving on http://127.0.0.1:5000

python loan_prediction.py

set MLFLOW_TRACKING_URI=http://127.0.0.1:5000
mlflow run --experiment-name Loan_prediction .
