import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("decision_tree_model.pkl","rb"))

st.title("Paddy Yield Prediction 🌾")

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
rainfall = st.number_input("Rainfall")
soil = st.number_input("Soil Type")
fertilizer = st.number_input("Fertilizer")
ph = st.number_input("Soil pH")
area = st.number_input("Area")

if st.button("Predict"):

    input_data = np.array([[temperature, humidity, rainfall,
                            soil, fertilizer, ph, area]])

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")