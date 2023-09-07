from fastapi import FastAPI
import pandas as pd
import numpy as np
from mmmproject.model.params import *
## from mmmproject.model.registry import load_model
from mmmproject.model.lp_model import find_optimal_budget
import datetime as datetime
from mmmproject.model.weekendclass import AddWeekendsTransformer
from mmmproject.model.registry import minmax_fb, minmax_gg, minmax_tt
app = FastAPI()
# app.state.model = load_model(flag="default")

# Define a root `/` endpoint -> standard endpoint for checking if API is working.
@app.get("/")
def index():
    return {'API working': True}


# /salepredict endpoint we want to use in streamlit to predict total sales
# Example url (local) to predict -> http://127.0.0.1:8000/salepredict?facebook=257.01&google=1.17&tiktok=0
@app.get("/salepredict")
def query_sale_predict(date: str, facebook: float, google: float, tiktok: float):

    """
    Returns predicted sales data from "df" according input data
    """

    # creating 1 row data as input, X_pred
    dict_feat = {
        "google": google,
        "facebook": facebook,
        "tiktok": tiktok
    }

    X_pred = pd.DataFrame(dict_feat, index=[date])

    # predicting sales
    y_pred = app.state.model.predict(X_pred)

    return {"predicted_sale": y_pred[0]}

@app.get("/budgetdivider")
def query_budget_divider(TOTAL_DAILY_BUDGET: float, Date: str):
    """
    Returns amount of different advertisements according to input data
    """
    optimal_solution=find_optimal_budget(TOTAL_DAILY_BUDGET, Date)
    return {'Status':optimal_solution[0], 'Total_clicks':optimal_solution[1], 'Google Budget': optimal_solution[2] ,'Facebook Budget':optimal_solution[3],'Tiktok Budget':optimal_solution[4]}



@app.get("/clickpredict")
def newfun(date: str, facebook: float, google: float, tiktok: float):
    '''
    function
    '''
    b = np.array([133.12031243, -69.17339136, 1236.51148254, 280, 1782.03178883])
    date = pd.to_datetime(date)
    weekend_date = int((date.day_of_week==4) | (date.day_of_week==5))

    X = np.array([weekend_date, minmax_fb(facebook), minmax_gg(google), minmax_tt(tiktok)])

    res = b[0] + np.dot(X, b[1:])

    return res  

if __name__ == '__main__':
    print(query_sale_predict(date='2021-07-01', facebook=600.0, google=45.0, tiktok=0.0))
