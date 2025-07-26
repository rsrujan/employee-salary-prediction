import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("best_salary_predictor_model.pkl")
scaler = joblib.load("scaler.pkl")  # ✅ Load scaler too

st.title("🧠 Employee Salary Prediction App")
st.markdown("Enter employee details below to predict the salary.")

# Input
experience = st.slider("Years of Experience", 0.0, 30.0, step=0.1)

if st.button("Predict Salary"):
    input_df = pd.DataFrame([[experience]], columns=["Years of Experience"])
    input_scaled = scaler.transform(input_df)  # ✅ Use the loaded scaler
    prediction = model.predict(input_scaled)
    st.success(f"💰 Predicted Salary: ₹{prediction[0]:,.2f}")
