from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    subprocess.run(['ansible-playbook', 'restart-nginx.yml'])
    return 'NGINX restart triggered', 200

if __name__ == '__main__':
    app.run(port=5001)
