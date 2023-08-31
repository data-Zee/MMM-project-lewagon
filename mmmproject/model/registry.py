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
