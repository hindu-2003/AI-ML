import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Advertising Sales Prediction")

st.title("📈 Advertising Sales Prediction")

# -------------------------
# Load pipeline model
# -------------------------
@st.cache_resource
def load_model():
    with open("advertising_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# -------------------------
# Inputs
# -------------------------
tv = st.number_input("TV Budget", 0.0, 300.0, 100.0)
radio = st.number_input("Radio Budget", 0.0, 100.0, 25.0)
news = st.number_input("Newspaper Budget", 0.0, 120.0, 10.0)

# -------------------------
# Predict
# -------------------------
if st.button("Predict Sales"):

    input_df = pd.DataFrame(
        [[tv, radio, news]],
        columns=["TV", "radio", "newspaper"]
    )

    pred = model.predict(input_df)[0]

    st.success(f"📢 Predicted Sales: {pred:.2f}")
