

# Heart Disease Prediction Streamlit App

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- THEME TOGGLE ----------------

if "theme" not in st.session_state:
    st.session_state.theme = "light"

theme_choice = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])

if theme_choice == "Dark":
    st.markdown(""" <style>
body {background-color: #0E1117; color: white;}
.stApp {background-color: #0E1117;}

```
h1 {color:#00E5FF; text-align:center;}
h2 {color:#00E5FF;}
label {color:white !important;}
</style>
""", unsafe_allow_html=True)


else:
    st.markdown(""" <style>
body {background-color: white; color: black;}
.stApp {background-color: white;}

```
h1 {color:#1F4E79; text-align:center;}
h2 {color:#1F4E79;}
label {color:black !important;}
</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------

with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------- UI ----------------

# ---------------- UI ----------------

if theme_choice == "Dark":
    title_color = "white"
    subtitle_color = "white"
else:
    title_color = "black"
    subtitle_color = "black"

st.markdown(
f"""
<h1 style='color:{title_color}; text-align:center;'>
Heart Disease Prediction System
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
f"""
<p style='color:{subtitle_color}; text-align:center;'>
Enter patient medical details to predict the risk of heart disease.
</p>
""",
unsafe_allow_html=True
)

age = st.number_input("Age", min_value=20, max_value=100, value=50)

sex = st.selectbox(
"Sex",
["Female", "Male"]
)

cp_type = st.selectbox(
"Chest Pain Type",
["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
)

trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)

chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)

fbs = st.selectbox(
"Fasting Blood Sugar > 120 mg/dl",
["No", "Yes"]
)

restecg = st.selectbox(
"Resting ECG Result",
["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"]
)

thalach = st.number_input("Maximum Heart Rate Achieved", min_value=70, max_value=220, value=150)

exang = st.selectbox(
"Exercise Induced Angina",
["No", "Yes"]
)

oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=6.0, value=1.0)

slope = st.selectbox(
"Slope of Peak Exercise ST Segment",
["Upsloping", "Flat", "Downsloping"]
)

ca = st.selectbox(
"Number of Major Vessels (0-3)",
[0,1,2,3]
)

thal = st.selectbox(
"Thalassemia",
["Normal", "Fixed Defect", "Reversible Defect"]
)

# ---------------- ENCODING ----------------

sex = 1 if sex == "Male" else 0

cp_map = {
"Typical Angina":0,
"Atypical Angina":1,
"Non-anginal Pain":2,
"Asymptomatic":3
}
cp = cp_map[cp_type]

fbs = 1 if fbs == "Yes" else 0

restecg_map = {
"Normal":0,
"ST-T wave abnormality":1,
"Left ventricular hypertrophy":2
}
restecg = restecg_map[restecg]

exang = 1 if exang == "Yes" else 0

slope_map = {
"Upsloping":0,
"Flat":1,
"Downsloping":2
}
slope = slope_map[slope]

thal_map = {
"Normal":1,
"Fixed Defect":2,
"Reversible Defect":3
}
thal = thal_map[thal]

# ---------------- INPUT ARRAY ----------------

input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
restecg, thalach, exang, oldpeak,
slope, ca, thal]])

# ---------------- PREDICTION ----------------

# ---------------- PREDICTION ----------------

if st.button("Predict Heart Disease"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease")
        st.write("⚠️ Please consult a medical professional for further evaluation.")
    else:
        st.success("Low Risk of Heart Disease")
        st.write("Your heart condition appears normal based on the model prediction.")