import os
import joblib
import streamlit as st
import numpy as np
import wget

model_name = 'RF_Loan_model.joblib'
file_url = f"https://raw.githubusercontent.com/christseng89/Complete-MLOps-BootCamp/main/Build-ML-App-Streamlit/{model_name}"

# Using HTML and CSS for custom font and color
st.markdown(
    """
    <style>
    .title {
        font-family: 'Arial', sans-serif;
        color: #2E8B57;  /* Change this color code as needed */
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .header {
        font-family: 'Verdana', sans-serif;
        color: #4682B4;  /* Change this color code as needed */
        font-size: 24px;
        font-weight: normal;
        margin-bottom: 20px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Check if the model file exists in the current directory
if not os.path.isfile(model_name):
    wget.download(file_url)

# Load the model
model = joblib.load(model_name)

def prediction(Gender,Married,Dependents,
         Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
         LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
        if Gender == "Male":
            Gender = 1
        else:
            Gender = 0

        if Married == "Yes":
            Married = 1
        else:
            Married = 0

        if Education == "Graduate":
            Education = 0
        else:
            Education = 1
        
        if Self_Employed == "Yes":
            Self_Employed = 1
        else:
            Self_Employed = 0

        if Credit_History == "Outstanding Loan":
            Credit_History = 1
        else:
            Credit_History = 0   
        
        if Property_Area == "Rural":
            Property_Area = 0
        elif Property_Area == "Semi Urban":
            Property_Area = 1  
        else:
            Property_Area = 2

        Total_Income = np_log(ApplicantIncome + CoapplicantIncome)
        LoanAmount = np_log(LoanAmount)
           
        prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Total_Income]])
        print(print(prediction))

        if prediction==0:
            pred = "Rejected"
        else:
            pred = "Approved"
        return pred        

def main():
    # Front end
    # st.title("Welcome to Loan Application")
    # st.header("Provide Your Information to Continue with Your Loan Application")
    # Displaying the styled title and header using the custom classes
    st.markdown('<p class="title">Welcome to Loan Application</p>', unsafe_allow_html=True)
    st.markdown('<p class="header">Provide Your Information to Continue with Your Loan Application</p>', unsafe_allow_html=True)    
    Gender = st.selectbox("Gender",("Male","Female"))
    Married = st.selectbox("Married",("Yes","No"))
    Dependents = st.number_input("Number of Dependents", min_value=0, max_value=3, value=0, step=1)
    Education = st.selectbox("Education",("Graduate","Not Graduate"))
    Self_Employed = st.selectbox("Self Employed",("Yes","No"))
    ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=0, step=1)
    CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, value=0, step=1)
    LoanAmount = st.number_input("Loan Amount", min_value=0, value=0, step=1)
    Loan_Amount_Term = st.number_input("Loan Term", min_value=30, value=360, step=1)
    Credit_History = st.selectbox("Credit History",("Outstanding Loan", "No Outstanding Loan"))
    Property_Area = st.selectbox("Property Area",("Rural","Urban","Semi Urban"))

    if st.button("Predict"):
        result = prediction(Gender,Married,Dependents,
         Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
         LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        
        if result == "Approved":
            st.success("Your loan Application is 'Approved'")
        else:
            st.error("Your loan Application is 'Rejected'")

def np_log(x):
    if x == 0:
        return 0
    
    return np.log(x)

if __name__ == "__main__":
    main()
