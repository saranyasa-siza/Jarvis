# 🤖 JARVIS - Virtual Assistant

## 📌 About the Project

JARVIS is a voice-activated virtual assistant built with Python. It listens for spoken commands, responds with text-to-speech, and performs tasks like opening websites, playing music, and reading the latest news headlines.

## ✨ Features

- 🎙️ Voice recognition using Google Web Speech API
- 🔊 Text-to-speech responses via `pyttsx3`
- 🌐 Opens websites — Google, YouTube, LinkedIn, GitHub
- 🎵 Plays songs from a custom music library
- 📰 Fetches top BBC News headlines via NewsAPI
- 🤖 Gemini AI integration (via `google.genai`)

## 🛠️ Tech Stack

- Python
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `requests`
- `google-generativeai`
- `python-dotenv`

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install speechrecognition pyttsx3 requests google-generativeai python-dotenv
   ```
3. Create a `.env` file and add your API keys:
   ```
   GEMINI_API_KEY=<your_gemini_api_key>
   ```
4. Run the assistant:
   ```bash
   python main.py
   ```

## 🗣️ Voice Commands

| Command | Action |
|---|---|
| `open google` | Opens Google |
| `open youtube` | Opens YouTube |
| `open linkedin` | Opens LinkedIn |
| `open github` | Opens GitHub |
| `play <song>` | Plays a song from the music library |
| `news` | Reads top 5 BBC News headlines |

## 📁 Project Structure

```
Jarvis/
├── main.py           # Core assistant logic
├── client.py         # Gemini AI client
├── musicLibrary.py   # Song name to URL mapping
├── voice_test.py     # Voice recognition testing
└── .env              # API keys (not committed)
```
done