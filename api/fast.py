from datetime import datetime
import pandas as pd
from fastapi import FastAPI
from taxifare.predict import load_model, predict


app = FastAPI()



@app.get("/")
def root():
    return {"message": "Hello Noé, API should works if your see this message!"}


@app.get("/predict")
def prediction(
    pickup_datetime: datetime,
    pickup_longitude: float,
    pickup_latitude: float,
    dropoff_longitude: float,
    dropoff_latitude: float,
    passenger_count: int):

    X = pd.DataFrame([{
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
    }])

    model = load_model("models/linreg_pipeline.joblib")

    y_pred = predict(model, X)

    return {"fare": y_pred[0]}
