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
