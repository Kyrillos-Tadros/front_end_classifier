import streamlit as st
import requests
import os
import subprocess

#url = 'http://0.0.0.0:8000'
url = 'https://****-ew.a.run.app'

audio_file_buffer = st.file_uploader('')

if audio_file_buffer is not None:
    res = requests.post(url + "/detect_audio", files={'audio': audio_file_buffer})
    audio_path = os.path.join(os.getcwd(),'user_audio.wav')

    if os.path.exists(audio_path):
        os.remove(audio_path)

    if res.status_code == 200:
        result = res.content
        st.write(result)
    else:
        st.markdown("**Oops**, something went wrong :sweat: Please try again.")
        print(res.status_code, res.content)
