<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  AI Virtual Nurse - Documentation
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container my-5">
  <div class="card shadow-lg p-4">
    <h1 class="text-primary">🩺 AI-Powered Virtual Nurse Assistant</h1>
    <p>An AI-powered healthcare assistant built using <b>Flask</b>, <b>OpenAI API</b>, and <b>Bootstrap</b>.</p>

🚀 Features
    
      ✅ AI-powered responses using GPT model
      ✅ Symptom tracking (JSON storage)
      ✅ Medication reminders
      ✅ Interactive Bootstrap chat UI
      ✅ Voice input support 🎤
      ✅ Persistent data storage
    
📂 Project Structure
    <pre>
ai_virtual_nurse/
│── app.py
│── nlp_engine.py
│── symptom_tracker.py
│── database.json
│── templates/index.html
│── static/style.css
│── static/script.js
│── requirements.txt
│── README.md
    </pre>

🔑 Setup Instructions</h3>
    <ol>
      <li>Clone or Download Project:
        <pre>git clone &lt;repo_url&gt;<br>cd ai_virtual_nurse</pre>
      </li>
      <li>Install Required Packages:
        <pre>pip install -r requirements.txt</pre>
      </li>
      <li>Get OpenAI API Key:
        <a href="https://platform.openai.com/account/api-keys" target="_blank">Create API Key</a>
      </li>
      <li>Set API Key in Your System:
        <pre>Windows:  setx OPENAI_API_KEY "sk-your-key-here"<br>Linux/Mac: export OPENAI_API_KEY="sk-your-key-here"</pre>
      </li>
      <li>Run the App:
        <pre>python app.py</pre>
      </li>
      <li>Open in Browser → <b>http://127.0.0.1:5000/</b></li>
    </ol>

📦 Requirements
    <pre>
Flask==2.3.2
openai>=1.0.0
    </pre>

⚠️ Notes
    <ul>
      <li>Ensure you have an active OpenAI API key.</li>
      <li>If you get <b>429: insufficient_quota</b>, your free credits are over.</li>
    </ul>
  </div>
</div>
</body>
</html>
