import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


st.set_page_config(page_title="Gemini Chatbot")
st.header("Gemini Chatbot")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Ask me anything: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")

    con_res = ""
    for chunk in response:
        con_res += chunk.text
    st.session_state['chat_history'].append(("Bot", con_res))
    st.write(con_res)

st.subheader("The Chat history is")

for role, text in st.session_state['chat_history']:
    if role == "You":
        st.write(f"**You**: {text}")
    else:
        st.write(f"**Bot**: {text}")
