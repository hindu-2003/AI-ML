import gradio as gr
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Model training code
def simple_prediction_model(data_path='advertising.csv'):
    data = pd.read_csv(data_path)
    X = data[['TV', 'radio', 'newspaper']]
    y = data['sales']
    model = LinearRegression()
    model.fit(X, y)
    
    def predict_sales(tv, radio, newspaper):
        new_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'radio', 'newspaper'])
        prediction = model.predict(new_data)
        return round(prediction[0], 2)
    
    return predict_sales

# Load model
predict_sales = simple_prediction_model()

# Gradio Interface
interface = gr.Interface(
    fn=predict_sales,
    inputs=[
        gr.Slider(0, 300, value=100, label="TV Budget"),
        gr.Slider(0, 100, value=30, label="Radio Budget"),
        gr.Slider(0, 100, value=20, label="Newspaper Budget"),
    ],
    outputs="number",
    title="Advertising Budget Sales Predictor",
    description="Adjust the sliders to input your advertising budget and predict expected sales."
)

# Launch the app
interface.launch()
