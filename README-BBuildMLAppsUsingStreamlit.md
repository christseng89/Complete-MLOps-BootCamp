# Build ML Apps w Streamlit
Folder => Build-ML-App-Streamlit

### Introduction to Streamlit
Streamlit is an open-source Python library that enables developers, especially data scientists and machine learning engineers, to quickly create and share data-driven 'Web applications' with minimal code. 

It is designed to simplify the process of turning Python scripts into interactive apps, allowing users to visualize data, run models, and create dashboards WITHOUT needing extensive web development experience.

Key Features of Streamlit
- Ease of Use
- Interactive Widgets
- Real-Time Updates
- Integration with Popular Python Libraries
- No Web Development Skills Required
- Rapid Prototyping and Deployment
- Markdown and Media Support

https://streamlit.io/
https://docs.streamlit.io/

### Hands On Working with Streamlit
cd Build-ML-App-Streamlit

python -m venv mlenv
mlenv\Scripts\activate

pip install -r requirements.txt

// Streamlit demo
streamlit run streamlit-demo.py
    ...
    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://10.39.101.8:8501

http://localhost:8501

// Streamlit app
streamlit run app.py 
http://localhost:8501

// Generate ML model (RF_Loan_model.joblib)
python loan_prediction_train.py
    Prediction is : [1]

### Building the ML Model with Streamlit
streamlit run streamlit-ml-app.py
