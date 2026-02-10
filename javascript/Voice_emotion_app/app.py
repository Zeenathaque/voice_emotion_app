import streamlit as st
import librosa
import numpy as np
import pandas as pd
import plotly.express as px
import whisper
from transformers import pipeline
import tempfile
import os

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Voice Sentiment Analysis Dashboard",
    layout="wide"
)

st.title("Voice Emotion & Sentiment Analysis Dashboard")

st.write(
    "This application analyzes voice input, detects emotions over time, "
    "and visualizes emotion changes with precise timestamps."
)

# -----------------------------
# Load Models (Cached)
# -----------------------------
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

@st.cache_resource
def load_emotion_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )

whisper_model = load_whisper_model()
emotion_model = load_emotion_model()

# -----------------------------
# Helper Functions
# -----------------------------
def split_audio(file_path, chunk_duration=5):
    """
    Splits audio into fixed-length chunks
    """
    audio, sr = librosa.load(file_path, sr=16000)
    chunk_samples = chunk_duration * sr

    chunks = []
    for start in range(0, len(audio), chunk_samples):
        end = start + chunk_samples
        chunk = audio[start:end]
        start_time = start / sr
        chunks.append((chunk, start_time))

    return chunks, sr


def transcribe_chunk(chunk, sr):
    """
    Transcribes a single audio chunk
    """
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        librosa.output.write_wav(temp_audio.name, chunk, sr)
        temp_path = temp_audio.name

    result = whisper_model.transcribe(temp_path, fp16=False)
    os.remove(temp_path)

    return result["text"].strip()


def analyze_emotions(chunks, sr):
    """
    Runs emotion detection on each chunk
    """
    records = []

    for chunk, start_time in chunks:
        text = transcribe_chunk(chunk, sr)

        if text == "":
            continue

        emotions = emotion_model(text)[0]
        top_emotion = max(emotions, key=lambda x: x["score"])

        records.append({
            "Minute": int(start_time // 60),
            "Second": int(start_time % 60),
            "Timestamp": f"{int(start_time//60)}:{int(start_time%60):02d}",
            "Text": text,
            "Emotion": top_emotion["label"],
            "Confidence": round(top_emotion["score"], 3)
        })

    return pd.DataFrame(records)

# -----------------------------
# UI: File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload an audio file (.wav or .mp3)",
    type=["wav", "mp3"]
)

if uploaded_file is not None:
    with st.spinner("Processing audio. Please wait..."):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            audio_path = temp_file.name

        chunks, sr = split_audio(audio_path)
        df = analyze_emotions(chunks, sr)

        os.remove(audio_path)

    if df.empty:
        st.warning("No speech detected in the audio.")
    else:
        st.success("Analysis completed successfully.")

        # -----------------------------
        # Display Table
        # -----------------------------
        st.subheader("Emotion Detection with Timestamps")
        st.dataframe(df, use_container_width=True)

        # -----------------------------
        # Visualization
        # -----------------------------
        st.subheader("Emotion Changes Over Time")

        fig = px.scatter(
            df,
            x="Timestamp",
            y="Confidence",
            color="Emotion",
            size="Confidence",
            title="Emotion Timeline",
            hover_data=["Text"]
        )

        st.plotly_chart(fig, use_container_width=True)

        # -----------------------------
        # Emotion Summary
        # -----------------------------
        st.subheader("Overall Emotion Distribution")
        summary = df["Emotion"].value_counts().reset_index()
        summary.columns = ["Emotion", "Count"]

        pie_fig = px.pie(
            summary,
            names="Emotion",
            values="Count",
            title="Emotion Distribution"
        )

        st.plotly_chart(pie_fig, use_container_width=True)