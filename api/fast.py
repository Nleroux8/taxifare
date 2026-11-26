from datetime import datetime

from fastapi import FastAPI

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


    return {"pickup_datetime":pickup_datetime}
