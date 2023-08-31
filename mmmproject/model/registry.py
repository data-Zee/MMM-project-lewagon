import pandas as pd
import os
import pickle
from datetime import datetime

def load_model(flag="default"):
    dirname = os.path.dirname(os.path.abspath(__file__))
    path_load = os.path.join(dirname,"..", "..", "pipelines")

    if flag == "default":
        model_path = os.path.join(path_load, "pipeline-2023-08-31.pkl")
        model = pickle.load(open(model_path, 'rb'))

    else:
        model = None
    return model

# def save_model():
#     parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     data_dir = 'raw_data'
#     data_file = 'df_clean.csv'

#     pipeline_save_path = os.path.join(parent_dir,'pipelines',f'pipeline-{datetime.now()}.pkl')
#     with open(pipeline_save_path, 'wb') as file:
#     pickle.dump(model, file)
