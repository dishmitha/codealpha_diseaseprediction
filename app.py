import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f8fafc, #dbeafe);
}

/* General Text */
html, body, p, div, span, label {
    color: #111827 !important;
}

/* Number Input */
.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
}

/* Select Box */
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
    border-radius: 8px !important;
}

/* Dropdown text */
div[data-baseweb="select"] span {
    color: black !important;
}

/* Labels */
label {
    color: black !important;
    font-weight: 600 !important;
}

/* Header Card */
.header-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.main-title {
    text-align: center;
    color: #dc2626 !important;
    font-size: 42px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #374151 !important;
    font-size: 18px;
}

/* Button */
.stButton > button {
    background-color: #dc2626;
    color: white !important;
    border-radius: 10px;
    width: 100%;
    height: 55px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #b91c1c;
    color: white !important;
}

/* Success Card */
.result-success {
    padding: 15px;
    border-radius: 12px;
    background-color: #dcfce7;
    color: #166534 !important;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

/* Danger Card */
.result-danger {
    padding: 15px;
    border-radius: 12px;
    background-color: #fee2e2;
    color: #991b1b !important;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD MODEL
# ==========================
model = joblib.load("disease_model.pkl")

# ==========================
# HEADER
# ==========================
st.markdown("""
<div class="header-card">
    <div class="main-title">❤️ Heart Disease Prediction</div>
    <div class="sub-title">
        CodeAlpha Machine Learning Internship Project
    </div>
</div>
""", unsafe_allow_html=True)

st.write("### Enter Patient Details")

# ==========================
# INPUT SECTION
# ==========================
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 40)

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "ASY", "TA"]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        80, 250, 120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        0, 700, 200
    )

with col2:
    fasting_bs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

    max_hr = st.number_input(
        "Maximum Heart Rate",
        60, 220, 150
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        ["N", "Y"]
    )

    oldpeak = st.number_input(
        "Oldpeak",
        0.0, 10.0, 1.0
    )

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

# ==========================
# ENCODING MAPS
# ==========================
sex_map = {
    "Female": 0,
    "Male": 1
}

cp_map = {
    "ASY": 0,
    "ATA": 1,
    "NAP": 2,
    "TA": 3
}

ecg_map = {
    "LVH": 0,
    "Normal": 1,
    "ST": 2
}

angina_map = {
    "N": 0,
    "Y": 1
}

slope_map = {
    "Down": 0,
    "Flat": 1,
    "Up": 2
}

# ==========================
# PREDICTION
# ==========================
if st.button("🔍 Predict Heart Disease Risk"):

    input_data = pd.DataFrame([[
        age,
        sex_map[sex],
        cp_map[chest_pain],
        resting_bp,
        cholesterol,
        fasting_bs,
        ecg_map[resting_ecg],
        max_hr,
        angina_map[exercise_angina],
        oldpeak,
        slope_map[st_slope]
    ]], columns=[
        'Age',
        'Sex',
        'ChestPainType',
        'RestingBP',
        'Cholesterol',
        'FastingBS',
        'RestingECG',
        'MaxHR',
        'ExerciseAngina',
        'Oldpeak',
        'ST_Slope'
    ])

    prediction = model.predict(input_data)[0]

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == 0:
        st.markdown(
            """
            <div class="result-success">
            ✅ LOW RISK OF HEART DISEASE
            </div>
            """,
            unsafe_allow_html=True
        )
        

    else:
        st.markdown(
            """
            <div class="result-danger">
            ⚠️ HIGH RISK OF HEART DISEASE
            </div>
            """,
            unsafe_allow_html=True
        )