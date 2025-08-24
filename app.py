import streamlit as st
import joblib
import os
import numpy as np

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.write("Predict a student's **Math score** from their **Reading** and **Writing** scores.")

model_path = os.path.join("models", "model.pkl")

if not os.path.exists(model_path):
    st.warning("No trained model found. Please run `python src/train_model.py` first to create models/model.pkl.")
else:
    model = joblib.load(model_path)

reading = st.number_input("Reading score (0-100)", min_value=0, max_value=100, value=70, step=1)
writing = st.number_input("Writing score (0-100)", min_value=0, max_value=100, value=70, step=1)

if st.button("Predict Math score"):
    if os.path.exists(model_path):
        X = np.array([[reading, writing]])
        pred = model.predict(X)[0]
        st.success(f"Predicted Math score: **{pred:.1f}** / 100")
    else:
        st.info("Train the model first!")
