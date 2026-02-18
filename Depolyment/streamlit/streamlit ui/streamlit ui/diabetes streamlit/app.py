import streamlit as st
import pickle
import numpy as np

# Load model

@st.cache_resource
def load_model():
    with open("diabetes_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# UI
st.title(" Diabetes Prediction App")
st.write("Enter patient details to predict diabetes risk")

st.sidebar.header("Patient Inputs")

pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 0)
glucose = st.sidebar.number_input("Glucose", 0, 250, 120)
bp = st.sidebar.number_input("Blood Pressure", 0, 150, 70)
skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
insulin = st.sidebar.number_input("Insulin", 0, 1000, 79)
bmi = st.sidebar.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.sidebar.number_input("Age", 1, 120, 33)

# Prediction
if st.button("Predict Diabetes Risk"):

    features = np.array([[
        pregnancies, glucose, bp, skin_thickness,
        insulin, bmi, dpf, age
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1] * 100

    st.subheader("Result")

    if prediction == 1:
        st.error(f" Likely Diabetic\n\nRisk Score: {probability:.1f}%")
    else:
        st.success(f" Likely Not Diabetic\n\nRisk Score: {probability:.1f}%")

    st.progress(float(probability / 100))
