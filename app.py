import streamlit as st
import joblib
import numpy as np

# 🔄 Load the saved LinearRegression model correctly
model = joblib.load('electricity_model.pkl')

st.title("🔌 Energy Usage Predictor")

temp = st.number_input("Average Temperature (°C)", value=10.0)
heating_days = st.number_input("Total Heating Degree Days", value=100)
cooling_days = st.number_input("Total Cooling Degree Days", value=50)

if st.button("Predict Energy Usage"):
    input_data = np.array([[temp, heating_days, cooling_days]])
    prediction = model.predict(input_data)
    st.success(f"📈 Predicted Avg. Electricity Usage: {prediction[0]:.2f} kWh")
