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
