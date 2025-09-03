# 🎙️ Voice-Controlled AI Assistant (with LLaMA)

A voice-activated personal assistant built in Python that integrates **Meta LLaMA-3** with **speech recognition** and **text-to-speech**.  
It listens for the wake word **“King”**, performs actions like playing YouTube videos, telling the time, or chatting with LLaMA, and stops when you say **“thanks stop”**.

---

## 🚀 Features
- **Voice Recognition**: Uses Google Speech Recognition to capture commands.
- **Text-to-Speech**: Natural voice output using `pyttsx3`.
- **AI-Powered Responses**: Integrates with **Meta LLaMA-3** (via `llama-cpp-python`).
- **YouTube Integration**: Plays requested songs or videos with `pywhatkit`.
- **Utilities**: Tells current time, cracks jokes, answers general queries.
- **Wake Word**: Responds only when you say **“King”**.
- **Exit Command**: Say **“thanks stop”** to gracefully quit.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [llama-cpp-python](https://pypi.org/project/llama-cpp-python/)

---

## 📂 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Abh1nav-ai/Speech_Recognition.git
cd Speech_Recognition


Note

.gitignore excludes venv/, .idea/, and large .gguf model files.

You must download the LLaMA model separately (not included due to size).
