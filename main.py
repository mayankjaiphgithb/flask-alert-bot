from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive ✅"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("Alert received:", data)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
