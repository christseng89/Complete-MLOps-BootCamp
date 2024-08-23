import mlflow.pyfunc

model_path = "D:/development/Complete-MLOps-BootCamp/MLFlow-Manage-ML-Experiments/mlruns/906337619727975581/a9f8b05dd54c42dda1a81d9fc8d9abcd/artifacts/GradientBoostingClassifier"

# Serve the model using the mlflow.pyfunc.serve method
mlflow.pyfunc.serve(model_path=model_path, host='127.0.0.1', port=9000)
