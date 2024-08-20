# Packing the ML Models (Section 5)

## Jupyter
jupyter lab

## Datasets
- Folder => Packaging-ML-Model\Experiments
- File => train.csv

### Source
- File => Loan-Experiment-Data-Scientist

### Building the Model
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(train_df,train_y,test_size=0.3, random_state=0)

from sklearn.linear_model import LogisticRegression
log = LogisticRegression() # Create and init the training model
log.fit(X_train,y_train)

### Challenges in Working inside the Jupyter Notebook

#### 1 Create Virtual Environment 
python -m venv myenv

myenv\Scripts\activate # Windows
source myenv/bin/activate # Ubuntu

#### 2 Dependencies (under virtual environment via requirements.txt)
// Create requirements file
pip freeze > requirements.txt
- requirements.txt

pip install -r requirements.txt

#### 3 Serialization and Deserialization of ML Models (joblib, pickle)
// serialization
import joblib
joblib.dump(log,"my_trained_model_v1.pkl")

// deserialization
final_model = joblib.load("my_trained_model_v1.pkl")

#### 4 Testing the Python code (pytest)

#### 5 Cannot use Python notebook for Production
- Difficult to debug
- Require changes in multiple places
- Lots of dependencies
- No modularity in the code
- Conflict of variables and functions
- Duplicate code snippets

=> Solutions
- Write Python scripts
- Follow modular programming
- Create package

### Module and Package Programming
// Module in Python
- A Python file can hold Classes, Functions and Variables.

// Package in Python
- One or more modules that are interlinked with each other
- A directory with subdirectories can be called a package if it contains __init__.py file.

// Package Folder Structure
PackageA
 - __init__.py
 - f1.py
 - f2.py
 - SubPackageA
   - __init__.py
   - f3.py
   - f4.py
 - SubPackageB
   - __init__.py
   - f5.py

import PackageA # import packageA
from PackageA import f1 # import module f1
from PackageA.SubPackageA import f3
from PackageA.SubPackageB import f5

### Building the ML Model Package
- Create package
- Maintain the separate modules
- Maintain separate files for 
  - Preprocessing
  - Data handling
  - Manual configuration etc.
- Build test cases (verify the integrity)

Folder => Packaging-ML-Model\packaging-ml-model

// Packing and Distribution Projects
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
Setup Tools https://packaging.python.org/en/latest/key_projects/#setuptools

### Creating Folder Hierarchy for ML Project
- setup.py (v)
- setup.cfg
- README.md (v)
- MANIFEST.in (v)
- LICENSE.txt
- prediction_model
  - config
    - config.py
  - datasets
    - *.csv ...
  - processing
    - data_handling.py
    - preprocessing.py
  - trained_models
  - pipeline.py
  - predict.py  
  - training_pipeline.py
- requirements.txt (v)
- tests
  - pytests.ini
  - test_prediction.py

// Packaging your project
https://packaging.python.org/en/latest/tutorials/packaging-projects/

https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#packaging-your-project

// Create a Source Distribution
https://docs.python.org/3.10/distutils/introduction.html
- 1. An Introduction to Distutils
- 2. Writing the Setup Script
- 3. Writing the Setup Configuration File
- 4. Creating a Source Distribution
- 5. Creating Built Distributions
- 6. Distutils Examples
- 7. Extending Distutils

https://docs.python.org/3.10/distutils/sourcedist.html

### Create Config Module
config.py

- import prediction_model
- all constants

### Data Handling Module
data_handling.py

- Serialization
- Deserialization

### Data Preprocessing
preprocessing.py

https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

// Templates
from sklearn.base import BaseEstimator,TransformerMixin

class DemoTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        return X

### Sklearn pipeline
pipeline.py

import prediction_model.processing.preprocessing as pp 
...
// Pipeline
- 'DomainProcessing',pp.DomainProcessing(variable_to_modify = config.FEATURE_TO_MODIFY,
    variable_to_add = config.FEATURE_TO_ADD)
