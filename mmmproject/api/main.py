from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from mmmproject.model.df_model import *
import json

app = FastAPI()

# class Day(BaseModel):
#     sales: float
#     fb_cost: float
#     google_cost: float
#     tt_cost: float
#     variable_1: int
#     variable_2: int

# df = {
#     0: Day(sales=20, fb_cost=1000, google_cost=800, tt_cost=500, variable_1=0, variable_2=1),
#     1: Day(sales=50, fb_cost=500, google_cost=600, tt_cost=300, variable_1=1, variable_2=1)
# }

# Define a root `/` endpoint -> standard endpoint for checking if API is working.
# in terminal launch local host with command uvicorn + file:variable --reload = "uvicorn main:app --reload"
# might need "pip install uvicorn"
# open local host in browser, with "/docs" behind it you can check if API is working, should return below return result.
@app.get("/")
def index():
    return {'API working': True}

# @app.get("/df/{day_sales}")
# def query_day_sales(day_sales: int) -> Day:
#     if day_sales not in df:
#         raise HTTPException(
#             status_code=404, detail=f"{day_sales} does not exist"
#         )
#     return df[day_sales]

# prediction endpoint we want to use in streamlit
@app.get("/salepredict")
def query_sale_predict(Day):
    """
    dd
    Return sales data from "simple_df" of given input Day.
    """
    pipeline_loaded = pickle.load(open('../pipelines/pipeline-2023-08-30 16:08:45.140758.pkl', 'rb'))
    return pipeline_loaded.score(X, y)

# @app.get("/predict")
# def predict(
#     # compute 'fare_amount' from:
#         pickup_datetime: str,  # 2013-07-06 17:18:00
#         pickup_longitude: float,    # -73.950655
#         pickup_latitude: float,     # 40.783282
#         dropoff_longitude: float,   # -73.984365
#         dropoff_latitude: float,    # 40.769802
#         passenger_count: int
#     ):      # 1
#     """
#     Make a single course prediction.
#     Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
#     Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
#     """
#     model = app.state.model
#     X_pred = pd.DataFrame(dict(
#         pickup_datetime=[pd.Timestamp("2013-07-06 17:18:00", tz='UTC')],
#         pickup_longitude=[-73.950655],
#         pickup_latitude=[40.783282],
#         dropoff_longitude=[-73.950655],
#         dropoff_latitude=[	40.783282],
#         passenger_count=[2],
#     ))
#
#     X_pred = preprocess_features(X_pred)
#     prediction = model.predict(X_pred)
#     return {'fare_amount': float(prediction)}
