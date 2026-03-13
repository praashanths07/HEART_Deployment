# ❤️ Heart Disease Prediction System

A **Machine Learning web application** built with **Python and
Streamlit** that predicts the risk of heart disease based on patient
medical attributes. The app provides a simple and interactive interface
where users can enter clinical parameters and receive an instant
prediction from a trained ML model.

------------------------------------------------------------------------

## 🚀 Project Overview

Heart disease is one of the leading causes of death worldwide. This
project uses a trained machine learning model to analyze patient health
data and predict whether a person is at **high risk or low risk of heart
disease**.

Users can enter medical details such as age, cholesterol level, blood
pressure, and other cardiovascular indicators to generate predictions.

------------------------------------------------------------------------

## 🧠 Machine Learning Features Used

The prediction model uses the following attributes:

-   Age
-   Sex
-   Chest Pain Type
-   Resting Blood Pressure
-   Cholesterol Level
-   Fasting Blood Sugar
-   Resting ECG Results
-   Maximum Heart Rate Achieved
-   Exercise Induced Angina
-   ST Depression (Oldpeak)
-   Slope of ST Segment
-   Number of Major Vessels
-   Thalassemia

------------------------------------------------------------------------

## 💻 Application Features

-   Interactive **Streamlit Web Interface**
-   **Light and Dark Theme** toggle
-   Real-time prediction of heart disease risk
-   User-friendly medical input form
-   Instant result showing **High Risk** or **Low Risk**

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Streamlit
-   NumPy
-   Pandas
-   Scikit-learn
-   Pickle

------------------------------------------------------------------------

## 📂 Project Structure

    Heart_Disease_Prediction
    │
    ├── app.py              # Streamlit web application
    ├── heart_model.pkl     # Trained ML model
    ├── scaler.pkl          # Feature scaler used during training
    ├── requirements.txt    # Python dependencies
    └── Heart_MLModel.ipynb # Model training notebook

------------------------------------------------------------------------

## ▶️ Running the Application

### 1. Clone the Repository

    git clone https://github.com/yourusername/Heart_Disease_Prediction.git
    cd Heart_Disease_Prediction

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Run the Streamlit App

    streamlit run app.py

The application will run locally at:

    http://localhost:8501

------------------------------------------------------------------------

## ⚠️ Disclaimer

This application is intended for **educational and demonstration
purposes only**.\
It should not be used as a substitute for professional medical advice or
diagnosis.

------------------------------------------------------------------------

## 👨‍💻 Author

Developed as a **Machine Learning and Data Analytics project**
demonstrating model deployment using Streamlit.
