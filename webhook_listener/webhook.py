from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    subprocess.run(["ansible-playbook", "ansible/restart_nginx.yml"])
    return "Triggered", 200

app.run(port=5001)
