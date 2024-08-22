import streamlit as st
import google.generativeai as genai

st.title("Welcome to AI Chat")


genai.configure(api_key="AIzaSyCHYckqo6n1Q5PSPTgK8jI9JawInMM4fGQ")
  
text = st.text_input("Enter your Question") 

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
