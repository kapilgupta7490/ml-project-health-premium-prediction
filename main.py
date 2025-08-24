import streamlit as st
from prediction_helper import predict

st.title('Health Insurance Prediction App')

# Row 0
row0_col1, row0_col2, row0_col3 = st.columns(3)
with row0_col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with row0_col2:
    number_of_dependants = st.number_input("No. of Dependent", min_value=0, max_value=5, step=1)
with row0_col3:
    income_lakhs = st.number_input("Income in Lakhs", min_value=0, max_value=1000, step=1)

# Row 1
row1_col1, row1_col2, row1_col3 = st.columns(3)
with row1_col1:
    gender = st.selectbox("Gender", ['Male', 'Female'])
with row1_col2:
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
with row1_col3:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

# Row 2
row2_col1, row2_col2, row2_col3 = st.columns(3)
with row2_col1:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
with row2_col2:
    smoking_status = st.selectbox("Smoking Status", [
        'No Smoking', 'Regular', 'Occasional', 'Does Not Smoke', 'Not Smoking', 'Smoking=0'
    ])
with row2_col3:
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])

# Row 3
row3_col1, row3_col2, row3_col3 = st.columns(3)
with row3_col1:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row3_col2:
    medical_history = st.selectbox("Medical History", [
        'Diabetes', 'High blood pressure', 'No Disease',
        'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ])
with row3_col3:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

if st.button('Predict'):
    input_data = {
        "age": age,
        "number_of_dependants": number_of_dependants,
        "income_lakhs": income_lakhs,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "genetical_risk": genetical_risk,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan
    }
    prediction=predict(input_data)
    st.success(f'Predicted Health Insurance Cost: {prediction}')