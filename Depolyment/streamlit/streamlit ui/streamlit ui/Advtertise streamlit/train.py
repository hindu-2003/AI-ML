import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------
# Load data
# -------------------------
data = pd.read_csv("advertising.csv")

X = data[["TV", "radio", "newspaper"]]
y = data["sales"]

# -------------------------
# Split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -------------------------
# Pipeline = scaler + model
# -------------------------
model = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

# -------------------------
# Train
# -------------------------
model.fit(X_train, y_train)

# -------------------------
# Evaluate
# -------------------------
pred = model.predict(X_test)

print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
print("R2:", r2_score(y_test, pred))

# -------------------------
# Save ONE PKL
# -------------------------
with open("advertising_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Saved advertising_model.pkl")
