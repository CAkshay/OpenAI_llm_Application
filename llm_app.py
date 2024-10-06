import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']='Simple LLM app with OpenAI'

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import openai

llm_model=ChatOpenAI(model='gpt-4o')
prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are a helpfull assistant that help in answering users question, please answer the questions asked by users'),
        ('user','{question}')
    ]
)
output_parser=StrOutputParser()
chain=prompt|llm_model|output_parser


st.title('Simple LLM app with OpenAI')
input_text=st.text_input('Enter your question')

if input_text:
    st.write(chain.invoke({'question':input_text}))