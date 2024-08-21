# MLflow

An open-source platform to manage the complete ML Lifecycle.

When using MLflow, key considerations include 
- Experiment tracking, 
- Model management, 
- Reproducibility, 
- Collaboration, 
- Scalability, 
- Compliance, 
- CI/CD integration, 
- Monitoring, 
- Extensibility, and 
- Proper documentation. 

By focusing on these areas, you can maximize the benefits of MLflow and ensure a smooth and efficient ML lifecycle management process.

## Introduction to MLflow - Key things to consider in MLflow
https://MLflow.org/docs/latest/introduction/index.html
https://viso.ai/deep-learning/MLflow-machine-learning-experimentation/

When working with MLflow, a platform for managing the ML lifecycle, there are several key considerations to ensure you effectively use the tool for experiment tracking, model management, and deployment. Here are the primary things to consider:

https://MLflow.org/docs/latest/introduction/index.html#use-cases-of-MLflow
### 1. Experiment Tracking:
   - Experiment Organization: Organize your experiments logically, using meaningful names and descriptions. This helps in identifying the purpose and context of each experiment.
   - Logging Parameters and Metrics: Ensure you log all relevant parameters, metrics, and artifacts (e.g., model weights, plots) using `MLflow.log_param()`, `MLflow.log_metric()`, and `MLflow.log_artifact()`. This helps in comparing different runs and analyzing model performance.
   - Versioning: Track the version of the code, data, and environment configurations used in each experiment. This is crucial for 'Reproducibility'.

### 2. Model Management:
   - Model Registry: Use the MLflow Model Registry to manage the lifecycle of your models ('Staging', 'Production', etc.). The registry allows you to transition models through various stages and maintain Version Control.
   - Model Signature: Ensure your models include a signature, which captures the input and output schema of the model. This helps in validating input data during deployment.
   - Packaging and Deployment: Consider how you will package and deploy models using MLflow. MLflow supports multiple deployment targets, such as 'Docker', 'Kubernetes', and 'Cloud platforms'. Make sure you understand the deployment environment and any specific requirements.

### 3. Reproducibility:
   - Environment Management: Capture the environment in which the experiment was run (e.g., Python packages, versions). MLflow supports environment logging through `MLflow.pyfunc.log_model()` and other utilities. This ensures that the model can be reproduced in the same environment.
   - Data Versioning: Keep track of the datasets used in experiments. Consider using tools like DVC (Data Version Control) alongside MLflow for versioning large datasets.
   - Code Versioning: Integrate MLflow with your version control system (e.g., Git) to track the exact codebase used for each experiment.

### 4. Collaboration:
   - Access Control: If multiple users or teams are using MLflow, ensure that access control and permissions are appropriately configured. This is particularly important in a shared or production environment.
   - Experiment Sharing: Leverage MLflow’s capabilities to share experiments, models, and insights across teams. This fosters collaboration and helps avoid redundant work.

### 5. Scalability:
   - Tracking Server: Set up a central 'MLflow Tracking Server' if you need to scale MLflow across multiple machines or teams. This server will store all experiment data, models, and logs in a central location.
   - Database and Artifact Store: Configure a robust database (e.g., 'MySQL', 'PostgreSQL') and artifact store (e.g., 'AWS S3', 'Azure Blob Storage') to handle large volumes of experiment data and artifacts.
   - Performance Considerations: Monitor the performance of your MLflow server and adjust configurations such as database connections, storage options, and logging frequency as needed.

### 6. Compliance and Security:
   - Data Privacy: Ensure that sensitive data is not logged inadvertently. Mask or omit any personal or sensitive information from logs and artifacts.
   - Audit Trails: Use MLflow’s logging capabilities to maintain an audit trail of model changes, experiment results, and deployment decisions. This is critical for regulatory compliance in certain industries.
   - Encryption and Security: Ensure that your MLflow instance, especially when exposed over the internet, is secured using SSL/TLS, and that data is encrypted in transit and at rest.

### 7. Integration with CI/CD Pipelines:
   - Automated Workflows: Integrate MLflow with your CI/CD pipelines to automate the model training, testing, and deployment process. This helps in continuously delivering improvements to models in production.
   - Testing and Validation: Implement automated tests for your models (e.g., performance checks, data validation) within the MLflow pipeline to ensure quality before deployment.

### 8. Monitoring and Logging:
   - Production Monitoring: Once a model is deployed, use MLflow to monitor its performance in production. Track metrics like prediction latency, accuracy, and data drift.
   - Logging and Alerts: Set up logging and alerts for any anomalies in model performance or operational issues. This ensures timely intervention if the model behavior deviates from expectations.

### 9. Extensibility and Customization:
   - Custom Plugins and Models: If MLflow’s built-in functionality doesn’t cover your needs, consider writing custom plugins or models. MLflow’s flexible architecture allows for custom integrations and extensions.
   - MLflow Projects: Use MLflow Projects to encapsulate your data science code in a reusable and reproducible way, which can be easily shared and executed by others.

### 10. Documentation and Training:
   - User Documentation: Maintain comprehensive documentation for how MLflow is set up, including best practices for usage within your organization.
   - Training and Onboarding: Provide training for new users or team members to get up to speed with MLflow’s capabilities, ensuring that everyone is using the tool effectively.

## Components of MLflow
- MLflow Tracking: Record and query experiments (code, data, config, and result)
- MLflow Projects: Package code in a format to reproduce runs on any platform
- MLflow Models: Deploy ML models in diverse serving environments
- Model Registry: Store, annotate, discover, and manage models in a central repository

## Compatibility of MLflow
https://MLflow.org/docs/latest/introduction/index.html?highlight=programming%20language#why-use-MLflow

- Compatible with various popular ML libraries
- Support API for Java, Python, and R, backed by a robust REST API and CLI
- Integrating MLflow with your code is a straightforward process

## Use Case of MLflow
- Experiment tracking, 
- Model lifecycle management ('Staging' for rollout and rollback), 
- Reproducible research, 
- Deployment (MLflow's `MLflow models serve` command quickly deploy model as a REST endpoint in production.), 
- CI/CD pipelines for ML, 
- Collaboration (Central Registry), 
- Production monitoring, 
- Regulatory compliance, 
- Multi-platform and multi-language support, and 
- Custom workflows and extensions (MLflow can be extended with custom plugins). 

### Getting System Ready with MLflow
MLFlow-Manage-ML-Experiments
cd MLFlow-Manage-ML-Experiments
python -m venv mlflow-venv
mlflow-venv\Scripts\activate

    (mlflow-venv) D:\development\Complete-MLOps-BootCamp ...

pip install setuptools
pip install mlflow
mlflow --version
    mlflow, version 2.15.1

mlflow
    ...
    Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

    Commands:
      artifacts    Upload, list, and download artifacts from an MLflow...
      db           Commands for managing an MLflow tracking database.
      deployments  Deploy MLflow models to custom targets.
      doctor       Prints out useful information for debugging issues with MLflow.
      experiments  Manage experiments.
      gc           Permanently delete runs in the `deleted` lifecycle stage.
      models       Deploy MLflow models locally.
      recipes      Run MLflow Recipes and inspect recipe results.
      run          Run an MLflow project from the given URI.
      runs         Manage runs.
      sagemaker    Serve models on SageMaker.
      server       Run the MLflow tracking server.

mlflow ui

http://127.0.0.1:5000
