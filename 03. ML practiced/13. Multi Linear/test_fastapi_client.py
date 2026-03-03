"""
🌾 FastAPI Client Examples - Test Your API
"""

import requests
import json

# ==================== CONFIGURATION ====================

API_URL = "http://localhost:8000"

# ==================== HELPER FUNCTIONS ====================

def print_response(response, title):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"✅ {title}")
    print(f"{'='*60}")
    print(json.dumps(response.json(), indent=2))
    print(f"{'='*60}\n")

# ==================== EXAMPLES ====================

def test_health():
    """Test health endpoint"""
    print("🏥 Testing Health Check...")
    response = requests.get(f"{API_URL}/health")
    print_response(response, "Health Status")

def test_model_info():
    """Get model information"""
    print("📊 Fetching Model Information...")
    response = requests.get(f"{API_URL}/model_info")
    print_response(response, "Model Information")

def test_single_prediction():
    """Make a single prediction"""
    print("🔮 Making Single Prediction...")
    
    data = {
        "urea": 162.78,
        "pesticide": 3600,
        "rainfall": 187.2,
        "temperature": 30
    }
    
    response = requests.post(f"{API_URL}/predict", json=data)
    print_response(response, "Single Prediction")

def test_batch_prediction():
    """Make batch predictions"""
    print("📦 Making Batch Predictions...")
    
    data = {
        "predictions": [
            {"urea": 162.78, "pesticide": 3600, "rainfall": 187.2, "temperature": 30},
            {"urea": 100, "pesticide": 2000, "rainfall": 250, "temperature": 28},
            {"urea": 200, "pesticide": 4500, "rainfall": 150, "temperature": 35},
            {"urea": 80, "pesticide": 1000, "rainfall": 100, "temperature": 25}
        ]
    }
    
    response = requests.post(f"{API_URL}/batch_predict", json=data)
    print_response(response, "Batch Predictions")

def test_scenarios():
    """Test predefined scenarios"""
    print("🌾 Testing Predefined Scenarios...")
    
    scenarios = ["optimal", "moderate", "high_input", "minimal"]
    
    for scenario in scenarios:
        response = requests.get(f"{API_URL}/scenarios/{scenario}")
        print_response(response, f"Scenario: {scenario.upper()}")

def test_statistics():
    """Get model statistics"""
    print("📈 Fetching Model Statistics...")
    response = requests.get(f"{API_URL}/statistics")
    print_response(response, "Model Statistics")

# ==================== CURL EXAMPLES ====================

def show_curl_examples():
    """Show cURL command examples"""
    
    print("\n" + "="*70)
    print("🔧 CURL COMMAND EXAMPLES (Copy & Paste)")
    print("="*70)
    
    print("""
1️⃣  HEALTH CHECK:
curl -X GET "http://localhost:8000/health"

2️⃣  GET MODEL INFO:
curl -X GET "http://localhost:8000/model_info"

3️⃣  SINGLE PREDICTION:
curl -X POST "http://localhost:8000/predict" \\
  -H "Content-Type: application/json" \\
  -d '{"urea": 162.78, "pesticide": 3600, "rainfall": 187.2, "temperature": 30}'

4️⃣  BATCH PREDICTIONS:
curl -X POST "http://localhost:8000/batch_predict" \\
  -H "Content-Type: application/json" \\
  -d '{
    "predictions": [
      {"urea": 162.78, "pesticide": 3600, "rainfall": 187.2, "temperature": 30},
      {"urea": 100, "pesticide": 2000, "rainfall": 250, "temperature": 28}
    ]
  }'

5️⃣  GET SCENARIO:
curl -X GET "http://localhost:8000/scenarios/optimal"

6️⃣  GET STATISTICS:
curl -X GET "http://localhost:8000/statistics"
    """)
    print("="*70 + "\n")

# ==================== JAVASCRIPT EXAMPLES ====================

def show_javascript_examples():
    """Show JavaScript/Node.js examples"""
    
    print("\n" + "="*70)
    print("📱 JAVASCRIPT/NODE.JS EXAMPLES")
    print("="*70)
    
    js_code = """
// 1. Single Prediction
async function predict() {
    const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            urea: 162.78,
            pesticide: 3600,
            rainfall: 187.2,
            temperature: 30
        })
    });
    
    const result = await response.json();
    console.log('Predicted Yield:', result.predicted_yield_kg, 'Kg');
}

// 2. Batch Predictions
async function batchPredict() {
    const response = await fetch('http://localhost:8000/batch_predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            predictions: [
                {urea: 162.78, pesticide: 3600, rainfall: 187.2, temperature: 30},
                {urea: 100, pesticide: 2000, rainfall: 250, temperature: 28}
            ]
        })
    });
    
    const results = await response.json();
    console.log('Predictions:', results);
}

// 3. Get Model Info
async function getModelInfo() {
    const response = await fetch('http://localhost:8000/model_info');
    const info = await response.json();
    console.log('Model Equation:', info.equation);
}

// Call the function
predict().catch(console.error);
    """
    
    print(js_code)
    print("="*70 + "\n")

# ==================== MAIN ====================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🌾 Paddy Yield Predictor - FastAPI Client Test")
    print("="*70)
    
    print("\n⚠️  Make sure FastAPI server is running:")
    print("   python fastapi_app.py")
    print("\n")
    
    try:
        # Run all tests
        test_health()
        test_model_info()
        test_single_prediction()
        test_batch_prediction()
        test_scenarios()
        test_statistics()
        
        # Show examples
        show_curl_examples()
        show_javascript_examples()
        
        print("✅ All tests completed successfully!")
        print("\n📚 API Documentation: http://localhost:8000/docs")
        print("🎯 Try interactive endpoints at the link above!\n")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        print("⚠️  Make sure FastAPI server is running:")
        print("   python fastapi_app.py")
        print("\nThen run this script again!")
    except Exception as e:
        print(f"❌ Error: {e}")
