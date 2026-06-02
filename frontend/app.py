import streamlit as st
import requests

st.title("Mock AI Demo")
text = st.text_input("Enter text")

if st.button("Predict"):
    r = requests.get("http://ai-backend-service:8000/predict", params={"text": text})  # internal DNS
    st.json(r.json())
