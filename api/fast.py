from fastapi import FastAPI

app = FastAPI()

app.state.model = load_model()

url = 'http://localhost:8000/'

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}

@app.get("/predict")
def predict(
    # compute 'fare_amount' from:
        pickup_datetime: str,  # 2013-07-06 17:18:00
        pickup_longitude: float,    # -73.950655
        pickup_latitude: float,     # 40.783282
        dropoff_longitude: float,   # -73.984365
        dropoff_latitude: float,    # 40.769802
        passenger_count: int
    ):      # 1
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """
    model = app.state.model
    X_pred = pd.DataFrame(dict(
        pickup_datetime=[pd.Timestamp("2013-07-06 17:18:00", tz='UTC')],
        pickup_longitude=[-73.950655],
        pickup_latitude=[40.783282],
        dropoff_longitude=[-73.950655],
        dropoff_latitude=[	40.783282],
        passenger_count=[2],
    ))

    X_pred = preprocess_features(X_pred)
    prediction = model.predict(X_pred)
    return {'fare_amount': float(prediction)}
