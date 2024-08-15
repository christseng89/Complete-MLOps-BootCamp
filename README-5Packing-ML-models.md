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