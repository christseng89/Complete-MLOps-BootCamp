# Monitoring ML Application with Whylogs

### Introduction to ML Monitoring
// Agenda
- ML Monitoring Concepts
- Data Drift, Model Outputs, and Performance
- Bias Tracking and Explainability
- Open Source Tools for ML Monitoring with Whylogs

https://docs.whylabs.ai/docs/start-here/

// Why ML Monitoring?
- Model Inputs
    - Data Drift
    - Data Quality
        - External Changes
            - An input sensor/device for data collection causing bad data
            - Data was manually entered incorrectly
            - Lighting issues on the Camera
        - Schema Changes
            - Software library outputs a different data format
        - Pipeline Bugs
            - Data is being transformed incorrectly
            - Data is being dropped
            - Data is being duplicated
            - Anywhere in the pipeline where data is being transformed
    - Schema

- Model Outputs
    - Concept Drift
    - Volume
    - System metrics

- Model Performance
    - Accuracy/Recall/Precision
    - Bias/Fairness
    - Explainability
    - Business KPIs

// Data Quality Instances
- External Changes
    - An input sensor/device for data collection causing bad data
    - Data was manually entered incorrectly
    - Lighting issues on the Camera
- Schema Changes
    - Software library outputs a different data format
- Pipeline Bugs
    - Data is being transformed incorrectly
    - Data is being dropped
    - Data is being duplicated
    - Anywhere in the pipeline where data is being transformed

// Data Drift Instances
- Input data no longer matches the training data
- In ML, Input data -> Training data -> Model -> Output
- Business expansion/Market events
    - Seasonal changes
    - New product/features launches
    - New competitors
    - New regulations
    - New customer segments
    - Change in Customer preferences
    - Change in Customer behavior
    - Change in Market dynamics

// Concept Drift Instances
- No change in input data, but output is not in line with the current situations.
    - House prices
    - Covid-19
    - Stock prices
    - Weather
    - Traffic
    - Customer behavior
    - Customer preferences
    - Market dynamics

// Bias Detection Instances
- It's a phenomenon that skew the result of an algorithm in a particular direction.
  - Example: Credit approval rate is higher for Men than Women.
- Bias can be introduced at any stage of the ML pipeline.

// Model Explainability Instances
- Understanding the prediction of a model, will build confidence, and identify the issues.
    - Example: Why a model is predicting a particular output for a particular input.

// Places where change can occur in ML Application
- ML/Data Pipeline
- Model Inputs and Outputs
- Predictions
- Ground Truth
- KPIs
- Software/Product Changes

### Setting Up WhyLabs
https://whylabs.ai/whylabs-free-sign-up => Sign Up
https://hub.whylabsapp.com/resources?targetOrgId=org-rE7D6t => Project Dashboard

### Whylogs - Drift Detection, Input, Output, Bias Monitoring
https://docs.whylabs.ai/docs/whylogs-overview/

- WhyLogs is an open-source data logging library that helps you monitor data quality, detect data drift, and understand your datasets.
- WhyLogs generates "summaries of datasets" known as WhyLogs Profiles.
    - Track changes in their dataset
    - Create data constraints to know whether their data looks the way it should
    - Quickly visualize key summary statistics about their datasets
    - Send to the WhyLabs AI Control Center for observability, monitoring, alerting, and reinforcing guardrails
- WhyLogs is lightweight and efficient, making it suitable for use in production systems where it can handle large datasets and continuously monitor data without significant computational overhead.

// WhyLab AI Features
https://docs.whylabs.ai/docs/whylabs-api

- WhyLabs AI is a powerful platform for monitoring and managing the health and performance of machine learning (ML) models and data pipelines.
- By integrating with WhyLogs, WhyLabs AI provides a comprehensive solution to ensure that data and models behave as expected in production environments, helping organizations maintain high standards of quality and reliability in their ML or AI-driven processes.

// Install WhyLogs
https://cmake.org/download/#latest => 3.29.5
cmake --version
    cmake version 3.29.5

pip install whylogs
pip install shap
pip install ipywidgets

// WhyLab AI Integration
WhyLab => Settings => Integrations => Create API Token

    os.environ["WHYLABS_DEFAULT_ORG_ID"] = "org-rE7D6t" # ORG-ID is case sensitive
    os.environ["WHYLABS_API_KEY"] = "BlaW5f2H7D.teMNRKZJLGtWnyv1MAwfwIUDG3PSjxtirY1FJz2fHwPDYvlidsb0c:org-rE7D6t"
    os.environ["WHYLABS_DEFAULT_DATASET_ID"] = "model-2" # The selected project "ML-Learning (model-2)" is "model-2"

// WhyLogs example
cd ML-Monitoring-WhyLogs
jupyter lab

// Source code -> WhyLogs_ML_Monitoring_Data_Drift,_Bias,_Explainability.ipynb
// Folder => datasets
