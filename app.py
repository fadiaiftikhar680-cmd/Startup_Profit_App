import streamlit as st
import joblib
import numpy as np

# 1. Saved model ko load karein
model = joblib.load("model.pkl")

# 2. Website ka Title aur Description
st.title("Startup Profit Prediction App 🚀")
st.write("Enter the startup's expenditures to predict its profit.")

# 3. User se input lene ke liye boxes
rd_spend = st.number_input("R&D Spend ($)", min_value=0.0, value=100000.0)
admin_spend = st.number_input("Administration Spend ($)", min_value=0.0, value=100000.0)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=0.0, value=200000.0)

# State selection dropdown
state = st.selectbox("Select State", ["California", "Florida", "New York"])

# 4. State input ko pre-process karna (State_Florida, State_New York)
state_florida = 1 if state == "Florida" else 0
state_new_york = 1 if state == "New York" else 0

# 5. Prediction Button
if st.button("Predict Profit"):
    # Features ka array banana (R&D, Admin, Marketing, Florida, New York)
    features = np.array([[rd_spend, admin_spend, marketing_spend, state_florida, state_new_york]])
    
    # Model se predict karwana
    prediction = model.predict(features)[0]
    
    # Result display karna
    st.success(f"The Predicted Profit is: ${prediction:,.2f}")