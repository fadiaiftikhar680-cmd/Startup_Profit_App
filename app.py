import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Startup Profit Prediction App")

st.write("Enter 5 feature values")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")
feature4 = st.number_input("Feature 4")
feature5 = st.number_input("Feature 5")

if st.button("Predict"):

    data = np.array([[feature1, feature2, feature3, feature4, feature5]])

    prediction = model.predict(data)

    st.success(f"Prediction: {prediction[0]:,.2f}")