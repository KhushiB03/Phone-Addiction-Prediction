import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("src/addiction_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Addiction Prediction",
    page_icon="📱"
)


# Title
st.title("📱 Addiction Prediction")
st.write("Enter the details below to predict the addiction label.")


# Inputs
id_value = st.number_input(
    "ID",
    min_value=0,
    value=1
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=21
)

daily_screen_time_hours = st.number_input(
    "Daily Screen Time (hours)",
    min_value=0.0,
    value=7.0
)

social_media_hours = st.number_input(
    "Social Media Hours",
    min_value=0.0,
    value=4.0
)

gaming_hours = st.number_input(
    "Gaming Hours",
    min_value=0.0,
    value=2.0
)

work_study_hours = st.number_input(
    "Work/Study Hours",
    min_value=0.0,
    value=5.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

notifications_per_day = st.number_input(
    "Notifications per Day",
    min_value=0,
    value=100
)

app_opens_per_day = st.number_input(
    "App Opens per Day",
    min_value=0,
    value=80
)

weekend_screen_time = st.number_input(
    "Weekend Screen Time",
    min_value=0.0,
    value=8.0
)


gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

academic_work_impact = st.selectbox(
    "Academic Work Impact",
    ["No", "Yes"]
)


# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "id": id_value,
        "age": age,
        "daily_screen_time_hours": daily_screen_time_hours,
        "social_media_hours": social_media_hours,
        "gaming_hours": gaming_hours,
        "work_study_hours": work_study_hours,
        "sleep_hours": sleep_hours,
        "notifications_per_day": notifications_per_day,
        "app_opens_per_day": app_opens_per_day,
        "weekend_screen_time": weekend_screen_time,
        "gender": gender,
        "stress_level": stress_level,
        "academic_work_impact": academic_work_impact
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Prediction: 1 — Addiction detected")
    else:
        st.success("Prediction: 0 — No addiction detected")