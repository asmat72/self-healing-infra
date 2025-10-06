from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Received alert:", request.json)
    subprocess.run(["ansible-playbook", "ansible/restart-nginx.yml"])
    return '', 200

app.run(port=5000)
