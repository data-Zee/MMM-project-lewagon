
# this .py file has been created by guido to have test data and test model for api
# is replaced by Victor -> registry.py -> loading model from pickle







# import pandas as pd
# from mamimo.carryover import ExponentialCarryover
# from mamimo.saturation import ExponentialSaturation
# from mamimo.linear_model import LinearRegression
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LinearRegression
# import os
# import pickle
# from datetime import datetime


# parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# data_dir = 'raw_data'
# data_file = 'df_clean.csv'

# def get_data(csv_path: str):
#     df = pd.read_csv(csv_path)
#     df = df.drop(columns='Unnamed: 0')
#     df['Day'] = pd.to_datetime(df['Day'])
#     df.set_index('Day', inplace=True)
#     df = df.rename(columns={"fb_costs": "facebook", "google_costs": "google", "tt_costs": "tiktok"})

#     # create a simple_df
#     simple_df = df.drop(columns = ['fb_impressions', 'fb_clicks', 'google_impressions', 'google_clicks', 'tt_impressions', 'tt_clicks'])
#     X_simple = simple_df.drop(columns = ['orders', 'total_sales']) # 2 channels: facebook and google
#     y_simple = simple_df['total_sales'] # for now lets just use total_sales and exclude orders
#     return X_simple, y_simple

# #def build_pipeline() -> Pipeline:
#     # initiate pipeline
#     # return model

# # created a "pipelines" directory in main directory
# # in "pipelines" directory, created "pipeline.pkl" file to save pickle file in
# # export fitted "model" as pickle file

# def load_model(flag="default"):
#     dirname = os.path.dirname(os.path.abspath(__file__))
#     path_load = os.path.join(dirname, "..", "pipelines")
#     if flag == "default":
#         model_path = os.path.join(path_load, "pipeline-2023-08-31.pkl")
#         model = pickle.load(open(model_path, 'rb'))

#     return model



# # if __name__ == "__main__":
# #     data_path = os.path.join(parent_dir,  data_dir, data_file)
# #     X, y = get_data(data_path)
# #     model = LinearRegression()
# #     model.fit(X, y)

#     # Pipeline pickle save

#     #pipeline_load_path = os.path.join(parent_dir,'pipelines','pipeline-2023-08-31.pkl')
#     #pipeline_save_path = os.path.join(parent_dir,'pipelines',f'pipeline-{datetime.now()}.pkl')
#     #with open(pipeline_save_path, 'wb') as file:
#     #    pickle.dump(model, file)