- 'DropFeatures', pp.DropColumns(variables_to_drop=config.DROP_FEATURES)
- 'MeanImputation', pp.MeanImputer(variables=config.NUM_FEATURES)
- 'ModeImputation',pp.ModeImputer(variables=config.CAT_FEATURES)
- 'LabelEncoder',pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)
- 'LogTransform',pp.LogTransforms(variables=config.LOG_FEATURES)

### Training pipeline
training_pipeline.py

This Training Pipeline automates the entire process of preparing data, applying transformations, and training a ML model, making it easy to apply the same transformations and model to new, unseen data.

- Data Loading: The training dataset is loaded.
- Target Preparation: The target variable (e.g., loan status) is transformed into binary labels.
- Pipeline Training: The preprocessing pipeline and logistic regression model are trained on the training data.
- Pipeline Saving: The trained pipeline is saved for future use (e.g., making predictions).

### Predict pipeline
predict.py

load_pipeline.predict() // predict feature

## Perform Training and Predictions
cd Packaging-ML-Model\packaging-ml-model

pip list ### Get the required package versions then update requirements.txt

python -m venv mlenv
mlenv\Scripts\activate

// (mlenv) ....
pip install -r requirements.txt
python.exe -m pip install --upgrade pip

cd prediction_model
python training_pipeline.py
  ...
  Model has been saved under the name classification.pkl

python predict.py
  ['Y' 'Y' 'Y' 'Y' 'Y' 'Y' 'Y' 'N' 'Y' 'Y' 'Y' 'Y' 'Y' 'N' 'Y' 'Y' 'Y' 'Y'...]
  // Y = Approved
  // N = Not Approved

###  Testing the New Virtual Environments
cd ..
deactivate

pip install virtualenv
virtualenv --version
  virtualenv 20.26.3 from C:\Python312\Lib\site-packages\virtualenv\__init__.py

virtualenv ml_package
  ...
  added seed packages: pip==24.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

ml_package\Scripts\activate
  (ml_package) ...

pip install -r requirements.txt
python.exe -m pip install --upgrade pip
cd prediction_model
python training_pipeline.py
  ...
  Model has been saved under the name classification.pkl

## Introduction to Pytest

### Why Pytest
- Intuitive Syntax: pytest offers a readable, expressive way to write test
- Powerful Fixtures: Easily setup and tear down test environments with fixtures
- Rich Plugin Ecosystem: Extend pytest's capabilities with a wide range of plugins
- Excellent Community Support: Benefit from a large, active community

### Pytest conventions
- Test Files: Name them with 'test_' at the beginning or '_test.py' at the end.
- Test Functions: Name them with 'test_' at the beginning.
- Test Classes: Name them with 'Test' at the beginning, and include methods that start with 'test_'.
- Setup/Teardown: Use 'setup_method', 'teardown_method', 'setup_class', and 'teardown_class' for setup and teardown logic.
- Assertions: Use Python's build-in assert statements.

### Pytest Fixtures
- Reusable Setup and Teardown (Clean up)
- Scoping (function, module, session, etc.)
- Parameterization (Run tests with different input data)

Fixture examples:
@pytest.fixture
@pytest.fixture(params=["sqlite", "postgresql", "mysql"])
@pytest.fixture(scope="module")
@pytest.mark.parametrize("input,expected", [(1, 2), (3, 4), (5, 6)])
@pytest.mark.slow

### Leveling up with Pytest
- Marking: Test Marking - Categorize tests with marks for selective execution
- Expand: Parametrization - Expand test coverage with variations
- Integrate: Plugins - Integrate tools for reporting, code coverage, and more
- Command: Command line options - Customize test execution (pytest --help)

### Pytest Hands on
cd Packaging-ML-Model\packaging-ml-model\pytest_example
add_subtract.py
app.py

test_add_subtract.py
test_app.py

pip install flask
python app.py

http://127.0.0.1:5001/

pytest

  ...
  test_add_subtract.py ..                            [ 66%]
  test_app.py .                                      [100%]

  =================== 3 passed in 2.16s =================== 

