import streamlit as st
from main import callOpenAI

st.title("CustomGPT Summarizer.")

user_input = st.text_area("Text", placeholder="Bitte hier den Text eingeben...")

if st.button("Zusammenfassen"):
    response = callOpenAI(user_input)
    st.write(response)

