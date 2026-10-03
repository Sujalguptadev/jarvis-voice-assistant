# Jarvis: AI-Powered Voice Assistant

A Python voice assistant for Windows with wake-word activation, system control, live news, and conversational AI.

## Features
- Wake word activation ("Jarvis")
- Opens websites and Windows apps by voice
- Plays songs from a custom music library
- Reads live top headlines (NewsAPI)
- Answers general questions using OpenAI (GPT-4o-mini) with short-term memory
- Text-to-speech via Windows SAPI

## Tech Stack
Python, SpeechRecognition, OpenAI API, NewsAPI, pywin32, Requests

## Setup
```bash
git clone https://github.com/Sujalguptadev/jarvis-voice-assistant.git
cd jarvis-voice-assistant
pip install -r requirements.txt
```

Copy `credentials.example.py` to `credentials.py` and add your keys:
```python
newsapi = "YOUR_NEWSAPI_KEY"
openai_key = "YOUR_OPENAI_API_KEY"
```

Run:
```bash
python jarvis.py
```

## Usage
1. Say **"Jarvis"**
2. Wait for the response, then say a command:
   - "Open YouTube"
   - "Open Notepad"
   - "Play <song name>"
   - "News"
   - Anything else goes to the AI, e.g. "What is recursion?"

## How It Works
Wake word -> command recognition -> keyword routing (sites, apps, music, news) -> fallback to OpenAI for everything else.

## Notes
- Windows only (uses SAPI and `os.startfile`/`start`).
- API keys are never committed. Use `credentials.py` locally.

## Future Improvements
- Weather and reminders
- Tool-calling / agent features
- Cross-platform TTS
