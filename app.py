import streamlit as st
import joblib
import numpy as np

model = joblib.load("titanic_model.pkl")

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")
st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details below to predict survival:")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.radio("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 80, 25)
fare = st.slider("Fare", 0.0, 500.0, 50.0)
sibsp = st.slider("Siblings/Spouses", 0, 5, 0)
parch = st.slider("Parents/Children", 0, 5, 0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

sex = 0 if sex == "Male" else 1
embarked = {"C": 0, "Q": 1, "S": 2}[embarked]

if st.button("Predict Survival"):
    features = np.array([[pclass, sex, age, fare, sibsp, parch, embarked]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ This passenger would have survived!")
    else:
        st.error("❌ This passenger would not have survived.")
