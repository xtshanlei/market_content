import streamlit as st
import openai


st.sidebar.title('Marketing Content Generator')
st.sidebar.write('By Yulei')
openai.api_key = st.secrets['api_key']

def text_generation(content_types, bullet_points,slogan):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",temperature=0.7,max_tokens=900,
      messages=[
            {"role": "system", "content": "You are an expert in the marketing industry. Write a {} based on the bullet points from the message. Make sure it's funny and easy to read. Your slogan is '{}'. If it's a blog, the word counts should be around 500.".format(content_types,slogan)},
            {"role": "user", "content": "{}".format(bullet_points)},
        ]
    )
    return response['choices'][0]['message']['content']


content_types = ', and '.join(st.sidebar.multiselect('What types of content do you want to generate?',['blog','tweet','facebook post'],['blog']))
slogan = st.sidebar.text_input('What is your marketing slogan?')
bullet_points = st.sidebar.text_area('Bullet points for your content:')

st.header('Generated Content by AI')
if st.sidebar.button('Generate!'):
    response = text_generation(content_types,bullet_points,slogan)
    st.write(response)
