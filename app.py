import streamlit as st
import joblib
import numpy as np

model = joblib.load('loan_model.pkl')

st.title("Loan Eligibility Prediction")

dependents = st.number_input("Number of Dependents", min_value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Annual Income")
loan_amt = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term (months)")
cibil = st.number_input("CIBIL Score")
residential = st.number_input("Residential Assets Value")
commercial = st.number_input("Commercial Assets Value")
luxury = st.number_input("Luxury Assets Value")
bank = st.number_input("Bank Asset Value")

if st.button("Predict"):
    # Encode categorical
    edu = 1 if education == "Graduate" else 0
    emp = 1 if self_employed == "Yes" else 0
    
    data = np.array([[dependents, edu, emp, income, loan_amt, loan_term, cibil,
                      residential, commercial, luxury, bank]])
    prediction = model.predict(data)
    
    st.success("Loan Approved" if prediction[0] == 1 else "Loan Rejected")
