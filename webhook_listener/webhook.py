from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
        try:
            result = subprocess.run(
                ["ansible-playbook", "ansible/restart_nginx.yml"],
                check=True,
                capture_output=True,
                text=True
            )
            return f"Triggered successfullyy:\n{result.stdout}", 200
        except subprocess.CalledProcessError as e:
            return f"Error triggering playbook:\n{e.stderr}", 500

if __name__ == "__main__"
    # Use 0.0.0.0 to listen on all interfaces
    app.run(port=5000)
