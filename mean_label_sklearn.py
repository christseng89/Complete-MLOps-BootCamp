import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin

# MeanImputer
class MeanImputer(BaseEstimator, TransformerMixin): 
    def __init__(self, variables=None):
        self.variables = variables
    
    def fit(self, X, y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self, X):
        # print(f"MeanImputer.transform() called with X: {X}")
        X = X.copy()
        for col in self.variables:
            X[col].fillna(self.mean_dict[col], inplace=True)
        return X

# Sample dataset with missing values
data = {
    'age': [25, 30, np.nan, 40, 35],
    'salary': [50000, 60000, 55000, np.nan, 70000],
    'experience': [1, 3, np.nan, 8, 5]
}

df = pd.DataFrame(data)
imputer = MeanImputer(variables=['age', 'salary', 'experience'])
imputer.fit(df)

print("\nMean values calculated during fit:")
print(imputer.mean_dict)

df_imputed = imputer.transform(df)

print("\nDataFrame after applying MeanImputer:")
print(df_imputed)

# LogTransforms
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
    
imputer = LogTransforms(variables=['age', 'salary', 'experience'])
imputer.fit(df_imputed)
df_log_transformed = imputer.transform(df_imputed)
print("\nDataFrame after applying LogTransforms:")
print(df_log_transformed)

# CustomLabelEncoder
class CustomLabelEncoder(BaseEstimator, TransformerMixin):
    # Encodes categorical variables based on their frequency (least frequent category gets the lowest value).
    def __init__(self, variables=None):
        self.variables = variables
    
    def fit(self, X, y=None):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index
            self.label_dict[var] = {k: i for i, k in enumerate(t, 0)}
        # print(f"\nLabel dict: {self.label_dict}")
        # self.label_dict = {'age': {20: 0, 25: 1, 30: 2}, 'salary': {6000: 0, 50000: 1, 7000: 2, 5000: 3}, 'experience': {2: 0, 1: 1, 3: 2}}
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].map(self.label_dict[col])
        return X

# Test LabelEncoder 
data = {
    'age': [25, 30, 20, 25, 30],
    'salary': [5000, 6000, 5000, 50000, 7000],
    'experience': [1, 3, 3, 2, 1]
}

df = pd.DataFrame(data)
# Use the CustomLabelEncoder
encoder = CustomLabelEncoder(variables=['age', 'salary', 'experience'])
encoder.fit(df)  # No error now
df_encoded = encoder.transform(df)
print("\nDataFrame after applying CustomLabelEncoder:")
print(df_encoded)
