#In this AI-powered fraud detection system, FraudShield utilises machine learning (ML) to analyze 
#financial transactions in real-time, identifying potential fraud risks and providing predictive insights.

#Import libraries
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the pre-trained fraud detection model
model = joblib.load("fraud_detection_pipeline.pkl")

# Set up the Streamlit application with improved styling
st.set_page_config(page_title="FraudShield", page_icon="🔍", layout="centered")

# App Title & Introduction
st.title("🚀 FraudShield: AI-Powered Fraud Detection")
st.markdown("""
### 🔍 Secure Your Transactions with FraudShield  
FraudShield is an AI-powered **fraud detection tool** that analyses transaction details and predicts 
**fraud risk in real-time** using machine learning.  
Simply enter transaction details, click **'Predict Fraud Risk'**, and get an instant fraud assessment 
with **risk probability!**
""")

st.divider()  

# User Input Section with Clean UI Formatting
st.subheader("📋 Enter Transaction Details")

# Transaction type selection
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"], index=0)

# Numeric inputs in columns for better layout
col1, col2 = st.columns(2)
amount = col1.number_input("💰 Amount", min_value=0.0, value=1000.0, step=100.0)
oldbalanceOrg = col2.number_input("🏦 Old Balance (Sender)", min_value=0.0, value=1000.0)

col3, col4 = st.columns(2)
newbalanceOrig = col3.number_input("📉 New Balance (Sender)", min_value=0.0, value=900.0)
oldbalanceDest = col4.number_input("🏦 Old Balance (Receiver)", min_value=0.0, value=0.0)

col5, col6 = st.columns(2)
newbalanceDest = col5.number_input("📈 New Balance (Receiver)", min_value=0.0, value=0.0)

st.divider()

# Predict Fraud Risk Button
if st.button("🔍 Predict Fraud Risk", type="primary"):
    # Creating input DataFrame
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Making fraud prediction
    prediction_proba = model.predict_proba(input_data)[0]  # Get fraud probability
    fraud_risk = prediction_proba[1]  # Probability of fraud (class 1)

    st.divider()
    st.subheader("📊 Prediction Result")

    # Display fraud probability score
    st.write(f"**Fraud Probability: {fraud_risk:.2%}**")

    if fraud_risk > 0.5:
        st.error("⚠️ **High Fraud Risk Detected!** Please verify this transaction.")
    elif fraud_risk > 0.2:
        st.warning("⚠️ **Moderate Fraud Risk!** Proceed with caution.")
    else:
        st.success("✅ **Low Fraud Risk** - This transaction appears legitimate.")

    st.divider()

    # 🌟 Fraud Risk Explanation
    st.subheader("💡 What Influences Fraud Prediction?")
    st.markdown("""
    - **Transaction Amount**: Large amounts are often flagged as risky.  
    - **Balance Behavior**: Sudden drops in sender or receiver balance may indicate fraud.  
    - **Transaction Type**: Fraud is more common in **TRANSFER & CASH_OUT** transactions.  
    - **Account Activity**: Suspicious transactions with extreme balance changes might be fraud.  
    """)

# Footer Info
st.markdown("""
---
💡 **FraudShield** helps businesses analyze transactions and minimize fraud risks using AI-powered
fraud detection models.
""")
