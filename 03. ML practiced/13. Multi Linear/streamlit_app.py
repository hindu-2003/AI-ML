import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(page_title="Paddy Yield Predictor", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
    .metric-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.title("🌾 Paddy Yield Predictor")
st.sidebar.markdown("---")
page = st.sidebar.radio("Choose Section:", [
    "📊 Home",
    "🔍 Data Exploration",
    "🤖 Model Training",
    "📈 Model Performance",
    "🔮 Make Predictions",
    "ℹ️ About"
])

# ==================== LOAD DATA ====================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('paddydataset.csv')
        return df
    except FileNotFoundError:
        st.error("⚠️ Dataset not found. Please ensure 'paddydataset.csv' is in the same directory.")
        return None

@st.cache_resource
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    return model, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test

# Load data
df = load_data()

if df is not None:
    # Feature configuration
    features_selected = ['Urea_40Days', 'Pest_60Day(in ml)', '30_50DRain( in mm)', 'Max temp_D31_D60']
    target = 'Paddy yield(in Kg)'
    
    X = df[features_selected].copy()
    y = df[target].copy()
    
    # Train model
    model, X_train, X_test, y_train, y_test, y_pred_train, y_pred_test = train_model(X, y)
    
    # Extract coefficients once (make available to all pages)
    intercept = model.intercept_
    coefficients = model.coef_
    
    # ==================== PAGE: HOME ====================
    if page == "📊 Home":
        st.title("🌾 Multi-Linear Regression: Predicting Paddy Yield")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📖 The Story
            
            Imagine you're a rice farmer. You want to predict **how much rice you'll harvest** based on factors you control:
            
            ✓ **Fertilizer (Urea)** - How much you use  
            ✓ **Pesticide** - How much you apply  
            ✓ **Rainfall** - Water during the season  
            ✓ **Temperature** - Max temp during growth  
            
            This is **Multi-Linear Regression** - finding relationships between multiple inputs and one output.
            """)
        
        with col2:
            st.info("""
            ### 🎯 What This Model Does
            
            It learns an **equation** like:
            
            ```
            Yield = Base + (Factor₁ × Urea) 
                        + (Factor₂ × Pest)
                        + (Factor₃ × Rain)
                        + (Factor₄ × Temp)
            ```
            
            Then uses it to **predict new yields**!
            """)
        
        st.markdown("---")
        
        # Quick stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Dataset Size", f"{len(df):,} rows")
        with col2:
            st.metric("📐 Features Used", "4")
        with col3:
            st.metric("🎯 Target Variable", "Paddy Yield")
    
    # ==================== PAGE: DATA EXPLORATION ====================
    elif page == "🔍 Data Exploration":
        st.title("🔍 Data Exploration")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Sample Data (First 10 Rows)")
            st.dataframe(pd.concat([X.head(10), y.head(10)], axis=1))
        
        with col2:
            st.subheader("📈 Statistical Summary")
            summary = pd.DataFrame({
                'Min': X.min().tolist() + [y.min()],
                'Mean': X.mean().tolist() + [y.mean()],
                'Max': X.max().tolist() + [y.max()],
                'Std Dev': X.std().tolist() + [y.std()]
            }, index=features_selected + [target])
            st.dataframe(summary)
        
        st.markdown("---")
        
        # Distribution plots
        st.subheader("📊 Feature Distributions")
        
        fig, axes = plt.subplots(2, 3, figsize=(14, 8))
        fig.suptitle('Feature Distributions', fontsize=14, fontweight='bold')
        
        # Plot features
        for idx, feature in enumerate(features_selected):
            row = idx // 3
            col = idx % 3
            axes[row, col].hist(X[feature], bins=30, color='skyblue', edgecolor='black')
            axes[row, col].set_title(feature.split('(')[0])
            axes[row, col].set_ylabel('Frequency')
        
        # Plot target in the last subplot
        axes[1, 2].hist(y, bins=30, color='lightcoral', edgecolor='black')
        axes[1, 2].set_title(target)
        axes[1, 2].set_ylabel('Frequency')
        
        plt.tight_layout()
        st.pyplot(fig)
    
    # ==================== PAGE: MODEL TRAINING ====================
    elif page == "🤖 Model Training":
        st.title("🤖 Model Training & Learned Equation")
        
        st.subheader("🏠 Base Yield (Intercept)")
        st.markdown(f"### {intercept:,.2f} Kg")
        
        st.subheader("📐 Feature Coefficients (Impact Factors)")
        
        coef_df = pd.DataFrame({
            'Feature': features_selected,
            'Coefficient': coefficients,
            'Impact': ['Positive ✓' if c > 0 else 'Negative ✗' for c in coefficients]
        })
        
        st.dataframe(coef_df, width='stretch')
        
        st.markdown("---")
        
        st.subheader("📝 The Equation Our Model Learned")
        
        equation = f"**Predicted Yield = {intercept:,.2f}**"
        for feature, coef in zip(features_selected, coefficients):
            sign = "+" if coef > 0 else "−"
            equation += f"\n\n{sign} ({abs(coef):.6f} × {feature})"
        
        st.markdown(equation)
        
        st.markdown("---")
        
        st.subheader("💡 What This Means (Plain English)")
        
        for feature, coef in zip(features_selected, coefficients):
            unit = "Kg" if "Urea" in feature else ("ml" if "Pest" in feature else ("mm" if "Rain" in feature else "°C"))
            impact = "increases" if coef > 0 else "decreases"
            st.markdown(f"• **1 {unit}** more {feature.split('(')[0]} → Yield **{impact}** by **{abs(coef):.2f} Kg**")
    
    # ==================== PAGE: MODEL PERFORMANCE ====================
    elif page == "📈 Model Performance":
        st.title("📈 Model Performance")
        
        # Calculate metrics
        r2_train = r2_score(y_train, y_pred_train)
        r2_test = r2_score(y_test, y_pred_test)
        rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
        rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
        mae_train = mean_absolute_error(y_train, y_pred_train)
        mae_test = mean_absolute_error(y_test, y_pred_test)
        
        # Metrics display
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("R² Score (Test)", f"{r2_test:.4f}", f"{r2_test*100:.2f}%")
            st.caption("Explains this % of yield variation")
        
        with col2:
            st.metric("RMSE (Test)", f"{rmse_test:,.0f} Kg", "Root Mean Squared Error")
        
        with col3:
            st.metric("MAE (Test)", f"{mae_test:,.0f} Kg", "Mean Absolute Error")
        
        st.markdown("---")
        
        # Performance table
        st.subheader("📊 Detailed Metrics")
        
        metrics_df = pd.DataFrame({
            'Metric': ['R² Score', 'RMSE (Kg)', 'MAE (Kg)'],
            'Training': [f"{r2_train:.4f}", f"{rmse_train:,.2f}", f"{mae_train:,.2f}"],
            'Testing': [f"{r2_test:.4f}", f"{rmse_test:,.2f}", f"{mae_test:,.2f}"]
        })
        
        st.dataframe(metrics_df, width='stretch')
        
        st.markdown("---")
        
        # Visualizations
        st.subheader("📊 Model Visualizations")
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Multi-Linear Regression: The Proof in Plots', fontsize=14, fontweight='bold')
        
        # Plot 1: Actual vs Predicted
        ax1 = axes[0, 0]
        ax1.scatter(y_test, y_pred_test, alpha=0.6, color='dodgerblue', edgecolors='navy', s=50)
        min_val = min(y_test.min(), y_pred_test.min())
        max_val = max(y_test.max(), y_pred_test.max())
        ax1.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
        ax1.set_xlabel('Actual Yield (Kg)', fontweight='bold')
        ax1.set_ylabel('Predicted Yield (Kg)', fontweight='bold')
        ax1.set_title('Actual vs Predicted Yield')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Residuals
        ax2 = axes[0, 1]
        residuals = y_test.values - y_pred_test
        ax2.scatter(y_pred_test, residuals, alpha=0.6, color='green', edgecolors='darkgreen', s=50)
        ax2.axhline(y=0, color='r', linestyle='--', lw=2, label='Zero Error')
        ax2.set_xlabel('Predicted Yield (Kg)', fontweight='bold')
        ax2.set_ylabel('Residuals (Kg)', fontweight='bold')
        ax2.set_title('Residual Plot')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Feature Importance
        ax3 = axes[1, 0]
        colors = ['green' if x > 0 else 'red' for x in coefficients]
        ax3.barh(range(len(features_selected)), coefficients, color=colors, edgecolor='black', linewidth=1.5)
        ax3.set_yticks(range(len(features_selected)))
        ax3.set_yticklabels([f.split('(')[0] for f in features_selected], fontsize=9)
        ax3.set_xlabel('Coefficient Value', fontweight='bold')
        ax3.set_title('Feature Importance')
        ax3.axvline(x=0, color='black', linestyle='-', lw=1)
        ax3.grid(True, alpha=0.3, axis='x')
        
        # Plot 4: Error Distribution
        ax4 = axes[1, 1]
        ax4.hist(residuals, bins=30, color='purple', alpha=0.7, edgecolor='black')
        ax4.axvline(x=0, color='red', linestyle='--', lw=2, label=f'Mean Error: {residuals.mean():.2f} Kg')
        ax4.set_xlabel('Prediction Error (Kg)', fontweight='bold')
        ax4.set_ylabel('Frequency', fontweight='bold')
        ax4.set_title('Distribution of Errors')
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        st.pyplot(fig)
    
    # ==================== PAGE: MAKE PREDICTIONS ====================
    elif page == "🔮 Make Predictions":
        st.title("🔮 Make Predictions")
        
        st.subheader("Enter Values for Your Scenario")
        
        col1, col2 = st.columns(2)
        
        with col1:
            urea = st.number_input(
                "🌾 Urea (in Kg)",
                min_value=0.0,
                max_value=300.0,
                value=162.78,
                step=1.0
            )
            rain = st.number_input(
                "💧 Rainfall (in mm)",
                min_value=0.0,
                max_value=500.0,
                value=187.2,
                step=1.0
            )
        
        with col2:
            pest = st.number_input(
                "🦗 Pesticide (in ml)",
                min_value=0.0,
                max_value=5000.0,
                value=3600.0,
                step=100.0
            )
            temp = st.number_input(
                "🌡️ Max Temperature (in °C)",
                min_value=15.0,
                max_value=50.0,
                value=30.0,
                step=0.5
            )
        
        st.markdown("---")
        
        # Make prediction
        input_data = np.array([[urea, pest, rain, temp]])
        prediction = model.predict(input_data)[0]
        
        # Display result
        st.subheader("📊 Prediction Result")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.info(f"""
            ### Predicted Yield
            ## {prediction:,.2f} Kg
            """)
        
        with col2:
            st.markdown("### Your Inputs")
            input_display = pd.DataFrame({
                'Parameter': ['Urea', 'Pesticide', 'Rainfall', 'Max Temp'],
                'Value': [f"{urea:.2f} Kg", f"{pest:.0f} ml", f"{rain:.2f} mm", f"{temp:.2f}°C"]
            })
            st.dataframe(input_display, width='stretch', hide_index=True)
        
        st.markdown("---")
        
        # Show calculation
        st.subheader("🧮 How We Got This Number")
        
        intercept = model.intercept_
        coefficients = model.coef_
        
        calculation = f"""
        **The Equation:**
        ```
        Yield = {intercept:,.2f} + ({coefficients[0]:.6f} × {urea})
                               + ({coefficients[1]:.6f} × {pest})
                               + ({coefficients[2]:.6f} × {rain})
                               + ({coefficients[3]:.6f} × {temp})
        ```
        
        **Breaking it Down:**
        - Base yield: **{intercept:,.2f} Kg**
        - From Urea: **{coefficients[0] * urea:,.2f} Kg**
        - From Pesticide: **{coefficients[1] * pest:,.2f} Kg**
        - From Rainfall: **{coefficients[2] * rain:,.2f} Kg**
        - From Temperature: **{coefficients[3] * temp:,.2f} Kg**
        
        **Total: {prediction:,.2f} Kg**
        """
        
        st.markdown(calculation)
        
        st.markdown("---")
        
        # Preset scenarios
        st.subheader("📋 Quick Scenarios")
        
        scenarios = {
            "🟢 Optimal Conditions": (162.78, 3600, 187.2, 30),
            "🟡 Moderate Input": (100, 2000, 250, 28),
            "🔴 High Input": (200, 4500, 150, 35),
            "⚪ Minimal Intervention": (80, 1000, 100, 25),
        }
        
        scenario_col1, scenario_col2 = st.columns(2)
        
        col_idx = 0
        for scenario_name, (u, p, r, t) in scenarios.items():
            col = scenario_col1 if col_idx < 2 else scenario_col2
            
            with col:
                if st.button(f"Use {scenario_name}", key=f"scenario_{scenario_name}", use_container_width=True):
                    st.session_state.urea = u
                    st.session_state.pest = p
                    st.session_state.rain = r
                    st.session_state.temp = t
            
            col_idx += 1
    
    # ==================== PAGE: ABOUT ====================
    elif page == "ℹ️ About":
        st.title("ℹ️ About This Application")
        
        st.markdown("""
        ### 🌾 Multi-Linear Regression: Predicting Paddy Yield
        
        This application demonstrates **Multi-Linear Regression** in action using a real paddy yield dataset.
        
        #### 📊 What is Multi-Linear Regression?
        
        Multi-Linear Regression is a statistical method that models the relationship between:
        - **One output variable** (Paddy Yield)
        - **Multiple input variables** (Urea, Pesticide, Rainfall, Temperature)
        
        The model learns an equation that best predicts the output based on the inputs.
        
        #### 📈 How It Works
        
        1. **Data Collection**: Gather historical data with multiple features and outcomes
        2. **Training**: The algorithm finds the best coefficients for each feature
        3. **Prediction**: Use the learned equation to predict new outcomes
        4. **Evaluation**: Measure how well the model predicts using metrics like R², RMSE, MAE
        
        #### 🎯 Real-World Applications
        
        - 🌾 **Agriculture**: Crop yield prediction
        - 💰 **Finance**: Stock price prediction
        - 🏥 **Healthcare**: Patient outcomes
        - 🏘️ **Real Estate**: House price prediction
        - 🚗 **Automotive**: Car price estimation
        
        #### 📚 Dataset Information
        
        - **Total Records**: 2,791 rows
        - **Features**: 4 (Urea, Pesticide, Rainfall, Max Temperature)
        - **Target**: Paddy Yield (in Kg)
        - **Data Split**: 80% training, 20% testing
        
        #### 💻 Technology Stack
        
        - **Python**: Programming language
        - **Pandas**: Data manipulation
        - **Scikit-learn**: Machine learning
        - **Matplotlib**: Visualization
        - **Streamlit**: Interactive web interface
        
        ---
        
        **Created with ❤️ for Learning Machine Learning**
        """)

else:
    st.error("Could not load data. Please ensure the dataset is available.")
