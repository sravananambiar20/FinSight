# 💰 FinSight

## Personal Finance Intelligence

FinSight is a machine-learning powered personal finance application that predicts transaction categories and detects unusual transactions.

The application uses transaction descriptions and amounts to provide real-time predictions through a Streamlit interface.

## 🚀 Features

- Transaction category prediction
- Unusual transaction detection
- TF-IDF based text feature extraction
- Logistic Regression for transaction categorization
- Isolation Forest for anomaly detection
- Interactive Streamlit web application
- Real-time transaction analysis

## 🧠 Machine Learning

### Transaction Categorization

A Logistic Regression model is used to classify transaction descriptions into spending categories.

Text descriptions are transformed into numerical features using TF-IDF vectorization.

### Anomaly Detection

An Isolation Forest model is used to identify potentially unusual transactions based on transaction amount.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- TF-IDF
- Logistic Regression
- Isolation Forest

## 📁 Project Structure

```text
FinSight/
│
├── Notebooks/
├── data/
├── models/
│   ├── anomaly_model.pkl
│   ├── category_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── requirements.txt
├── FinSight_Analysis (1).ipynb
└── README.md
```

## ▶️ Run Locally

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

## 🌐 Live Application

FinSight is deployed using Streamlit Community Cloud.

## 📊 Example

Input:

Transaction Description: Starbucks  
Transaction Amount: 10

Output:

Category: Coffee Shops  
Transaction Status: Normal

## 👩‍💻 Project

FinSight was developed as a machine-learning project demonstrating text classification and anomaly detection for personal finance data.
