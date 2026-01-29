# Customer Churn Prediction 🚀

This project is an end-to-end **Customer Churn Prediction** system built using Machine Learning and deployed using **Streamlit**.


## 📌 Problem Statement
Customer churn is a major challenge for subscription-based businesses.  
This project predicts whether a customer is likely to churn so that businesses can take proactive retention actions.


## 🧠 Model Used
- Logistic Regression
- Binary classification (Churn: Yes / No)


## ⚙️ Features Used
- Customer demographics (gender, senior citizen, partner, dependents)
- Services subscribed (internet, phone, streaming, security)
- Contract type and payment method
- Tenure and billing information


## 🖥️ Application Overview
The Streamlit web application:
- Collects user-friendly inputs via dropdowns and sliders
- Internally performs one-hot encoding
- Loads a trained model using `joblib`
- Displays churn prediction along with probability (%)


## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  


## 🚀 How to Run Locally
```bash
pip install streamlit
streamlit run app.py
---

## 📈 Output
- Predicts whether a customer will churn (Yes / No)
- Displays churn probability (%) to indicate prediction confidence

---

## 📌 Business Use Case
This application can help businesses to:
- Identify customers with high churn risk
- Take proactive retention measures
- Improve customer lifetime value
- Reduce revenue loss due to churn

---

## ✨ Author
Srishti Pandey
