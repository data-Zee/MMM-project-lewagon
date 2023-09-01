from fastapi import FastAPI
import pandas as pd
from mmmproject.model.registry import load_model
import datetime as datetime

app = FastAPI()
app.state.model = load_model(flag="default")


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



if __name__ == '__main__':
    print(query_sale_predict(date='2021-07-01', facebook=600.0, google=45.0, tiktok=0.0))
