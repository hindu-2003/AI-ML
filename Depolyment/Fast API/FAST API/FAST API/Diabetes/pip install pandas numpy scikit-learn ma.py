pip install pandas numpy scikit-learn matplotlib seaborn xgboost
pip install geopy
import pandas as pd

data = pd.read_csv("data/train.csv", nrows=100000)
print(data.head())
print(data.info())
data = data[data['fare_amount'] > 0]
data = data[data['passenger_count'] > 0]
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])

data['hour'] = data['pickup_datetime'].dt.hour
data['day'] = data['pickup_datetime'].dt.day
data['month'] = data['pickup_datetime'].dt.month
data['weekday'] = data['pickup_datetime'].dt.weekday
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat/2)**2 + np.cos(np.radians(lat1)) * \
        np.cos(np.radians(lat2)) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

data['distance_km'] = haversine(
    data['pickup_latitude'],
    data['pickup_longitude'],
    data['dropoff_latitude'],
    data['dropoff_longitude']
)
features = [
    'passenger_count',
    'hour',
    'weekday',
    'distance_km'
]

X = data[features]
y = data['fare_amount']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)
from xgboost import XGBRegressor
model = XGBRegressor()
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))
import pickle
pickle.dump(model, open("model.pkl", "wb"))
@app.route("/predict", methods=["POST"])