### Pytest fixtures
test_add_subtract_fixture.py
pytest test_add_subtract_fixture.py

  ...
  test_add_subtract_fixture.py ..                                                [100%] 

  ================================= 2 passed in 0.06s =================================

pytest test_add_subtract_fixture.py -s -v

  ...
  test_add_subtract_fixture.py::test_add Setup add and subtract
  PASSED
  test_add_subtract_fixture.py::test_subtract Setup add and subtract
  PASSED
  ================================= 2 passed in 0.06s =================================

### Create and Run Python Tests for ML Project
cd Packaging-ML-Model\Pytest_example
python app.py
pytest

cd ..\packaging-ml-model
tests\test_prediction.py
tests\test_jupyter.py

pytest

...
tests\test_jupyter.py .                                            [ 25%]
tests\test_prediction.py ...                                       [100%]
=========================== 4 passed in 1.98s ===========================

## ML Package Building
https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

### Create Manifest file and VERSION file
https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html

MANIFEST.ini
VERSION

__init__.py

import os 
from prediction_model.config import config
with open(os.path.join(config.PACKAGE_ROOT,'VERSION')) as f : 
    __version__ = f.read().strip()

### Create setup.py
https://setuptools.pypa.io/en/latest/
https://setuptools.pypa.io/en/latest/userguide/quickstart.html

pip install --upgrade setuptools
pip install --upgrade build

cd Packaging-ML-Model/packaging-ml-model
python -m build
  ...
  Successfully built prediction_model-1.0.0.tar.gz and prediction_model-1.0.0-py3-none-any.whl

// folder => prediction_model.egg-info

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
https://mlflow.org/docs/latest/introduction/index.html

When working with MLflow, a platform for managing the ML lifecycle, there are several key considerations to ensure you effectively use the tool for experiment tracking, model management, and deployment. Here are the primary things to consider:

https://mlflow.org/docs/latest/introduction/index.html#use-cases-of-mlflow
### 1. Experiment Tracking:
   - Experiment Organization: Organize your experiments logically, using meaningful names and descriptions. This helps in identifying the purpose and context of each experiment.
   - Logging Parameters and Metrics: Ensure you log all relevant parameters, metrics, and artifacts (e.g., model weights, plots) using `mlflow.log_param()`, `mlflow.log_metric()`, and `mlflow.log_artifact()`. This helps in comparing different runs and analyzing model performance.
   - Versioning: Track the version of the code, data, and environment configurations used in each experiment. This is crucial for 'Reproducibility'.

### 2. Model Management:
   - Model Registry: Use the MLflow Model Registry to manage the lifecycle of your models ('Staging', 'Production', etc.). The registry allows you to transition models through various stages and maintain Version Control.
   - Model Signature: Ensure your models include a signature, which captures the input and output schema of the model. This helps in validating input data during deployment.
   - Packaging and Deployment: Consider how you will package and deploy models using MLflow. MLflow supports multiple deployment targets, such as 'Docker', 'Kubernetes', and 'Cloud platforms'. Make sure you understand the deployment environment and any specific requirements.

### 3. Reproducibility:
   - Environment Management: Capture the environment in which the experiment was run (e.g., Python packages, versions). MLflow supports environment logging through `mlflow.pyfunc.log_model()` and other utilities. This ensures that the model can be reproduced in the same environment.
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
https://mlflow.org/docs/latest/introduction/index.html?highlight=programming%20language#why-use-mlflow

- Compatible with various popular ML libraries
- Support API for Java, Python, and R, backed by a robust REST API and CLI
- Integrating MLflow with your code is a straightforward process

## Use Case of MLflow
- Experiment tracking, 
- Model lifecycle management ('Staging' for rollout and rollback), 
- Reproducible research, 
- Deployment (MLflow's `mlflow models serve` command quickly deploy model as a REST endpoint in production.), 
- CI/CD pipelines for ML, 
- Collaboration (Central Registry), 
- Production monitoring, 
- Regulatory compliance, 
- Multi-platform and multi-language support, and 
- Custom workflows and extensions (MLflow can be extended with custom plugins). 
