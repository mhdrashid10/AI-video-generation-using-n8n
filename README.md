# AI-video-generation-using-n8n

## Overview
This project implements a fully automated AI-powered video generation pipeline that converts a single topic input into a YouTube-ready MP4 video using a webhook trigger.

The system integrates multiple AI and media services to generate script, voiceover, visuals, and final video composition without manual editing.

⚙️ Architecture

Webhook Trigger
   ↓
Groq (LLM) – Script Generation
   ↓
Microsoft Edge TTS – Voiceover Generation
   ↓
Pexels API – Stock Video Retrieval
   ↓
Python (MoviePy) – Video & Audio Composition
   ↓
Read File
   ↓
Respond to Webhook (Returns MP4)

🛠️ Technologies Used

n8n (workflow orchestration)

Groq API (LLM script generation)

Microsoft Edge TTS (neural voice synthesis)

Pexels API (stock video retrieval)

Python 3.13

MoviePy (video processing)

🔁 How It Works

A topic is sent via webhook.

Groq generates a clean narration script.

Edge TTS converts the script into an audio file.

Pexels API fetches relevant stock footage.

Python (MoviePy) synchronizes video duration with audio.

Final MP4 file is rendered automatically.

The video is returned as the webhook response.

🧪 Sample Webhook Input
{
  "topic": "Cinematic professional camera and filmmaking equipment in action"
}

🔐 Setup Instructions

Before running the workflow, replace the placeholders with your own API keys:

YOUR_GROQ_API_KEY

YOUR_PEXELS_API_KEY

Do NOT commit real API keys to version control.

▶️ Running the Project

Import workflow.json into n8n.

Install Python dependencies:

pip install moviepy requests


Ensure Edge TTS is installed.

Trigger the webhook with a topic.

The system will return a generated MP4 video.

🎯 Challenges Faced

Managing cross-service API integration

Synchronizing video duration with generated voiceover

Handling file system security restrictions in n8n

Ensuring full end-to-end automation

🚀 Future Improvements

Scene-based semantic visual matching

Automatic subtitle generation

Auto-thumbnail generation

Direct YouTube upload integration
