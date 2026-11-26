import joblib
import pandas as pd

def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    trained_model = joblib.load(model_path)
    return trained_model

def predict(model, data):
    """Make predictions using the loaded model and input data."""
    prediction = model.predict(data)
    return prediction


if __name__ == "__main__":
    X_dummy = pd.DataFrame([{
          'pickup_datetime': '2013-07-06 17:18:00 UTC',
          'pickup_longitude': -73.950655,
          'pickup_latitude': 40.783282,
          'dropoff_longitude': -73.984365,
          'dropoff_latitude': 40.769802,
          'passenger_count': 1
    }])

    model = load_model("models/linreg_pipeline.joblib")

    print(predict(model, X_dummy))
