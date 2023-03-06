import streamlit as st
import openai


st.title('Automatic Marketing Content Generator')
openai.api_key = st.secrets['api_key']

def text_generation(bullet_points):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",temperature=0.7,max_tokens=900,
      messages=[
            {"role": "system", "content": "You are an expert in the marketing industry. Write a blog based on the bullet points from the message. Make the blog funny and easy to read. Then write a tweet based on the blog. Your slogan is 'Doing it Differently!'"},
            {"role": "user", "content": {}.format(bullet_points)},
        ]
    )
    return response['choices'][0]['message']['content']

bullet_points = st.text_area('Bullet points for your content:')
if bullet_points:
    st.write(text_generation(bullet_points))
