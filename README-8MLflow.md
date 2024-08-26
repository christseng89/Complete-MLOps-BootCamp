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
MLflow-Manage-ML-Experiments
cd MLFlow-Manage-ML-Experiments
python -m venv mlflow-venv
mlflow-venv\Scripts\activate

    (mlflow-venv) D:\development\Complete-MLOps-BootCamp ...

pip install setuptools
pip install mlflow --user --no-warn-script-location
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

### Logging Functions of MLflow Tracking ('mlruns' folder => '0' => meta.yaml)

https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html

// Notes on Logging Functions of MLflow Tracking
- `mlflow.set_tracking_uri()` connects to a tracking URI. You can also set the MLFLOW_TRACKING_URI environment variable to have MLflow find a URI from there. In both cases, the URI can either be a HTTP/HTTPS URI for a remote server, a database connection string, or a local path to log data to a directory. The URI defaults to mlruns.

- `mlflow.get_tracking_uri()` returns the current tracking URI.

- `mlflow.create_experiment()` creates a new experiment and returns its ID. Runs can be launched under the experiment by passing the experiment ID to mlflow.start_run.

- `mlflow.set_experiment()` sets an experiment as active. If the experiment does not exist, creates a new experiment. If you do not specify an experiment in mlflow.start_run(), new runs are launched under this experiment.

- `mlflow.start_run()` returns the currently active run (if one exists), or starts a new run and returns a mlflow.ActiveRun object usable as a context manager for the current run. You do not need to call start_run explicitly: calling one of the logging functions with no active run automatically starts a new one.

- `mlflow.end_run()` ends the currently active run, if any, taking an optional run status.

- `mlflow.log_param()` logs a single key-value param in the currently active run. The key and value are both strings. Use mlflow.log_params() to log multiple params at once.

- `mlflow.log_metric()` logs a single key-value metric. The value must always be a number. MLflow remembers the history of values for each metric. Use mlflow.log_metrics() to log multiple metrics at once.

- `mlflow.set_tag()` sets a single key-value tag in the currently active run. The key and value are both strings. Use mlflow.set_tags() to set multiple tags at once.

- `mlflow.log_artifact()` logs a local file or directory as an artifact, optionally taking an artifact_path to place it in within the run’s artifact URI. Run artifacts can be organized into directories, so you can place the artifact in a directory this way.

- `mlflow.log_artifacts()` logs all the files in a given directory as artifacts, again taking an optional artifact_path.

help.py # Sample program to use MLflow APIs

### Basic MLflow tutorial
https://docs.python.org/3/library/argparse.html

demo.py
rd mlruns /s

python demo.py 

   Input Arguments: 5 and 10
   2024/08/21 18:02:41 INFO mlflow.tracking.fluent: Experiment with name 'Demo_Experiment' does not exist. Creating a new experiment.
   MLFlow Run Completed

mlruns => 853229105381995442 (experiment_id) => go thru all meta.yaml...

mlflow ui

http://127.0.0.1:5000/ => Demo_Experiment => Run Name (masked-penguin-758)
- Overview
   - Created at
   - Experiment ID
   - Run ID
   - Source
   - Parameters (2)
- Model metrics (5*5 + 10*10 = 125)
- Artifacts

### Exploration of MLflow
cd MLFlow-Manage-ML-Experiments
mlflow-venv\Scripts\activate
mlflow ui

cd MLFlow-Manage-ML-Experiments
mlflow-venv\Scripts\activate
python demo.py 
python demo.py -p1 3 -p2 5

http://127.0.0.1:5000/ => Demo_Experiment => Run Name (2 names) => Compare
- Box Plot
   - Parameters
   - Metrics
   - Tags

### Machine Learning Experiment on MLflow
basic_ml.py

python basic_ml.py
python basic_ml_finetune1.py
python basic_ml_finetune2.py

http://127.0.0.1:5000/ 

1. => ML-Model-1 => Run Name (2 names) => Compare
2. => ML-Model-1 => Columns
3. => ML-Model-1 => Chart => Run Name (all) => + Add chart => Parallel Coordinates => 
   - Params (alpha, l1ratio)
   - Metrics (r2-score) => Add Chart

### Create ML Model for Loan Prediction
loan_prediction.py

