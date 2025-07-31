async function sendMessage() {
  let input = document.getElementById("user-input").value;
  if (!input) return;

  addMessage("You", input, "user-msg");
  document.getElementById("user-input").value = "";

  addMessage("Nurse", "⏳ Typing...", "bot-msg", true);

  let res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: input })
  });
  let data = await res.json();

  // Remove "Typing..."
  document.getElementById("chat-box").lastChild.remove();

  addMessage("Nurse", data.reply, "bot-msg");
  loadReminders();
}

function addMessage(sender, text, cls, temporary=false) {
  let box = document.getElementById("chat-box");
  let msg = document.createElement("div");
  msg.className = "chat-message " + cls;
  msg.innerHTML = `<b>${sender}:</b> ${text}`;
  box.appendChild(msg);
  box.scrollTop = box.scrollHeight;
  if (temporary) return msg;
}

async function loadReminders() {
  let res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: "reminders" })
  });
  let data = await res.json();

  let list = document.getElementById("reminder-list");
  list.innerHTML = "";
  if (data.reply.includes("🔔 Reminders:")) {
    let reminders = data.reply.split("🔔 Reminders: ")[1].split(",");
    reminders.forEach(r => {
      let li = document.createElement("li");
      li.className = "list-group-item";
      li.textContent = r.trim();
      list.appendChild(li);
    });
  }
}

function startVoice() {
  let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();
  recognition.onresult = function (event) {
    document.getElementById("user-input").value = event.results[0][0].transcript;
  };
}

window.onload = loadReminders;
