from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received alert:", request.json)
    return "Triggered", 200

app.run(port=5001)
