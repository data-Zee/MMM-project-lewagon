import pandas as pd
from mamimo.carryover import ExponentialCarryover
from mamimo.saturation import ExponentialSaturation
from mamimo.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os
import pickle
from datetime import datetime

def get_data(csv_path: str):
    # accessing raw_data.csv with os library
    # reading df
    df = pd.read_csv(csv_path)
    df = df.drop(columns='Unnamed: 0')
    df['Day'] = pd.to_datetime(df['Day'])
    df.set_index('Day', inplace=True)
    df = df.rename(columns={"fb_costs": "facebook", "google_costs": "google", "tt_costs": "tiktok"})

    # create a simple_df
    simple_df = df.drop(columns = ['fb_impressions', 'fb_clicks', 'google_impressions', 'google_clicks', 'tt_impressions', 'tt_clicks'])
    X_simple = simple_df.drop(columns = ['orders', 'total_sales']) # 2 channels: facebook and google
    y_simple = simple_df['total_sales'] # for now lets just use total_sales and exclude orders
    return X_simple, y_simple

def build_pipeline() -> Pipeline:
    # initiate pipeline
    adstock = ColumnTransformer(
        [
        ('facebook_pipe', Pipeline([
                ('carryover', ExponentialCarryover()),
                ('saturation', ExponentialSaturation())
        ]), ['facebook']),
        ('google_pipe', Pipeline([
                ('carryover', ExponentialCarryover()),
                ('saturation', ExponentialSaturation())
        ]), ['google']),
        ('tiktok_pipe', Pipeline([
                ('carryover', ExponentialCarryover()),
                ('saturation', ExponentialSaturation())
        ]), ['tiktok'])
    ])

    # initiate model
    model = Pipeline([
        ('adstock', adstock),
        ('regression', LinearRegression(positive=True))
    ])
    return model

# created a "pipelines" directory in "api" directory
# created "pipeline.pkl" file to save pickle file in
# export fitted "model" as pickle file
if __name__ == "__main__":
    cwd = os.getcwd()
    parent_dir = cwd
    data_dir = 'raw_data'
    data_file = 'df_clean.csv'
    data_path = os.path.join(parent_dir, '../..', data_dir, data_file)
    X, y = get_data(data_path)
    model = build_pipeline()
    # fitting model to create (test) pickle file
    model.fit(X, y)
    pipeline_path = os.path.join(parent_dir, '../..', f'pipelines/pipeline-{datetime.now()}.pkl')
    with open(pipeline_path, 'wb') as file:
        pickle.dump(model, file)
