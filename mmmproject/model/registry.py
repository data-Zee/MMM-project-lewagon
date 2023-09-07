import pandas as pd
import os
import pickle
import datetime
from google.cloud import storage
from mmmproject.model.params import *
from sklearn.model_selection import TimeSeriesSplit
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import MinMaxScaler
#from mmmproject.model.weekendclass import AddWeekendsTransformer
import traceback

class AddWeekendsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # This transformer doesn't need to learn any parameters during fitting,
        # so we simply return self.
        return self

    def transform(self, X):
        """Creates a new column with row value = 1 if the day is a Friday or Saturday and 0 if not."""
        df = X.copy()  # Create a copy of the input DataFrame to avoid modifying it directly
        weekday_values = df.index.weekday
        df['fri_sat'] = ((weekday_values == 4) | (weekday_values == 5)).astype(int)
        return df[['fri_sat']]

def load_model(flag="default"):
    dirname = os.path.dirname(os.path.abspath(__file__))
    path_load = os.path.join(dirname,"..", "..", "pipelines")

    if MODEL_TARGET == "local":
        model_path = os.path.join(path_load, "pipeline-2023-08-31.pkl")
        model = pickle.load(open(model_path, 'rb'))

    elif MODEL_TARGET == "gcs":

        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)

        try:
            # Create a blob object from the filepath
            blob = bucket.blob("model.pkl")
            print('blob_created')
            # Download the file to a destination
            latest_model_path_to_save = os.path.join(MODEL_REGISTRY_PATH, 'model.pkl')
            blob.download_to_filename(latest_model_path_to_save)
            print('blob_downloaded')
            latest_model = pickle.load(open(latest_model_path_to_save, 'rb'))

            print("✅ Latest model downloaded from cloud storage")

            return latest_model
        except:
            print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}")

def load_pipeline(flag="default"):
    # dirname = os.path.dirname(os.path.abspath(__file__))
    dirname = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    path_load = os.path.join(dirname,"..", "..", "pipelines")

    if MODEL_TARGET == "local":
        model_path = os.path.join(path_load, "pipeline-2023-08-31.pkl")
        model = pickle.load(open(model_path, 'rb'))

    elif MODEL_TARGET == "gcs":

        client = storage.Client()
        bucket = client.get_bucket(BUCKET_NAME)

        try:
            # Create a blob object from the filepath
            blob = bucket.blob("pipelines/pipeline-2023-09-06 17:09:02.597279")
            print('blob_created')
            # Download the file to a destination
            # latest_model_path_to_save = os.path.join(MODEL_REGISTRY_PATH, 'pipeline.pkl')
            local_path = os.path.join(dirname ,'pipelines','latest_pipeline.pkl')
            (print(local_path))
            blob.download_to_filename(local_path)
            print('blob_downloaded')
            latest_model = pickle.load(open(local_path, 'rb'))


            print("✅ Latest pipeline downloaded from cloud storage")

            return latest_model
        except Exception as e:
            print(e)
            print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}")
            print(__name__)

    else:
        model = None
    return model

if __name__ == "__main__":

    local_file_name = "/Users/noaruccius/code/data-Zee/MMM-project-lewagon/pipelines/latest_pipeline.pkl"
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob("pipelines/pipeline-2023-09-06 17:09:02.597279")
    blob.upload_from_filename(local_file_name)

def minmax_fb(x):
    scaled_fb = ((x - 0)/(2294.69 - 0))
    return scaled_fb
def minmax_gg(x):
    scaled_gg = ((x - 0)/(480.66 - 0))
    return scaled_gg
def minmax_tt(x):
    scaled_tt = ((x - 0)/(840.37- 0))
    return scaled_tt


# save as pickle file
# def save_model():
#     parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     data_dir = 'raw_data'
#     data_file = 'df_clean.csv'

#     pipeline_save_path = os.path.join(parent_dir,'pipelines',f'pipeline-{datetime.datetime.now()}.pkl')
#     with open(pipeline_save_path, 'wb') as file:
#        pickle.dump(model, file)
