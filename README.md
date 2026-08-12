# Customer Churn Prediction

## Project Overview

This project uses machine learning to predict whether a telecom customer is likely to churn.

The goal is to identify high-risk customers and help businesses take proactive customer-retention actions.

## Dataset

Telco Customer Churn Dataset

- Customers: 7,043
- Target Variable: Churn
- Churn = 1 → Customer likely to churn
- Churn = 0 → Customer likely to stay

## Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Encoding
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis
8. Churn Prediction
9. Streamlit Deployment

## Machine Learning Models

- Logistic Regression
- Random Forest

## Model Performance

|## Model Performance

**Logistic Regression**
- Accuracy: 82.11%
- Precision: 68.62%
- Recall: 59.79%
- F1-Score: 63.90%

**Random Forest**
- Accuracy: 80.20%
- Precision: 67.80%
- Recall: 47.99%
- F1-Score: 56.20%

**Selected Model:** Logistic Regression

Logistic Regression achieved better Recall and F1-Score than Random Forest.

## Best Model

Logistic Regression was selected as the final model because it achieved higher Recall and F1-Score compared with Random Forest.

## Important Features

- Tenure
- Total Charges
- Monthly Charges
- Internet Service
- Contract Type

## Streamlit Application

A Streamlit web application was developed to allow users to enter customer information and receive a churn prediction.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Author

**Pruthviraj Pawar**

M.Sc. Data Science