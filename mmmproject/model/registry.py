import pandas as pd
import os
import pickle
from datetime import datetime
from google.cloud import storage
from mmmproject.model.params import *

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
            latest_model_path_to_save = os.path.join(MODEL_REGISTRY_PATH, 'pipeline.pkl')
            blob.download_to_filename(latest_model_path_to_save)
            print('blob_downloaded')
            latest_model = pickle.load(open(latest_model_path_to_save, 'rb'))

            print("✅ Latest pipeline downloaded from cloud storage")

            return latest_model
        except:
            print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}")


    else:
        model = None
    return model

if __name__ == "__main__":
    storage_file_name = os.path.join(MODEL_REGISTRY_PATH, 'pipeline.pkl')
    local_file_name = "/Users/noaruccius/code/data-Zee/MMM-project-lewagon/pipelines/pipeline-2023-09-06 17:09:02.597279.pkl"
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(storage_file_name)
    blob.upload_from_filename(local_file_name)


# save as pickle file
# def save_model():
#     parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     data_dir = 'raw_data'
#     data_file = 'df_clean.csv'

#     pipeline_save_path = os.path.join(parent_dir,'pipelines',f'pipeline-{datetime.now()}.pkl')
#     with open(pipeline_save_path, 'wb') as file:
#        pickle.dump(model, file)
