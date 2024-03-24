import os 
# from apikey import apikey 

import streamlit as st 
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper

# os.environ['OPENAI_API_KEY'] = apikey

st.title('🦜🔗 Tweet Generator')
prompt = st.text_input('Tweet topic: ')