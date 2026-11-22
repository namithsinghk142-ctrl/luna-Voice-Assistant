# 🌙 Luna AI — Voice Assistant

A futuristic AI voice assistant built using Python, Flask, HTML, CSS, and JavaScript. Luna features voice recognition, smart commands, YouTube music playback, in-session memory, arithmetic calculation, real-time responses, and a cinematic sci-fi interface.

---

## 🚀 Features

### 🎙️ Voice & Audio
- **Voice Recognition:** Client-side speech-to-text powered by the browser Web Speech API (`webkitSpeechRecognition`).
- **AI Voice Responses:** Natural text-to-speech output using the browser Speech Synthesis API (`speechSynthesis`).
- **Interactive Mic Interface:** Glowing, pulsing microphone button with dynamic listening states.

### 🌐 Smart Integrations
- **Google Search:** Instantly opens Google search queries in your default browser (e.g., *"search quantum computing"*).
- **YouTube Music Playback:** Automates YouTube queries and plays music tracks directly in your browser (e.g., *"play mockingbird"*).

### 🧠 Intelligence & Memory
- **In-Session Memory:** Remembers your name and mood during the active session (e.g., *"my name is Namith"*, *"what is my name"*).
- **Smart Calculator:** Evaluates mathematical expressions using spoken words or numbers (e.g., *"what is 45 x 8"*, *"12 plus 5"*).
- **Conversational Responses:** Built-in replies for greetings, motivation, programming thoughts, jokes, and chit-chat.
- **Recommendations:** Curated suggestions for movies, video games, and trending music.
- **Real-Time Clock & Date:** Real-time client-side clock and server-synchronized date/time reports.

### 🌌 Interface & Architecture
- **Futuristic Sci-Fi UI:** Dark-mode radial gradients, animated particles, glowing neon orbs, and glassmorphism cards.
- **Fast Flask Backend:** Lightweight Python Flask API handling commands with Flask-CORS enabled.
- **Zero External API Costs:** Runs out of the box with standard Python libraries and Web Speech APIs — no paid third-party API keys required.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask, Flask-CORS
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **APIs & Web Standards:** Browser Web Speech API (`webkitSpeechRecognition` & `speechSynthesis`)
- **OS Integration:** Python `webbrowser` module

---

## 📸 Architecture & Workflow

```
[ User Microphone ]
        │
        ▼ (Speech-to-Text via Web Speech API)
[ Browser Frontend (index.html) ]
        │
        ▼ POST /command (JSON payload)
[ Flask Backend (app.py) ]
        │
        ├─► Pattern Matching & Logic (Greetings, Jokes, Recommendations)
        ├─► Math Expression Parser (Calculator)
        ├─► In-Memory Session Store (Name, Mood)
        └─► System Browser Launcher (Google Search, YouTube)
        │
        ▼ JSON Response {"response": "..."}
[ Browser Frontend (index.html) ]
        │
        ▼ (Text-to-Speech via speechSynthesis)
[ Audio Output & Chat Display ]
```

---

## ▶️ Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system.
- A modern Chromium-based browser (**Google Chrome**, **Microsoft Edge**, **Brave**, or **Opera**) with microphone permissions enabled for Web Speech API support.

### 1. Clone the repository
```bash
git clone https://github.com/namithsinghk142-ctrl/luna-Voice-Assistant.git
```

### 2. Navigate to the project directory
```bash
cd luna-Voice-Assistant
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```
*(Alternatively: `pip install flask flask-cors`)*

### 4. Run the application
```bash
python app.py
```

### 5. Open in your browser
Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

> **Note on Permissions:** When you first click the microphone button, grant the browser permission to access your microphone.

---

## 🎙️ Example Voice & Text Commands

| Category | Example Commands | Behavior |
| :--- | :--- | :--- |
| **Greetings** | *"Hello"*, *"Hey Luna"*, *"Good morning"* | Friendly personalized greeting |
| **Identity** | *"Who are you"*, *"What is your name"* | Introduces Luna AI |
| **Search** | *"Search gaming laptops"*, *"Google"* | Opens Google search in default browser |
| **Music** | *"Play mockingbird"*, *"Play lo-fi hip hop"*, *"YouTube"* | Opens YouTube search query in default browser |
| **Calculator** | *"What is 45 x 8"*, *"12 plus 5"*, *"100 divided by 4"* | Calculates and speaks the result |
| **Memory** | *"My name is Namith"*, *"What is my name"* | Stores and recalls name during active session |
| **Mood** | *"I am sad"*, *"I'm happy"* | Empathetic conversational responses |
| **Jokes** | *"Tell me a joke"* | Shares a programming or tech joke |
| **Suggestions**| *"Movie"*, *"Game"*, *"Suggest music"* | Recommends movies, games, or songs |
| **Time & Date**| *"What time is it"*, *"What is the date"* | Reports current time or date |
| **Coding** | *"Coding"*, *"Motivate me"* | Motivational and coding tips |

---

## 🔍 Feature Implementation Status

| Feature | Implementation Status | Notes |
| :--- | :---: | :--- |
| **Voice Recognition** | ✅ Fully Implemented | Client-side via Web Speech API |
| **Text-to-Speech** | ✅ Fully Implemented | Client-side via SpeechSynthesis |
| **Google Search** | ✅ Fully Implemented | Launches host browser via `webbrowser.open` |
| **YouTube Playback** | ✅ Fully Implemented | Launches YouTube search query in host browser |
| **Calculator** | ✅ Fully Implemented | Handles arithmetic operations with regex and eval |
| **Jokes & Chit-chat** | ✅ Fully Implemented | Curated humorous and conversational responses |
| **Movie & Game Tips** | ✅ Fully Implemented | Built-in recommendation lists |
| **Real-time Clock** | ✅ Fully Implemented | Frontend live clock and backend time inquiry |
| **Memory Storage** | ⚠️ In-Session | Active during runtime; resets on server restart |
| **Hands-free Wake Word** | ⏳ Planned | Currently requires clicking mic before speaking |
| **Mobile Responsive UI**| ⏳ Planned | Optimized for desktop screen dimensions |

---

## 🌌 Future Improvements

- [ ] Persistent database storage for user memory (SQLite / JSON).
- [ ] Hands-free continuous wake-word detection (e.g. Porcupine / openWakeWord).
- [ ] LLM API integration (e.g., Gemini API / OpenAI API) for open-ended conversation.
- [ ] Real-time live Weather API integration (OpenWeatherMap).
- [ ] Spotify Web Playback API integration.
- [ ] Mobile-responsive adaptive UI layouts.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
