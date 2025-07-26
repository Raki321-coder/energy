# energy
🔌 Energy Usage Predictor

A simple machine learning project to predict monthly electricity usage (in kWh) based on average temperature and heating/cooling degree days.

🚀 Project Overview

This project uses linear regression to model the relationship between energy consumption and climate variables such as:

Average Monthly Temperature (°C)

Heating Degree Days (HDD)

Cooling Degree Days (CDD)

An interactive web interface is built using Streamlit, allowing users to enter their own climate inputs and get a predicted energy usage instantly.

📊 Model Summary

Model Type: LinearRegression() from sklearn

Input Features: [Avg Temp, HDD, CDD]

Target: Monthly Electricity Usage (kWh)

Model Accuracy:

Root Mean Squared Error: ~1433.83 kWh

Percent Error: ~24.85%

📂 Files Included

File

Description

Energy_Project.ipynb

Full Jupyter Notebook with data exploration, model training, and evaluation

electricity_model.pkl

Saved machine learning model using joblib

app.py

Streamlit app script to run the web-based predictor

🔧 How to Run

1. Install dependencies

pip install streamlit numpy scikit-learn

2. Launch the Streamlit app

streamlit run app.py

3. Use the app

In your browser:

Enter the average temperature, HDD, and CDD

Click Predict Energy Usage

Get your estimated electricity consumption!

🌍 Use Cases

Forecast electricity demand based on seasonal temperature shifts

Educate users on energy-climate relationships

Add-ons: connect to real-time weather API, or use historical building data for personalized prediction
