import os
import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPEN_API_KEY")


def get_openai_response(question: str) -> str:
    llm = OpenAI(api_key=API_KEY,
                 model="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm.invoke(question)
    return response


st.set_page_config(page_title="Q&A Chatbot", page_icon="🤖")
st.header("LangChain Q&A Chatbot")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask The Question")

if submit:
    st.subheader("The Response is")
    st.write(response)
