import streamlit as st
import pandas as pd
import pickle

# Load saved model
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Page title
st.title("📊 Telco Customer Churn Prediction")
st.write("Enter customer information to predict whether the customer will churn.")

# Customer information
gender = st.selectbox("Gender", ["Female", "Male"])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    value=12
)

phone = st.selectbox("Phone Service", ["Yes", "No"])

multiple = st.selectbox(
    "Multiple Lines",
    ["No phone service", "No", "Yes"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

security = st.selectbox(
    "Online Security",
    ["No internet service", "No", "Yes"]
)

backup = st.selectbox(
    "Online Backup",
    ["No internet service", "No", "Yes"]
)

device = st.selectbox(
    "Device Protection",
    ["No internet service", "No", "Yes"]
)

tech = st.selectbox(
    "Tech Support",
    ["No internet service", "No", "Yes"]
)

tv = st.selectbox(
    "Streaming TV",
    ["No internet service", "No", "Yes"]
)

movies = st.selectbox(
    "Streaming Movies",
    ["No internet service", "No", "Yes"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)


# Prediction button
if st.button("Predict Churn"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone],
        "MultipleLines": [multiple],
        "InternetService": [internet],
        "OnlineSecurity": [security],
        "OnlineBackup": [backup],
        "DeviceProtection": [device],
        "TechSupport": [tech],
        "StreamingTV": [tv],
        "StreamingMovies": [movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]
    })

    # Binary encoding
    binary_cols = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling"
    ]

    mapping = {
        "Yes": 1,
        "No": 0
    }

    for col in binary_cols:
        if col == "gender":
            input_data[col] = input_data[col].map({
                "Female": 0,
                "Male": 1
            })
        else:
            input_data[col] = input_data[col].map(mapping)

    # One-hot encoding
    multi_cat_cols = [
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaymentMethod"
    ]

    input_data = pd.get_dummies(
        input_data,
        columns=multi_cat_cols,
        drop_first=True
    )

    # Make sure input has same columns as training data
    input_data = input_data.reindex(
        columns=columns,
        fill_value=False
    )

    # Scale numerical columns
    num_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    input_data[num_cols] = scaler.transform(
        input_data[num_cols]
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    # Result
    if prediction == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")