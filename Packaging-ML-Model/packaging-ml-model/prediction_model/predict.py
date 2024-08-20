import pandas as pd
import numpy as np
# import joblib

from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config  
from prediction_model.processing.data_handling import load_pipeline, load_dataset

classification_pipeline = load_pipeline(config.MODEL_NAME)

# def generate_predictions(data_input): # TEST_FILE = 'test.csv'
#     data = pd.DataFrame(data_input)
#     pred = classification_pipeline.predict(data[config.FEATURES]) # predict is part of joblib.load(save_path) 
#     output = np.where(pred==1,'Y','N')
#     result = {"prediction":output}
#     return result

def generate_predictions(single_row=None):
    if single_row is not None:
        test_data = single_row
    else:
        test_data = load_dataset(config.TEST_FILE)
    
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred == 1, 'Y', 'N')
    
    # Return a dictionary with the prediction results
    result = {"prediction": output}
    return result

if __name__=='__main__':
    generate_predictions()