import json
import os

DB_FILE = "database.json"

# Create DB file if not exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"symptoms": [], "reminders": ["Take medicine at 9 AM"]}, f)

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def track_symptom(message):
    data = read_db()
    if any(word in message.lower() for word in ["fever", "pain", "cough", "headache"]):
        data["symptoms"].append(message)
        write_db(data)
        return "I have noted your symptom. Please take care."
    return None

def get_reminders():
    data = read_db()
    return data["reminders"]
