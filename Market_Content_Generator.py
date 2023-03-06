import streamlit as st
import openai


st.title('Automatic Marketing Content Generator')
openai.api_key = st.secrets['api_key']

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",temperature=7,max_tokens=256,
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
st.write(response['choices'][0]['message']['content'])
