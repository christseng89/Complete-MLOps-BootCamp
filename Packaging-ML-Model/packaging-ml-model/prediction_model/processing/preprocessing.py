from sklearn.base import BaseEstimator,TransformerMixin

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

# from prediction_model.config import config
import numpy as np

class MeanImputer(BaseEstimator,TransformerMixin): 
    # Imputes missing values in columns with the mean of those columns.
    def __init__(self,variables=None): 
        self.variables = variables
    
    def fit(self,X,y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            # X[col].fillna(self.mean_dict[col],inplace=True)
            X[col] = X[col].fillna(self.mean_dict[col])
        return X


class ModeImputer(BaseEstimator,TransformerMixin):
    # Imputes missing values in columns with the mode (most frequent value) of those columns.
    def __init__(self,variables=None):
        self.variables = variables
    
    def fit(self,X,y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            # X[col].fillna(self.mode_dict[col],inplace=True)
            X[col].fillna(self.mode_dict[col])
        return X

class DropColumns(BaseEstimator,TransformerMixin):
    # Drops columns from the dataset.
    def __init__(self,variables_to_drop=None):
        self.variables_to_drop = variables_to_drop
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        X = X.drop(columns = self.variables_to_drop)
        return X

class DomainProcessing(BaseEstimator,TransformerMixin):
    # Modifies specified columns by adding the values from a specified column.
    def __init__(self,variable_to_modify = None, variable_to_add = None):
        self.variable_to_modify = variable_to_modify
        self.variable_to_add = variable_to_add
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variable_to_modify:
            X[col] = X[col] + X[self.variable_to_add]
        return X

class CustomLabelEncoder(BaseEstimator,TransformerMixin):
    # Encodes categorical variables based on their frequency (least frequent category gets the lowest value).
    def __init__(self, variables=None):
        self.variables=variables
    
    def fit(self, X,y):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index 
            self.label_dict[var] = {k:i for i,k in enumerate(t,0)}
        return self
    
    def transform(self,X):
        X=X.copy()
        for col in self.variables:
            X[col] = X[col].map(self.label_dict[col])
        return X

# Try out Log Transformation
class LogTransforms(BaseEstimator,TransformerMixin):
    # Applies a logarithmic transformation to specified columns.
    def __init__(self,variables=None):
        self.variables = variables
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            X[col] = np.log(X[col])
        return X
    