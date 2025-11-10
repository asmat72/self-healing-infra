# ***self-healing-infra***
“A self-healing system for cloud infrastructure using monitoring and automated recovery scripts.”

- ***🎯 Objective:***
      - Automatically detect service failures (e.g., NGINX down) and recover them using Prometheus     alerts, Alertmanager notifications, and Ansible automation.
      - Clone the repository:  
                “git clone   ***“https://github.com/asmat72/self-healing-infra.git”***
  
- ***🧰 Tools Used:***
    - “Prometheus”.
    - “Alertmanager”
    - “Ansible”
    - “Shell Scripting”
    - “Ubuntu VM / Docker”
    - “NGINX”
  
  - ***🚀 Setup Guide:***
      - 🔧 Deploy NGINX:
      - 📈 Install Prometheus:
      - ⚠️ Create Alert Rules:
      - 📣 Configure Alertmanager:
      - 🧪  Build Webhook Listener:
      - 🔁 Create Ansible Playbook:
  
  - ***🎬 Demo: Test and Capture:***
      - Stop NGINX manually:
      - Prometheus detects failure up{job="nginx"} == 0
      - Alertmanager fires alert Alert routed to webhook:
      - NGINX restarts automatically Verified via   "systemctl status nginx" :
  
  - ***📦 Deliverables:***
      - Prometheus config:
      - Alertmanager webhook setup:
      - Ansible playbook:
      - Webhook listener:
      - Demo logs and screenshots:
   
  - ***📚 Notes:***
      - You can extend this setup to monitor other services or metrics (e.g., CPU, memory).
      - For production, secure the webhook and use remote Ansible hosts.   

