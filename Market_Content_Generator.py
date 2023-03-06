import streamlit as st
import openai


st.title('Automatic Marketing Content Generator')
openai.api_key = st.secrets['api_key']

def text_generation(content_types, bullet_points):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",temperature=0.7,max_tokens=900,
      messages=[
            {"role": "system", "content": "You are an expert in the marketing industry. Write a {} based on the bullet points from the message. Make sure it's funny and easy to read. Your slogan is 'Doing it Differently!'".format(content_types)},
            {"role": "user", "content": "{}".format(bullet_points)},
        ]
    )
    return response['choices'][0]['message']['content']


content_types = st.multiselect('What types of content do you want to generate?',['blog','tweet','facebook post'],['blog'])
bullet_points = st.text_area('Bullet points for your content:').join(', and')
if st.button('Generate!'):
    response = text_generation(content_types,bullet_points)
