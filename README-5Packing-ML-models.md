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
python -m venv mlenv

mlenv\Scripts\activate # Windows
source mlenv/bin/activate # Ubuntu

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
