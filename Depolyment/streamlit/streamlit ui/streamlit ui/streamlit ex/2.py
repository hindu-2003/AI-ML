import streamlit as st

st.header("Add Two Numbers")

num1 = st.number_input("Enter first number", 0)
num2 = st.number_input("Enter second number", 0)

if st.button("Calculate"):
    st.write("Result:", num1 + num2)
