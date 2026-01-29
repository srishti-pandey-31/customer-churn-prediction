import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL & FEATURES ----------------

model = joblib.load("churn_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("Customer Churn Prediction")
st.write("Fill in customer details below:")

# ---------------- USER INPUTS (CLEAN UI) ----------------

gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

internet_service = st.selectbox(
    "Internet Service", ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security", ["No", "Yes", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup", ["No", "Yes", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection", ["No", "Yes", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support", ["No", "Yes", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV", ["No", "Yes", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies", ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract", ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# ---------------- ENCODING LOGIC ----------------

# Start with all-zero input
input_data = {feature: 0 for feature in features}

# Binary fields
input_data["gender"] = 1 if gender == "Male" else 0
input_data["SeniorCitizen"] = 1 if senior == "Yes" else 0
input_data["Partner"] = 1 if partner == "Yes" else 0
input_data["Dependents"] = 1 if dependents == "Yes" else 0
input_data["PhoneService"] = 1 if phone_service == "Yes" else 0

# Numeric fields
input_data["tenure"] = tenure
input_data["MonthlyCharges"] = monthly_charges
input_data["TotalCharges"] = total_charges

# Multiple lines
if multiple_lines == "Yes":
    input_data["MultipleLines_Yes"] = 1
elif multiple_lines == "No phone service":
    input_data["MultipleLines_No phone service"] = 1

# Internet service
if internet_service == "Fiber optic":
    input_data["InternetService_Fiber optic"] = 1
elif internet_service == "No":
    input_data["InternetService_No"] = 1

# Helper function for internet-related services
def encode_service(value, yes_col, no_internet_col):
    if value == "Yes":
        input_data[yes_col] = 1
    elif value == "No internet service":
        input_data[no_internet_col] = 1

encode_service(online_security, "OnlineSecurity_Yes", "OnlineSecurity_No internet service")
encode_service(online_backup, "OnlineBackup_Yes", "OnlineBackup_No internet service")
encode_service(device_protection, "DeviceProtection_Yes", "DeviceProtection_No internet service")
encode_service(tech_support, "TechSupport_Yes", "TechSupport_No internet service")
encode_service(streaming_tv, "StreamingTV_Yes", "StreamingTV_No internet service")
encode_service(streaming_movies, "StreamingMovies_Yes", "StreamingMovies_No internet service")

# Contract
if contract == "One year":
    input_data["Contract_One year"] = 1
elif contract == "Two year":
    input_data["Contract_Two year"] = 1

# Payment method
if payment_method == "Credit card (automatic)":
    input_data["PaymentMethod_Credit card (automatic)"] = 1
elif payment_method == "Electronic check":
    input_data["PaymentMethod_Electronic check"] = 1
elif payment_method == "Mailed check":
    input_data["PaymentMethod_Mailed check"] = 1

# ---------------- PREDICTION ----------------

input_df = pd.DataFrame([input_data])

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    churn_prob = probabilities[1] * 100
    stay_prob = probabilities[0] * 100

    if prediction == "Yes":
        st.error(f"Customer is likely to churn ({churn_prob:.2f}%)")
    else:
        st.success(f"Customer is NOT likely to churn ({stay_prob:.2f}%)")
