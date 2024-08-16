import os
import pandas as pd
import joblib

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config

#Load the dataset
def load_dataset(file_name): # File Name = train.csv
    filepath = os.path.join(config.DATAPATH,file_name) # Data Path = datasets
    _data = pd.read_csv(filepath)
    return _data

#Serialization
def save_pipeline(pipeline_to_save): # Pipeline to save => log
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME) 
    # Path = trained_models
    # Model Name = classification.pkl
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#Deserialization
def load_pipeline(pipeline_to_load): # Pipeline to load => final_model
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    model_loaded = joblib.load(save_path)
    print(f"Model has been loaded")
    return model_loaded