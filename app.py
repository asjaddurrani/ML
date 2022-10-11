# import libraries

import streamlit as st
from PIL import Image

st.write(""" # Add Media File in Streamlit Web Application
        """)

# add image
st.write(""" ## Image """)
image1 = Image.open("image.jpg")
st.image(image1)

# add Video
st.write(""" ## Video """)
video1 = open("video.mp4","rb")
st.video(video1)

# add Audio
st.write(""" ## Audio """)
audio1 = open("audio.mp3","rb")
st.audio(audio1)