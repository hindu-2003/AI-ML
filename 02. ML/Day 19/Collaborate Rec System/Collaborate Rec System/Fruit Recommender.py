# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

# --- Load the data ---
@st.cache_data
def load_data():
    df = pd.read_csv('fruit_ratings.csv')
    X = df.pivot(index='User', columns='Fruit', values='Rating')
    X_filled = X.fillna(X.median())
    return df, X_filled

fruit_ratings, X = load_data()

# --- Fit SVD ---
@st.cache_data
def train_svd(X, n_components=2):
    svd = TruncatedSVD(n_components=n_components)
    svd.fit(X)
    U = svd.transform(X)
    VT = svd.components_
    return svd, U, VT

svd, U, VT = train_svd(X)

# --- Streamlit UI ---
st.title("🍎 Fruit Recommender System")
st.write("Select the fruits you have rated:")

fruits = X.columns.tolist()
user_ratings = []

for fruit in fruits:
    rating = st.slider(f"{fruit}", 0, 5, 0)
    user_ratings.append(rating if rating != 0 else np.nan)

# Button to get recommendations
if st.button("Get Recommendations"):
    new_user = np.array(user_ratings).reshape(1, -1)
    new_user_filled = pd.DataFrame(new_user, columns=X.columns).fillna(X.median())
    
    # Transform into latent space and predict
    new_user_2d = svd.transform(new_user_filled)
    predicted_ratings = np.dot(new_user_2d, VT)
    
    recs = pd.DataFrame(predicted_ratings, columns=X.columns).T
    recs.columns = ['Predicted Rating']
    
    # Remove already rated fruits
    already_rated = [fruits[i] for i, r in enumerate(user_ratings) if not np.isnan(r)]
    top_recs = recs[~recs.index.isin(already_rated)].sort_values('Predicted Rating', ascending=False)
    
    st.write("### Recommended Fruits for You:")
    st.table(top_recs)
