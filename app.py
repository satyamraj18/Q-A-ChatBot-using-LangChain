from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
#from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

def get_openai_response(question):
    chatllm = ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature=0.6,model='gpt-3.5-turbo')
    response = chatllm([SystemMessage(content="Yor are a helpful and smart AI assitant"),HumanMessage(content=question)])
    return response.content

st.set_page_config(page_title="Q&A Demo")
st.header("Q&A ChatBot using LangChain")
input=st.text_input("Input: ", key="input")
response=get_openai_response(input)
submit=st.button("Ask the question")

if submit:
    st.subheader("The response is")
    st.write(response)