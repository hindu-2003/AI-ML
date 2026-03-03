"""
🌾 FastAPI Backend for Paddy Yield Prediction
REST API for Multi-Linear Regression Model
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# ==================== INITIALIZATION ====================

app = FastAPI(
    title="🌾 Paddy Yield Predictor API",
    description="REST API for Multi-Linear Regression Model - Predict paddy yield based on farming inputs",
    version="1.0.0"
)

# Enable CORS (for frontend apps to access this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== GLOBAL VARIABLES ====================

model = None
features_selected = ['Urea_40Days', 'Pest_60Day(in ml)', '30_50DRain( in mm)', 'Max temp_D31_D60']
target = 'Paddy yield(in Kg)'
intercept = None
coefficients = None

# ==================== DATA MODELS ====================

class PredictionInput(BaseModel):
    """Input model for prediction"""
    urea: float = 162.78  # Urea in Kg
    pesticide: float = 3600.0  # Pesticide in ml
    rainfall: float = 187.2  # Rainfall in mm
    temperature: float = 30.0  # Max temperature in °C
    
    class Config:
        example = {
            "urea": 162.78,
            "pesticide": 3600,
            "rainfall": 187.2,
            "temperature": 30
        }

class PredictionOutput(BaseModel):
    """Output model for prediction"""
    predicted_yield_kg: float
    input_values: dict
    equation: str

class ModelInfo(BaseModel):
    """Model information"""
    intercept: float
    coefficients: dict
    equation: str

class BatchPredictionInput(BaseModel):
    """Input for batch predictions"""
    predictions: list[PredictionInput]

# ==================== HELPER FUNCTIONS ====================

def load_and_train_model():
    """Load data and train the model"""
    global model, intercept, coefficients
    
    try:
        # Load data
        df = pd.read_csv('paddydataset.csv')
        
        # Prepare data
        X = df[features_selected].copy()
        y = df[target].copy()
        
        # Split and train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Extract coefficients
        intercept = model.intercept_
        coefficients = model.coef_
        
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

def make_prediction(urea: float, pesticide: float, rainfall: float, temperature: float) -> float:
    """Make prediction using the model"""
    if model is None:
        raise ValueError("Model not trained")
    
    input_data = np.array([[urea, pesticide, rainfall, temperature]])
    prediction = model.predict(input_data)[0]
    
    return prediction

def generate_equation_string() -> str:
    """Generate human-readable equation"""
    if intercept is None or coefficients is None:
        return "Model not available"
    
    equation = f"Yield = {intercept:,.2f}"
    for feature, coef in zip(features_selected, coefficients):
        sign = "+" if coef > 0 else "−"
        equation += f"\n       {sign} {abs(coef):.6f} × {feature}"
    
    return equation

# ==================== STARTUP EVENT ====================

@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    print("🌾 Loading Paddy Yield Prediction Model...")
    if load_and_train_model():
        print("✅ Model loaded successfully!")
    else:
        print("❌ Error loading model!")

# ==================== ROOT ENDPOINT ====================

@app.get("/", tags=["Info"])
async def root():
    """Welcome endpoint"""
    return {
        "message": "🌾 Welcome to Paddy Yield Predictor API",
        "version": "1.0.0",
        "endpoints": {
            "predict": "/predict (POST) - Make single prediction",
            "batch_predict": "/batch_predict (POST) - Make multiple predictions",
            "model_info": "/model_info (GET) - Get model information",
            "health": "/health (GET) - Check API health"
        }
    }

# ==================== HEALTH CHECK ====================

@app.get("/health", tags=["Info"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "✅ healthy",
        "model_loaded": model is not None
    }

# ==================== MODEL INFO ENDPOINT ====================

@app.get("/model_info", response_model=ModelInfo, tags=["Model"])
async def get_model_info():
    """Get model coefficients and equation"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    coef_dict = {
        features_selected[i]: float(coefficients[i]) 
        for i in range(len(features_selected))
    }
    
    return ModelInfo(
        intercept=float(intercept),
        coefficients=coef_dict,
        equation=generate_equation_string()
    )

# ==================== SINGLE PREDICTION ENDPOINT ====================

