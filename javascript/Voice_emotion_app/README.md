# Voice Emotion & Sentiment Analysis Dashboard

## Overview
This project is a voice-based emotion and sentiment analysis application developed as part of a Python Development Internship assignment. The application accepts audio input, analyzes the speech over time, detects emotional changes, and presents the results through an interactive dashboard.

The system identifies emotions at different timestamps (minute and second) and visualizes emotion transitions using charts and tables.

---

## Features
- Upload audio files in WAV or MP3 format
- Automatic speech-to-text conversion using a pretrained model
- Emotion detection for each audio segment
- Timestamp-based emotion tracking (minute and second)
- Interactive dashboard with:
  - Emotion timeline
  - Confidence scores
  - Emotion distribution charts
- Fully deployed and accessible via a public URL

---

## Technology Stack
- **Python**
- **Streamlit** – Web application framework
- **Whisper** – Speech-to-text conversion
- **Hugging Face Transformers** – Emotion classification
- **Librosa** – Audio processing
- **Plotly** – Data visualization
- **Pandas & NumPy** – Data handling

---

## System Architecture
1. Audio input is uploaded by the user
2. Audio is split into fixed-length segments
3. Each segment is transcribed into text
4. Emotion analysis is performed on transcribed text
5. Emotions are mapped with timestamps
6. Results are visualized on an interactive dashboard

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps
```bash
pip install -r requirements.txt