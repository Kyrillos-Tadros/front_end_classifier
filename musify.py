import streamlit as st
import requests
import json 

background_css = """
<style>
body {
  background-image: url('https://cdn.pixabay.com/photo/2016/01/14/06/09/woman-1139397_960_720.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  opacity: 0.8; /* Adjust the opacity as needed */
  color: white; /* Set text color to white */
  font-size: 2em; /* Increase font size */
  padding: 20px; /* Add padding for better visibility */
}
p{
  color:black;
}
hr {
  margin: 0px 0px;   
  }
  h1{
    padding: 0px;
  }
  .stTabs{
      margin-top:-75px;
  }
</style>
"""

st.markdown(background_css, unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["Main Page", "How to Use the App", "Genre Information"])

genre_info = {
                    "blues": "Blues is a genre of music that originated in the African American communities of the United States. It typically features melancholy lyrics and a distinctive musical style.",
                    "classical": "Classical music is a genre that encompasses a broad range of music from the Western tradition. It often features complex compositions and instrumental arrangements.",
                    "Ccountry": "Country music is a genre that originated in the Southern United States. It often highlights themes of rural life, love, and heartache.",
                    "disco": "Disco is a genre of dance music that was popular in the 1970s. It is characterized by a strong beat and electronic instrumentation.",
                    "hip hop": "Hip hop is a genre of music that emerged in the Bronx, New York City, during the 1970s. It is characterized by rhythmic speech over a beat.",
                    "jazz": "Jazz is a genre of  music that originated in the African American communities of New Orleans. It features improvisation and swing rhythms.",
                    "metal": "Metal is a genre of music that is characterized by its loud, aggressive sound. It often features distorted guitars and powerful vocals.",
                    "pop": "Pop music is a genre that encompasses popular music from various styles. It is often catchy and appeals to a broad audience.",
                    "reggae": "Reggae is a genre of music that originated in Jamaica. It is characterized by its offbeat rhythms and socially conscious lyrics.",
                    "rock": "Rock music is a genre that emerged in the 1950s and has since evolved into various subgenres. It typically features electric guitars and strong rhythms."
                }






with tab1:
  st.markdown("<h1 style='text-align: center; font-size: 1.5em;color: black;margin-top:-15px;'>Musify</h1>", unsafe_allow_html=True)
  st.markdown("<h2 style='text-align: center;color: black;margin-top: -19px;font-size: 0.9em;'>Genre Classification App</h2>", unsafe_allow_html=True)
  st.markdown("<hr style='border-top: 1px solid #000;color: black;'>", unsafe_allow_html=True)
  
  
  
  url = 'https://musicgc-k47xyyahgq-ew.a.run.app'  

  
  audio_file_buffer = st.file_uploader("Upload a music file for genre classification:") 
 

  
  if audio_file_buffer is not None:
    try:
        res = requests.post(url + "/upload_music", files={'mus': audio_file_buffer})
        if res.status_code == 200:
            result_dict = json.loads(res.content)
            predicted_genre = result_dict.get('prediction').lower()

            if predicted_genre:
                if predicted_genre in genre_info:
                    st.write("# Predicted Genre:" , predicted_genre)
                    
                    st.markdown(genre_info[predicted_genre])
                    st.audio(audio_file_buffer)
                else:
                    st.warning("Genre information not available for:" + predicted_genre)
            else:
                st.warning("No genre prediction found in the response.")
        else:
            st.markdown("**Oops**, something went wrong :sweat: Please try again.")
            print(res.status_code, res.content)
    except Exception as e:
        st.error(e)
        print(e)



  

  with tab2:
    st.markdown("""
    <h2 style='color: black; font-size: 21px;'>1. Upload a music file:</h2>
    <p style='color: black; font-size: 18px;'>Click the "Browse files" button and select the audio file you want to classify.</p>

    <h2 style='color: black; font-size: 21px;'>2. Wait for classification:</h2>
    <p style='color: black; font-size: 18px;'>Once you upload the file, the app will process it and predict the music genre. This might take a few seconds depending on the file size.</p>

    <h2 style='color: black; font-size: 21px;'>3. View results:</h2>
    <p style='color: black; font-size: 18px;'>After processing, the app will display the predicted genre.</p>
    """, unsafe_allow_html=True)
  
  
  
  with tab3:
    
    genre_label = st.subheader("**Select a Genre to Learn More About:**")  

    genre_dropdown = st.selectbox("", list(genre_info.keys()))  

    if genre_dropdown:
        st.markdown(genre_info[genre_dropdown])