import mlflow
logged_model = 'runs:/72cda47143284c29bf4c89bae15fe03f/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

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

data = [ # From input_example.json
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

# loaded_model.predict(pd.DataFrame(data))
print(f"Prediction is : {loaded_model.predict(pd.DataFrame(data, columns=columns))}")
