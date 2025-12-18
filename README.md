# Smart Note - AI-Powered Text Summarization 📝🤖

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)  
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Spaces-orange)](https://huggingface.co/spaces/zahraa12355/smart_note)

Welcome to **Smart Note**, a lightweight and effective AI-powered text summarization app built with **Gradio**!  
Quickly digest meeting notes, articles, or any long text with concise summaries.

---
## 🔹 Project Overview

Smart Meeting Notes is an AI-powered application that transforms meeting transcripts into concise summaries. Built using large language models (LLMs), it aims to help professionals quickly grasp key points from meetings without reading through lengthy transcripts.

## 🔹 Features

- AI-driven text summarization
- User-friendly Gradio interface
- Lightweight and fast
- Option to run locally or deploy on Hugging Face Spaces

---

## 🔹 Project Structure

- `app.py` - Runs the Gradio interface for text summarization  
- `requirements.txt` - Lists all Python dependencies for the project  
- `README.md` - Contains project description and instructions  

  ---

# Smart Note - AI-Powered Text Summarization 📝🤖

Smart Note is a smart meeting notes summarization app powered by **Hugging Face** models and **Gradio**.  
It quickly converts long text—like meeting notes or articles—into concise summaries.

---
## 🔹 Run Locally

Follow these steps to run Smart Note on your local machine:

1. **Clone the repository:**

```bash
   git clone https://github.com/zaralrubaie/-smart-meeting-notes-by-LLM-.git
   cd smart_note
```
2. Install dependencies:
 ```bash
pip install -r requirements.txt
```
## 🔹 Usage

1. Open the application in your browser.
2. Upload a meeting transcript (in text format).
3. Click "Summarize" to generate a concise summary of the meeting.

## 🔹 Live Demo

Try the app live here:  
[Smart Note on Hugging Face Spaces](https://huggingface.co/spaces/zahraa12355/smart_note)
   
## 🔹 Limitations

- Summarization performance may decrease for long or complex texts, and inference time increases with input length.
- Running the model locally on CPU-only hardware can be slow due to limited memory and lack of GPU acceleration.
- This project uses a pretrained model for inference only; fine-tuning or training large transformer models locally is computationally expensive and not supported.
- When deployed on Hugging Face Spaces, inference time may vary depending on server load and network latency.
  
  ##  🔹License
This project is licensed under the MIT License.

