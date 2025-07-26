
import streamlit as st
import joblib

st.title("🗞️ News Headline Classifier")

headline = st.text_input("Enter a news headline:")

if headline:
    model = joblib.load("models/news_model.joblib")
    vectorizer = joblib.load("models/tfidf_vectorizer.joblib")
    vec = vectorizer.transform([headline])
    pred = model.predict(vec)[0]
    st.success(f"📂 Predicted Category: {pred}")
