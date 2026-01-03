import streamlit as st
from predict_model import predict_sales
import pandas as pd

# Title
st.title("📊 Sales Prediction App")

# User Inputs
month = st.selectbox("Select Month", ["Jan","Feb","Mar","Apr","May"])
product = st.selectbox("Select Product", ["Mobile","Laptop"])
region = st.selectbox("Select Region", ["Pune","Mumbai"])

# Predict button
if st.button("Predict Sales"):
    prediction = predict_sales(month, product, region)
    st.success(f"Predicted Sales: {prediction}")

# Optional: Show Historical Sales Chart
df = pd.read_csv("data/sales_small.csv")
st.subheader("📈 Historical Sales Data")
st.line_chart(df.pivot(index='Month', columns='Product', values='Sales'))
