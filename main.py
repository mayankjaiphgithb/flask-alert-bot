import os
from flask import Flask, request, jsonify
from telegram import Bot
from datetime import datetime

app = Flask(__name__)

# Telegram credentials (Railway me env vars me set honge)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN) if TELEGRAM_TOKEN else None

@app.route("/", methods=["GET"])
def home():
    return "Flask Alert Bot is Running ✅", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook Data:", data)

    msg = f"🔔 Alert Received:\n{data}\n⏰ {datetime.now()}"
    if bot and TELEGRAM_CHAT_ID:
        try:
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)
        except Exception as e:
            print("Telegram Error:", e)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
