import streamlit as st
import openai

---------------------------------------------------------------
st.title('Automatic Marketing Content Generator')
openai.api_key = st.secrets['api_key']
