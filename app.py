from flask import Flask, render_template, request, jsonify
from nlp_engine import get_ai_response
from symptom_tracker import track_symptom, get_reminders

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Get AI response
    ai_reply = get_ai_response(user_message)

    # Track symptoms if detected
    symptom_reply = track_symptom(user_message)
    if symptom_reply:
        ai_reply += f" {symptom_reply}"

    # Get reminders
    reminders = get_reminders()
    if reminders:
        ai_reply += f"\n🔔 Reminders: {', '.join(reminders)}"

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
