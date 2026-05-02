import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('cgpa_model.pkl', 'rb'))

st.title("🎓 CGPA to Package Predictor")
st.write("Enter your CGPA to predict your salary package!")

cgpa = st.slider("Select CGPA", 5.0, 10.0, 7.0, 0.1)

if st.button("Predict Package"):
    result = model.predict([[cgpa]])
    st.success(f"💼 Predicted Package: {result[0]:.2f} LPA")
    