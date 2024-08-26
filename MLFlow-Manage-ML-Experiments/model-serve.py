import mlflow
model_name = 'Loan_prediction RF'

stage = "Production" # Staging
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")

# Predict on a Pandas DataFrame.
import pandas as pd

columns = [ # From input_example.json
  "Gender",
  "Married",
  "Dependents",
  "Education",
  "Self_Employed",
  "LoanAmount",
  "Loan_Amount_Term",
  "Credit_History",
  "Property_Area",
  "TotalIncome"
]

data = [ # From Artifacts
    [
    1.0,
    1.0,
    0.0,
    1.0,
    0.0,
    4.852030263919617,
    360.0,
    0.0,
    2.0,
    8.72355674269043
    ]    
]
print(f"Prediction is : {loaded_model.predict(pd.DataFrame(data, columns=columns))}")
