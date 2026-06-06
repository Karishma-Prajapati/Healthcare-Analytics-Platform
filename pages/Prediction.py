import streamlit as st
import joblib
import pandas as pd

from utils.database import save_prediction
from utils.doctor_recommendation import suggest_doctors

heart_model = joblib.load("models/heart_model.pkl")
heart_scaler = joblib.load("models/heart_scaler.pkl")

diabetes_model = joblib.load("models/diabetes_model.pkl")
diabetes_scaler = joblib.load("models/diabetes_scaler.pkl")

st.title("🩺 Disease Prediction")

name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 100)

disease = st.selectbox(
    "Select Disease",
    ["Heart Disease", "Diabetes"]
)

# HEART
if disease == "Heart Disease":

    st.subheader("👤 Basic Information")
    age = st.number_input("Age", 1, 100, 30)
    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )
    sex = 1 if sex == "Male" else 0
    st.subheader("🩺 Symptoms")
    cp = st.selectbox(
        "Chest Pain Type",
        [0, 1, 2, 3]
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        [0, 1]
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1]
    )
    st.subheader("📊 Clinical Measurements")
    bp = st.slider(
        "Resting Blood Pressure",60,250,120
    )

    chol = st.slider(
        "Cholesterol",100,600,200
    )
    thalach = st.slider("Maximum Heart Rate",60,250,150)

    oldpeak = st.slider(
    "Oldpeak",
    0.0,
    10.0,
    1.0,
    0.1
)

    with st.expander("🧪 Advanced Cardiac Parameters"):
        restecg = st.selectbox(
        "Resting ECG",
        [0, 1, 2]
        )

        slope = st.selectbox(
        "Slope",
        [0, 1, 2]
        )
        ca = st.selectbox(
        "Major Vessels",
        [0, 1, 2, 3]
        )

        thal = st.selectbox(
        "Thalassemia",
        [1, 2, 3]
        )
        
        if st.button("Predict"):
            values = pd.DataFrame([[
                age,sex,cp,bp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
                ]], columns=[
                    "age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"
                ])
            values = heart_scaler.transform(values)
            prob = heart_model.predict_proba(values)[0][1]
            save_prediction(
            name,
            age,
            disease,
            prob
            )
            st.metric(
            "Risk %",
            f"{prob*100:.2f}%"
            )

            if prob > 0.5:
                st.error(
                f"⚠ High Risk Detected ({prob*100:.2f}%"
                )
                st.info("""
                    ### Next Steps

                    • Schedule a consultation with a specialist
                    
                    • Maintain a healthy diet
                    
                    • Exercise regularly
                    
                    • Follow prescribed medications
                    
                    • Monitor your health metrics
                    """)

                st.subheader("👨‍⚕ Recommended Specialists")

                doctors = suggest_doctors("Heart Disease")

                for doctor in doctors:
                    st.write("•", doctor)
            else:
                st.success(
                f"✅ Low Risk ({prob*100:.2f}%)"
                )

            st.subheader("Recommended Doctors")

            for doctor in suggest_doctors(disease):
                st.write("•", doctor)

# DIABETES
else:
    preg = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1
    )
    glucose = st.number_input(
    "Glucose",
    min_value=50,
    max_value=300,
    value=120
    )
    st.caption("Normal fasting glucose: 70–99 mg/dL")
    bp = st.number_input(
    "Blood Pressure",
    min_value=40,
    max_value=200,
    value=80
    )
    skin = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20
    )
    insulin = st.number_input(
    "Insulin",
    min_value=0,
    max_value=900,
    value=80
    )
    bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=70.0,
    value=25.0,
    step=0.1
    )
    dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5,
    step=0.01
    )

    if st.button("Predict"):

        values = pd.DataFrame([[
            preg, glucose,
            bp, skin,
            insulin,
            bmi,
            dpf,
            age
        ]])

        values = diabetes_scaler.transform(values)

        prob = diabetes_model.predict_proba(values)[0][1]

        save_prediction(
            name,
            age,
            disease,
            prob
        )

        st.metric(
            "Risk %",
            f"{prob*100:.2f}%"
        )

        if prob > 0.5:
            st.error(
                f"⚠ High Risk Detected ({prob*100:.2f}%)"
            )
            st.info("""
                    ### Next Steps

                    • Schedule a consultation with a specialist
                    
                    • Maintain a healthy diet
                    
                    • Exercise regularly
                    
                    • Follow prescribed medications
                    
                    • Monitor your health metrics
                    """)
            
            st.subheader("👨‍⚕ Recommended Specialists")
            doctors = suggest_doctors("Diabetes")

            for doctor in doctors:
                st.write("•", doctor)
        else:
            st.success(
            f"✅ Low Risk ({prob*100:.2f}%)"
            )