import requests 
import streamlit as st
# api from api.nasa.gov
api_key ='L4VW9bSymbQah651NSfuE20El7FxzxC8lYq8DPaN'

url =f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = requests.get(url)

content = request.json()
explanation = content["explanation"]

request_image = requests.get(content["url"])


with open('image.jpg','wb') as file:
    file.write(request_image.content)

    st.image("image.jpg")
    st.write(explanation)

