import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

# Page Config
st.set_page_config(page_title="Growth Mindset", page_icon="🚀", layout="wide")

# Custom CSS for Full Background Gradient
st.markdown("""
    <style>
        html, body, .appview-container .main .block-container {
            background:linear-gradient(135deg, #FF0000, #0000FF);
            margin: 0;
            padding: 20px;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        h1, h2 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("🌱 Welcome to the Growth Mindset Website")

# Information Paragraph
st.write("""
Speech-to-text technology converts spoken language into written text using advanced algorithms. 
It helps improve accessibility, allows hands-free control, and boosts productivity by transforming audio inputs into accurate text.
""")

# Upload Audio Section
st.subheader("🎧 Upload Your Audio")
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

# Convert Speech to Text Section
st.subheader("🔊 Convert Speech to Text")
if audio_file:
    audio_format = audio_file.name.split(".")[-1]
    audio_path = f"temp_audio.{audio_format}"
    with open(audio_path, "wb") as f:
        f.write(audio_file.read())

    # Convert MP3/M4A to WAV (if needed)
    if audio_format in ["mp3", "m4a"]:
        audio = AudioSegment.from_file(audio_path, format=audio_format)
        audio.export("converted_audio.wav", format="wav")
        audio_path = "converted_audio.wav"

    if st.button("🔊 Convert Audio"):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            st.info("🎉 Audio uploaded successfully. Converting to text...")
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            st.success("✅ Audio converted successfully!")
            st.write(f"**{text}**")
        except sr.UnknownValueError:
            st.error("❌ Could not understand the audio.")
        except sr.RequestError:
            st.error("⚠️ Error processing speech recognition.")
else:
    st.warning("🔊 Please upload an audio file first.")
