from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Loading the trained model
model_name = 'RF_Loan_model.joblib'
model = joblib.load(model_name)

# Views
@app.route('/')
def home():
    # Render the form with empty input and no result
    return render_template('loan_prediction.html', form_data={}, prediction='')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the cancel button was clicked
    if request.form.get('cancel'):
        return redirect(url_for('home'))  # Reset all inputs and result

    # Collect form data
    request_data = dict(request.form)
    form_data = request_data.copy()  # Copy of form data to retain inputs

    # Remove optional fields from data processing (not form_data)
    request_data.pop('First_Name', None)
    request_data.pop('Last_Name', None)

    try:
        # Convert input data to integers, using default values if empty
        request_data = {k: int(v) if v.strip() != '' else 0 for k, v in request_data.items()}

        # Convert to DataFrame
        data = pd.DataFrame([request_data])

        # Add TotalIncome column calculation
        data['TotalIncome'] = data.get('applicant_income', 0) + data.get('co_applicant_income', 0)
        data['LoanAmount'] = data.get('LoanAmount', 0)

        data['TotalIncome'] = np.log(data['TotalIncome'] + 1).copy()
        data['LoanAmount'] = np.log(data['LoanAmount'] + 1).copy()

        # Define required columns with default values if missing
        required_columns = [
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

        # Add missing columns with default values
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0  # Default to 0 or another appropriate value

        # Select only the required columns
        data = data[required_columns]
        for col in data:
            data[col] = data[col].iloc[0]

        # Make the prediction
        prediction = model.predict(data)

        if int(prediction[0]) == 0:
            result = "Congratulations! Your loan request is 'Approved'."
        else:
            result = "Sorry! Your loan request is 'Rejected'."

    except (ValueError, KeyError) as e:
        result = f"Error: {str(e)}. Please ensure all fields are filled correctly."

    # Return the form with current input values and the result
    return render_template('loan_prediction.html', form_data=form_data, prediction=result)

@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
