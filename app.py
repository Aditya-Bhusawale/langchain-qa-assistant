import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot with Groq"


prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant.plz response to a user query"),
    ("user","Question:{question}")
])


def generate_response(question):
    llm=ChatGroq(model="llama-3.3-70b-versatile")
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({"question":question})
    return answer


st.title("Q&A Chatbot")

question=st.text_input("Ask Question...")

if question:
    response=generate_response(question)
    st.write(response)
else:
    st.write("please provide the user input")

