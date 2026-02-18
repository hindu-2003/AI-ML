import streamlit as st
import pandas as pd

st.title("CSV Actions App")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    
    st.subheader("📌 Data Preview")
    st.dataframe(df)

    st.subheader("🔍 Basic Info")
    st.write("Shape (rows, columns):", df.shape)
    st.write("Columns:", list(df.columns))

    st.subheader("📊 Describe Statistics")
    st.write(df.describe())

    st.subheader("🔎 Filter Data")
    column = st.selectbox("Select column to filter", df.columns)
    unique_vals = df[column].unique()
    selected_val = st.selectbox(f"Select value from '{column}'", unique_vals)
    
    filtered_df = df[df[column] == selected_val]
    st.write("Filtered Data:")
    st.dataframe(filtered_df)

    st.subheader("📈 Quick Chart")
    numeric_cols = df.select_dtypes(include=['int','float']).columns
    if len(numeric_cols) > 0:
        chart_col = st.selectbox("Pick column for line chart", numeric_cols)
        st.line_chart(df[chart_col])
    else:
        st.warning("⚠ No numeric columns available for chart")
