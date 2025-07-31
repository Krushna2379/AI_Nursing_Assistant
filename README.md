  AI-Powered Virtual Nurse Assistant
An AI-powered healthcare assistant built using Flask (Python), OpenAI API, and Bootstrap frontend.
It can chat with patients, track symptoms, give reminders, and provide health guidance.


Features
-AI-powered responses (using GPT model)
-Symptom tracking (saves symptoms in a JSON file)
-Medication reminders
-Interactive Bootstrap-based chat UI
-Voice input support 🎤 (Speech-to-Text)
-Persistent data storage (JSON)
 
Project Structure
ai_virtual_nurse/
│── app.py                 # Flask backend
│── nlp_engine.py          # AI response logic (OpenAI API)
│── symptom_tracker.py     # Symptom & reminder tracking
│── database.json          # Stores reminders & symptoms
│── templates/
│   └── index.html         # Frontend UI
│── static/
│   ├── style.css          # Chat UI styles
│   └── script.js          # Chat logic + voice input
│── requirements.txt       # Python dependencies
│── README.md              # Documentation

Setup Instructions 
-Clone or Download Project 
-Install Required Packages
-Get Your OpenAI API Key
-Set API Key in Your System
-Run the App

Usage
-Type or speak your message → The nurse replies.
-It tracks symptoms like fever, headache, cough, pain.
-Shows reminders in the right panel.

Requirements
-Flask==2.3.2
-openai>=1.0.0
