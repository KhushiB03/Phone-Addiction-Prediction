# 📱 Phone Addiction Prediction

A machine learning-based web application that predicts whether a user is likely to show signs of phone addiction based on factors such as screen time, social media usage, gaming time, sleep, notifications, app usage, stress level, and academic/work impact.

The application is built with **Python and Streamlit** and provides an interactive interface for making predictions using a trained machine learning model.

---

## 🚀 Live Demo

**Streamlit App:**
https://phone-addiction-prediction-zoyfchvnbnbqrzkje3fghy.streamlit.app/

---

## ✨ Features

* 📱 Predicts phone addiction using a trained ML model
* ⏱️ Uses daily and weekend screen-time information
* 📲 Considers social media usage and gaming hours
* 🔔 Considers notifications and app openings per day
* 😴 Includes sleep hours as an input
* 🧠 Considers stress level
* 🎓 Considers academic/work impact
* 👤 Includes age and gender
* 🌐 Interactive Streamlit web interface
* 🧪 Automated model testing with `pytest`
* ⚙️ Continuous Integration using GitHub Actions

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* Scikit-learn
* Joblib

### Web Application

* Streamlit

### Testing & CI

* Pytest
* GitHub Actions

---

## 📂 Project Structure

```text
Phone-Addiction-Prediction/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── src/
│   └── addiction_model.pkl
│
├── tests/
│   └── test_model.py
│
├── app.py
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

The application collects information from the user through the Streamlit interface.

The inputs include:

* ID
* Age
* Daily screen time
* Social media hours
* Gaming hours
* Work/study hours
* Sleep hours
* Notifications per day
* App opens per day
* Weekend screen time
* Gender
* Stress level
* Academic/work impact

The collected information is converted into a Pandas DataFrame and passed to the trained machine learning model.

The model returns:

```text
1 → Addiction detected
0 → No addiction detected
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/KhushiB03/Phone-Addiction-Prediction.git
```

### 2. Move into the project directory

```bash
cd Phone-Addiction-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Testing

This project uses **pytest** for automated testing.

Run the tests locally with:

```bash
pytest
```

The tests verify that:

1. The trained machine learning model can be loaded successfully.
2. The model accepts the expected input format.
3. The model produces a valid prediction (`0` or `1`).

---

## ⚙️ GitHub Actions

GitHub Actions is used for Continuous Integration (CI).

Whenever code is pushed to the `main` branch or a pull request targets `main`, GitHub Actions automatically:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs the pytest test suite.

Workflow file:

```text
.github/workflows/tests.yml
```

The workflow helps ensure that changes to the project do not break the existing model functionality.

---

## 📊 Prediction Output

The application displays one of two results:

### Prediction 1

```text
📱 Addiction detected
```

### Prediction 0

```text
✅ No addiction detected
```

---

## 🔮 Future Improvements

* Add model performance metrics such as accuracy, precision, recall, and F1-score.
* Add more comprehensive input validation tests.
* Add additional machine learning models for comparison.
* Improve prediction explanations using model interpretability techniques.
* Add automated model performance testing.
* Add continuous deployment improvements.
* Add data visualization for user inputs and prediction-related patterns.

---

## ⚠️ Disclaimer

This application is a machine learning project intended for educational and research purposes. Its predictions should not be treated as a medical or clinical diagnosis.

---

## 👩‍💻 Author

**Khushi Bhardwaj**

Computer Science Engineering Student | Machine Learning Enthusiast


