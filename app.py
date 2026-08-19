
import streamlit as st
import joblib

# Load trained models
category_model = joblib.load("models/category_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")
anomaly_model = joblib.load("models/anomaly_model.pkl")

# Page configuration
st.set_page_config(
    page_title="FinSight",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 FinSight")
st.subheader("Personal Finance Intelligence")

st.write(
    "Enter a transaction description and amount to predict "
    "its category and check whether the transaction looks unusual."
)

# User inputs
description = st.text_input(
    "Transaction Description",
    placeholder="e.g., Starbucks"
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=10.0,
    step=1.0
)

# Prediction button
if st.button("Analyze Transaction"):

    if description.strip() == "":
        st.warning("Please enter a transaction description.")

    else:
        # Category prediction
        description_tfidf = tfidf.transform([description])
        predicted_category = category_model.predict(
            description_tfidf
        )[0]

        # Anomaly prediction
        anomaly_prediction = anomaly_model.predict(
            [[amount]]
        )[0]

        st.divider()

        st.subheader("Prediction Results")

        st.write(
            f"**Predicted Category:** {predicted_category}"
        )

        if anomaly_prediction == -1:
            st.error("⚠️ This transaction looks unusual.")
        else:
            st.success("✅ This transaction looks normal.")
