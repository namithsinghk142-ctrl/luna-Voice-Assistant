from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import webbrowser
import urllib.parse
import random
import datetime
import re
import time

app = Flask(__name__)
CORS(app)

# 🧠 MEMORY
user_memory = {
    "name": None,
    "mood": None
}

# 🌐 HOME PAGE
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# 🎤 MAIN COMMAND SYSTEM
@app.route("/command", methods=["POST"])
def command():

    data = request.get_json()

    cmd = data.get("text", "").lower().strip()

    print("Received:", cmd)

    response = "I don't understand that yet."

    # ⏰ CURRENT TIME
    now = datetime.datetime.now()

    # 👋 GREETINGS
    greetings = [
        "Hello, how can I help you?",
        "Hi, what can I do for you?",
        "Hey there.",
        "I'm listening.",
        "Welcome back."
    ]

    if any(word in cmd for word in ["hello", "hi", "hey"]):

        if user_memory["name"]:
            response = f"Hello {user_memory['name']}, how can I help you?"
        else:
            response = random.choice(greetings)

    # 🌙 WAKE WORD
    elif "luna" in cmd:
        response = "Yes? I'm listening."

    # 🧠 REMEMBER NAME
    elif "my name is" in cmd:

        name = cmd.replace("my name is", "").strip().title()

        user_memory["name"] = name

        response = f"Nice to meet you, {name}. I'll remember that."

    # 🧠 RECALL NAME
    elif "what is my name" in cmd:

        if user_memory["name"]:
            response = f"Your name is {user_memory['name']}."
        else:
            response = "I don't know your name yet."

    # 😄 MOOD
    elif "i am sad" in cmd or "i'm sad" in cmd:

        user_memory["mood"] = "sad"

        sad_replies = [
            "I'm here for you.",
            "Things will get better.",
            "Take a small break and breathe.",
            "Maybe some music would help."
        ]

        response = random.choice(sad_replies)

    elif "i am happy" in cmd or "i'm happy" in cmd:

        user_memory["mood"] = "happy"

        happy_replies = [
            "That's amazing.",
            "I like hearing that.",
            "Keep the good energy going.",
            "Nice."
        ]

        response = random.choice(happy_replies)

    # ⏰ TIME
    elif "time" in cmd:
        response = "The time is " + now.strftime("%I:%M %p")

    # 📅 DATE
    elif "date" in cmd:
        response = "Today is " + now.strftime("%A, %d %B %Y")

    # ☀️ GOOD MORNING
    elif "good morning" in cmd:
        response = "Good morning. Hope you have a great day."

    # 🌙 GOOD NIGHT
    elif "good night" in cmd:
        response = "Good night. Sleep well."

    # ☁️ WEATHER
    elif "weather" in cmd:

        weather_responses = [
            "It looks like a cool day outside.",
            "The weather seems pleasant today.",
            "Probably a good day to code.",
            "I think the weather is decent today.",
            "Looks like nice weather for music and coding."
        ]

        response = random.choice(weather_responses)

    # 🧮 CALCULATOR
    elif re.search(r'\d', cmd):

        try:

            expression = cmd

            expression = re.sub(r'(?<=\d)\s*x\s*(?=\d)', '*', expression)

            expression = expression.replace("plus", "+")
            expression = expression.replace("minus", "-")
            expression = expression.replace("times", "*")
            expression = expression.replace("multiplied by", "*")
            expression = expression.replace("divided by", "/")

            expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)

            result = eval(expression)

            response = f"The answer is {result}"

        except:
            response = "I couldn't calculate that."

    # 🌍 SEARCH
    elif "search" in cmd:

        query = cmd.replace("search", "").strip()

        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"

        webbrowser.open(url)

        response = f"Searching for {query}"

    # 🌍 GOOGLE
    elif "google" in cmd:

        webbrowser.open("https://google.com")

        response = "Opening Google"

    # ▶️ YOUTUBE
    elif "youtube" in cmd:

        webbrowser.open("https://youtube.com")

        response = "Opening YouTube"

    # 🎵 SMART MUSIC PLAYER
    elif "play" in cmd:

        song = cmd

        remove_words = [
            "can you",
            "please",
            "play",
            "me",
            "a",
            "the",
            "song",
            "music",
            "video"
        ]

        for word in remove_words:
            song = song.replace(word, "")

        song = song.strip()

        if song == "":

            response = "What would you like me to play?"

        else:

            query = urllib.parse.quote(song)

            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"

            webbrowser.open(url)

            responses = [
                f"Playing {song}",
                f"Sure, playing {song}",
                f"Opening {song} on YouTube",
                f"I found {song} for you"
            ]

            response = random.choice(responses)

    # 😂 JOKES
    elif "joke" in cmd:

        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "I would tell you a coding joke, but it has too many errors.",
            "Why was the computer cold? It left its Windows open.",
            "Debugging is like being the detective in a crime movie where you are also the murderer.",
            "Why did the Python programmer wear glasses? Because they couldn't C."
        ]

        response = random.choice(jokes)

    # 🎬 MOVIES
    elif "movie" in cmd:

        movies = [
            "You should watch Interstellar.",
            "Try Inception.",
            "Maybe watch Spider-Man Into the Spider-Verse.",
            "I recommend The Dark Knight.",
            "Try watching Your Name."
        ]

        response = random.choice(movies)

    # 🎮 GAMES
    elif "game" in cmd:

        games = [
            "Minecraft is always fun.",
            "You should try Valorant.",
            "Maybe play Elden Ring.",
            "Try Hollow Knight.",
            "You could play GTA V."
        ]

        response = random.choice(games)

    # 🎧 MUSIC SUGGESTIONS
    elif "suggest music" in cmd or "music suggestion" in cmd:

        music = [
            "Try listening to Blinding Lights.",
            "Maybe some lo-fi music.",
            "You should listen to Mockingbird.",
            "Try Starboy.",
            "Maybe listen to Arctic Monkeys."
        ]

        response = random.choice(music)

    # 😴 BORED
    elif "bored" in cmd:

        bored_replies = [
            "You should build another cool project.",
            "Maybe listen to some music.",
            "Try watching something interesting.",
            "You could learn a new tech skill today.",
            "Maybe play a game.",
            "Try coding something random."
        ]

        response = random.choice(bored_replies)

    # ⚽ MESSI
    elif "messi" in cmd:
        response = "Lionel Messi is considered one of the greatest football players ever."

    # 🤖 WHO ARE YOU
    elif "who are you" in cmd or "your name" in cmd:
        response = "I am Luna, your futuristic AI voice assistant."

    # ❤️ THANKS
    elif "thank" in cmd:
        response = "You're welcome."

    # 💻 CODING
    elif "coding" in cmd or "programming" in cmd:

        coding = [
            "Consistency matters more than motivation.",
            "Projects teach faster than tutorials.",
            "Debugging is part of programming.",
            "You're improving every time you code."
        ]

        response = random.choice(coding)

    # 🚀 MOTIVATION
    elif "motivate me" in cmd:

        motivation = [
            "Small progress every day becomes huge progress.",
            "Keep building.",
            "You're already ahead of many beginners.",
            "The best projects come from experimenting."
        ]

        response = random.choice(motivation)

    # 🎨 COMPLIMENTS
    elif "am i smart" in cmd:
        response = "You're clearly learning fast."

    # 🤖 FALLBACK
    else:

        smart_replies = [
            "Interesting.",
            "I'm learning more every day.",
            "That sounds cool.",
            "Can you explain more?",
            "I like talking with you.",
            "That's actually interesting.",
            "Maybe I’ll understand that better in the future.",
            "You ask good questions.",
            "Tell me more about that.",
            "I think that's worth exploring."
        ]

        response = random.choice(smart_replies)

    # ⏳ FAKE THINKING
    time.sleep(1)

    return jsonify({"response": response})

# 🚀 RUN APP
if __name__ == "__main__":
    app.run(debug=True)