Random =>   
   https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

Tree =>     
   https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

Linear =>   
   https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

GridSearchCV => 
   https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#
   https://scikit-learn.org/stable/modules/grid_search.html#grid-search

python loan_prediction.py

// Conclusion => Adopt RandomForestClassifier 

### Install Anaconda (Prerequisite for MLflow Project)
// Anaconda3-2024.06-1-Windows-x86_64.exe => 
// Add Path C:\ProgramData\anaconda3\Scripts

cd MLFlow-Manage-ML-Experiments
mlflow-venv\Scripts\activate

### MLflow Project
https://mlflow.org/docs/latest/projects.html
https://mlflow.org/docs/latest/projects.html#mlproject-file

MLProject
conda.yaml
   http://127.0.0.1:5000 => Run Name => Artifacts => conda.yaml

mlflow run --experiment-name Loan_prediction .
   ...
   *** MLFlow Completed ***
   2024/08/23 16:18:54 INFO mlflow.projects: === Run (ID 'bc64b3a0ed7840b4b0e30ccaffca68b2') succeeded ===

http://127.0.0.1:5000 => Loan_prediction => Source (D:\development\Complete-MLOps-BootCamp#\...)

// Project required files => Create a Git repository
- MLProject
- conda.yaml
- loan_prediction.py
- train.csv

mlflow run https://github.com... --experiment-name Loan_prediction

### MLflow Models
mlflow.sklearn.log_model(model, name, input_example=input_example)

http://127.0.0.1:5000 => Run Name => Artifacts

   GradientBoostingClassifier => Make Predictions (Predict on a Pandas DataFrame, Predict on a Spark DataFrame)
      MLmodel
      conda.yaml
      input_example.json
      model.pkl
      python_env.yaml
      requirements.txt
      serving_input_payload.json
   ROC_curve.png

test-model-panda.py
python test-model-panda.py
   Prediction is : [0]

// Serve the Models with Local REST server
// mlflow models serve -m runs:/<RUN_ID>/<model> --no-conda --port 9000 => "runs:/<RUN_ID>/<model>" from the Artifacts

mlflow models serve -m runs:/a9f8b05dd54c42dda1a81d9fc8d9abcd/GradientBoostingClassifier --no-conda --port 9000
   ...
   flow mlflow.pyfunc.scoring_server.wsgi:app'
   INFO:waitress:Serving on http://127.0.0.1:9000

// Postman => MLflow => Test Model Gradient Boosting Classifier (Post http://127.0.0.1:9000/invocations)
   {
      "predictions": [
         0
      ]
   }

// GitBash
curl --location 'http://127.0.0.1:9000/invocations' \
--header 'Content-Type: application/json' \
--data '{
    "dataframe_split": {
        "columns": [
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
        ],
        "data": [
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
    }
}'

//{"predictions": [0]}

### MLflow Registry

#### Setting Up MySql Database Locally
https://dev.mysql.com/downloads/mysql/
https://dev.mysql.com/downloads/workbench/

root/t1xxx$Xxxxx

// MySQL Workbench => Create Schema => db_mlflow

#### Log Model Metrics in MySql
// install mysql-client
cd MLFlow-Manage-ML-Experiments
mlflow-venv\Scripts\activate

pip install mysqlclient

#### Log Model Metrics in MySql
https://mlflow.org/docs/latest/tracking/server.html
https://docs.sqlalchemy.org/en/20/core/engines.html#mysql

// Stop mlflow ui
mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri mysql://root:t1216$Chris@localhost/db_mlflow --default-artifact-root mlruns
   ... 
   INFO  [89d4b8295536_create_latest_metrics_table_py] Migration complete!
   INFO  [2b4d017a5e9b_add_model_registry_tables_to_db_py] Migration complete!
   ...
   INFO  [alembic.runtime.migration] Context impl MySQLImpl.
   INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
   INFO:waitress:Serving on http://127.0.0.1:5000

// delete mlruns folder
// revise load_prediction.py
python loan_prediction.py

// MySQL Workbench => View all tables (tags, runs, params, metrics etc.)

set MLFLOW_TRACKING_URI=http://127.0.0.1:5000
echo %MLFLOW_TRACKING_URI% 

mlflow run --experiment-name Loan_prediction .
