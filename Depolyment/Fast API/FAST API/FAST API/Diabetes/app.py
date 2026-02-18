from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import sklearn



# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("diabetes_pipeline.pkl")  # use joblib for speed & safety

# ===============================
# FASTAPI INIT
# ===============================
app = FastAPI(
    title="Diabetes Prediction API",
    description="Predict Diabetes using GaussianNB + StandardScaler",
    version="1.0"
)

# ===============================
# INPUT SCHEMA
# ===============================
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# ===============================
# PREDICTION ENDPOINT
# ===============================
@app.post("/predict")
def predict(data: DiabetesInput):
    # Convert input to numpy array
    input_array = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    # Make prediction
    prediction = model.predict(input_array)[0]

    return {
        "prediction": int(prediction),
        "result": "Diabetic" if prediction == 1 else "Not Diabetic"
    }
