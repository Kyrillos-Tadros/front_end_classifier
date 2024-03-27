import streamlit as st
import requests

# Custom CSS style for full-page background image with less opacity and responsive layout
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

</style>
"""

# Apply the custom CSS style
st.markdown(background_css, unsafe_allow_html=True)

# Set the very large "Welcome" message using Markdown and center alignment
st.markdown("<h1 style='text-align: center; font-size: 3em;color: black;'>Welcome to</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 2.5em;color: black;'>Music Genre Classification App</h2>", unsafe_allow_html=True)
st.markdown("<hr style='border-top: 1px solid #bbb;color: black;'>", unsafe_allow_html=True)

# Create a slightly smaller "App usage" section
st.markdown("<h1 style='text-align: center; font-size: 2.5em;color: black;'>App Usage</h1>", unsafe_allow_html=True)
st.markdown("""
<h2 style= 'color: black;'>1. Upload a music file:</h2>
<p style= 'color: black;'>Click the "Browse files" button and select the audio file you want to classify.</p>

<h2 style= 'color: black;'>2. Wait for classification:</h2>
<p style= 'color: black;'>Once you upload the file, the app will process it and predict the music genre. This might take a few seconds depending on the file size.</p>

<h2 style= 'color: black;'>3. View results:</h2>
<p style= 'color: black;'>After processing, the app will display the predicted genre.</p>
""", unsafe_allow_html=True)

# URL and file uploader
url = 'https://musicgc-k47xyyahgq-ew.a.run.app'
audio_file_buffer = st.file_uploader('')

if audio_file_buffer is not None:
    res = requests.post(url + "/upload_music", files={'mus': audio_file_buffer})

    if res.status_code == 200:
        result = res.content
        st.write(result)
    else:
        st.markdown("**Oops**, something went wrong :sweat: Please try again.")
        print(res.status_code, res.content)

    st.info("You have uploaded file info as following:")
    st.text(f"Filename: {audio_file_buffer.name}")
    st.text(f"File size: {audio_file_buffer.size} bytes")
    
    
st.sidebar.header("Supported Genres")  # Set the title in the sidebar

supported_genres = {
    "Blues": "Blues is a genre of music that originated in the African American communities of the United States. It typically features melancholy lyrics and a distinctive musical style.",
    "Classical": "Classical music is a genre that encompasses a broad range of music from the Western tradition. It often features complex compositions and instrumental arrangements.",
    "Country": "Country music is a genre that originated in the Southern United States. It often highlights themes of rural life, love, and heartache.",
    "Disco": "Disco is a genre of dance music that was popular in the 1970s. It is characterized by a strong beat and electronic instrumentation.",
    "Hip Hop": "Hip hop is a genre of music that emerged in the Bronx, New York City, during the 1970s. It is characterized by rhythmic speech over a beat.",
    "Jazz": "Jazz is a genre of music that originated in the African American communities of New Orleans. It features improvisation and swing rhythms.",
    "Metal": "Metal is a genre of music that is characterized by its loud, aggressive sound. It often features distorted guitars and powerful vocals.",
    "Pop": "Pop music is a genre that encompasses popular music from various styles. It is often catchy and appeals to a broad audience.",
    "Reggae": "Reggae is a genre of music that originated in Jamaica. It is characterized by its offbeat rhythms and socially conscious lyrics.",
    "Rock": "Rock music is a genre that emerged in the 1950s and has since evolved into various subgenres. It typically features electric guitars and strong rhythms."
}

if 'genre_status' not in st.session_state:
    st.session_state['genre_status'] = {genre: False for genre in supported_genres}

for genre in supported_genres:
    button_id = f"{genre}_button"
    
    if st.sidebar.button(genre, key=button_id):    
        st.session_state['genre_status'][genre] = not st.session_state['genre_status'][genre]
        
        if st.session_state['genre_status'][genre]:
            st.write(supported_genres[genre])
            
            
            
      