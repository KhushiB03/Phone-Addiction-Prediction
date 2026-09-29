import joblib
import pandas as pd

#test if model loads or not
def test_model():
    model = joblib.load("src/addiction_model.pkl")
    #true if loads
    assert model is not None

#does model predicts and classifies
def test_model_prediction():
    model = joblib.load("src/addiction_model.pkl")
    input_data = pd.DataFrame([{
         "id": 1,
        "age": 21,
        "gaming_hours": 2.0,
        "work_study_hours": 5.0,
        "sleep_hours": 6.0,
        "notifications_per_day": 100,
        "app_opens_per_day": 80,
        "weekend_screen_time": 8.0,
        "gender": "Male",
        "stress_level": "High",
        "academic_work_impact": "Yes"

    }])
    prediction = model.predict(input_data)[0]
    assert prediction in [0,1]