@app.post("/predict", response_model=PredictionOutput, tags=["Predictions"])
async def predict(input_data: PredictionInput):
    """
    Make a single yield prediction
    
    **Input:**
    - `urea`: Urea used (in Kg)
    - `pesticide`: Pesticide applied (in ml)
    - `rainfall`: Rainfall received (in mm)
    - `temperature`: Maximum temperature (in °C)
    
    **Output:**
    - `predicted_yield_kg`: Predicted paddy yield in kilograms
    - `input_values`: The values you provided
    - `equation`: The equation used for prediction
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Make prediction
        prediction = make_prediction(
            input_data.urea,
            input_data.pesticide,
            input_data.rainfall,
            input_data.temperature
        )
        
        return PredictionOutput(
            predicted_yield_kg=float(prediction),
            input_values={
                "urea_kg": input_data.urea,
                "pesticide_ml": input_data.pesticide,
                "rainfall_mm": input_data.rainfall,
                "temperature_celsius": input_data.temperature
            },
            equation=generate_equation_string()
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== BATCH PREDICTION ENDPOINT ====================

@app.post("/batch_predict", tags=["Predictions"])
async def batch_predict(batch_data: BatchPredictionInput):
    """
    Make multiple yield predictions at once
    
    **Input:** List of prediction inputs
    
    **Output:** List of predictions
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        results = []
        
        for i, input_data in enumerate(batch_data.predictions):
            prediction = make_prediction(
                input_data.urea,
                input_data.pesticide,
                input_data.rainfall,
                input_data.temperature
            )
            
            results.append({
                "id": i + 1,
                "predicted_yield_kg": float(prediction),
                "input_values": {
                    "urea_kg": input_data.urea,
                    "pesticide_ml": input_data.pesticide,
                    "rainfall_mm": input_data.rainfall,
                    "temperature_celsius": input_data.temperature
                }
            })
        
        return {
            "total_predictions": len(results),
            "predictions": results
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ==================== SCENARIO ENDPOINTS ====================

@app.get("/scenarios/{scenario_name}", tags=["Scenarios"])
async def get_scenario_prediction(scenario_name: str):
    """
    Get prediction for predefined scenarios
    
    Available scenarios:
    - optimal
    - moderate
    - high_input
    - minimal
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    scenarios = {
        "optimal": {
            "name": "Optimal Conditions",
            "urea": 162.78,
            "pesticide": 3600,
            "rainfall": 187.2,
            "temperature": 30,
        },
        "moderate": {
            "name": "Moderate Input",
            "urea": 100,
            "pesticide": 2000,
            "rainfall": 250,
            "temperature": 28,
        },
        "high_input": {
            "name": "High Input, High Temperature",
            "urea": 200,
            "pesticide": 4500,
            "rainfall": 150,
            "temperature": 35,
        },
        "minimal": {
            "name": "Minimal Intervention",
            "urea": 80,
            "pesticide": 1000,
            "rainfall": 100,
            "temperature": 25,
        }
    }
    
    if scenario_name.lower() not in scenarios:
        raise HTTPException(
            status_code=404, 
            detail=f"Scenario not found. Available: {list(scenarios.keys())}"
        )
    
    scenario = scenarios[scenario_name.lower()]
    prediction = make_prediction(
        scenario["urea"],
        scenario["pesticide"],
        scenario["rainfall"],
        scenario["temperature"]
    )
    
    return {
        "scenario": scenario["name"],
        "predicted_yield_kg": float(prediction),
        "farming_inputs": {
            "urea_kg": scenario["urea"],
            "pesticide_ml": scenario["pesticide"],
            "rainfall_mm": scenario["rainfall"],
            "temperature_celsius": scenario["temperature"]
        }
    }

# ==================== STATISTICS ENDPOINT ====================

@app.get("/statistics", tags=["Info"])
async def get_statistics():
    """Get model performance statistics"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Load data for statistics
        df = pd.read_csv('paddydataset.csv')
        X = df[features_selected].copy()
        y = df[target].copy()
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
        
        r2_test = r2_score(y_test, y_pred_test)
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
        mae_test = mean_absolute_error(y_test, y_pred_test)
        
        return {
            "dataset_size": len(df),
            "training_samples": len(X_train),
            "testing_samples": len(X_test),
            "features": features_selected,
            "performance": {
                "r2_score": float(r2_test),
                "r2_percentage": float(r2_test * 100),
                "rmse_kg": float(rmse_test),
                "mae_kg": float(mae_test),
                "interpretation": f"Model explains {r2_test*100:.2f}% of yield variation"
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==================== RUN COMMAND ====================

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting FastAPI server...")
    print("📍 API will be available at: http://localhost:8000")
    print("📚 API Documentation at: http://localhost:8000/docs")
    print("📋 Alternative docs at: http://localhost:8000/redoc")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
