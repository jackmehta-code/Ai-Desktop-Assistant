import customtkinter as ctk
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import threading
import os

# Setup appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Text to speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = r.listen(source, timeout=5)
            command = r.recognize_google(audio)
            return command.lower()
        except:
            return "Sorry, I didn't catch that."

# App opener using Windows shell commands
def open_app(command):
    apps = {
        'notepad': 'start notepad',
        'calculator': 'start calc',
        'calc': 'start calc',
        'chrome': 'start chrome',
        'command prompt': 'start cmd',
        'cmd': 'start cmd',
        'control panel': 'start control',
        'paint': 'start mspaint',
        'file explorer': 'start explorer',
        'explorer': 'start explorer',
        'task manager': 'start taskmgr'
    }
    for key, cmd in apps.items():
        if key in command:
            os.system(cmd)
            return f"Opening {key.title()}..."
    return None

# Core logic
def respond_to_command(command):
    command = command.lower()

    if 'time' in command:
        return f"The current time is {datetime.datetime.now():%I:%M %p}"

    elif 'travel to' in command:
        destination = command.replace('travel to', '').strip()
        try:
            summary = wikipedia.summary(destination, sentences=2)
            pywhatkit.search(f"{destination} travel guide")
            return f"Travel info for {destination}:\n{summary}"
        except:
            pywhatkit.search(f"{destination} travel guide")
            return f"Opened travel info for {destination} in browser."

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        try:
            return wikipedia.summary(person, sentences=1)
        except:
            return "I couldn't find information."

    elif 'search' in command or 'what is' in command or 'how to' in command:
        topic = command.replace('search', '').replace('what is', '').replace('how to', '').strip()
        pywhatkit.search(topic)
        return f"Searching for '{topic}'..."

    elif 'open youtube' in command:
        pywhatkit.playonyt("YouTube")
        return "Opening YouTube..."

    elif 'open google' in command:
        pywhatkit.search("Google")
        return "Opening Google..."

    elif 'exit' in command or 'bye' in command:
        speak("Goodbye!")
        root.destroy()
        return "Exiting..."

    app_response = open_app(command)
    if app_response:
        return app_response

    return "Sorry, I don't understand that."

# GUI setup
root = ctk.CTk()
root.title("DeskBuddy - AI Assistant")
root.geometry("600x550")

output_box = ctk.CTkTextbox(root, width=550, height=370, font=("Arial", 14), wrap="word")
output_box.pack(pady=20)

input_field = ctk.CTkEntry(root, placeholder_text="Type your command here", width=400, font=("Arial", 14))
input_field.pack(pady=5)

def handle_command(cmd):
    response = respond_to_command(cmd)
    output_box.insert("end", f"You: {cmd}\nBuddy: {response}\n\n")
    output_box.see("end")
    speak(response)

def on_send():
    cmd = input_field.get().strip()
    input_field.delete(0, 'end')
    if cmd:
        threading.Thread(target=handle_command, args=(cmd,), daemon=True).start()

def on_speak():
    threading.Thread(target=lambda: handle_command(take_voice_input()), daemon=True).start()

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="🎤 Speak", command=on_speak).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="➡️ Send", command=on_send).grid(row=0, column=1, padx=10)
ctk.CTkButton(btn_frame, text="❌ Exit", command=root.destroy).grid(row=0, column=2, padx=10)

root.mainloop()
