
# 🤖 DeskBuddy – Free AI Desktop Assistant

DeskBuddy is a voice- and text-enabled AI assistant for Windows, built with Python. It performs tasks like answering factual questions, opening desktop apps, providing travel info, and searching the web — all for free!

---

## ✨ Features

✅ Voice & Text Command Input  
✅ Wikipedia Integration (for Q&A & Travel Info)  
✅ Web Searching (via pywhatkit, no OpenAI/paid APIs)  
✅ Opens Windows Apps (Notepad, Calculator, etc.)  
✅ Easy GUI with `customtkinter`  
✅ Works 100% Offline (except search)

---

## 📸 Screenshots

| Chat UI | Voice Input |
|--------|-------------|
| ![Chat UI](assets/chat_ui.png) | ![Voice Input](assets/speak_ui.png) |

---

## 🛠️ Installation

1. 🐍 Install Python (3.10+ recommended): https://www.python.org/downloads/

2. 📦 Install dependencies:
```bash
pip install -r requirements.txt
```

3. ▶️ Run the app:
```bash
python deskbuddy.py
```

---

## 🗣️ Sample Commands

- `"what is artificial intelligence"`
- `"who is Elon Musk"`
- `"open notepad"`
- `"travel to Goa"`
- `"search Python decorators"`
- `"open calculator"`

---

## 📂 File List

| File | Description |
|------|-------------|
| `deskbuddy.py` | Main application script |
| `requirements.txt` | Required packages |
| `assets/` | Screenshots and UI images |

---

## 📃 License

MIT License. Free for personal and academic use.

---

## 🙌 Credits

- Developed using Python & customtkinter  
- Wikipedia, pywhatkit for info & search  
- Speech Recognition & pyttsx3 for offline voice input/output  
