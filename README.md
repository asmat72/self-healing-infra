# ***🔧 Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible***
##              ***self-healing-infra***
"A real-world automation project that detects service failures and automatically recovers them using Prometheus alerts and Ansible playbooks.            
 A self-healing system for cloud infrastructure using monitoring and automated recovery scripts.”

- ***🎯 Objective:***
   - Build a self-healing infrastructure that can:
     - Detect service failures (e.g., NGINX down, CPU overload)
     - Trigger alerts using Prometheus and Alertmanager.
     - Automatically recover services using Ansible automation
     - Clone the repository:  
                “git clone   ***“https://github.com/asmat72/self-healing-infra.git”***
  
- ***🧰 Tools Used:***
   - **Prometheus** – Monitoring and alerting.
   - **Alertmanager** – Alert routing and webhook execution.
   - **Ansible** – Automation engine for recovery tasks.
   - **Shell Scripting** – Lightweight service checks and triggers.
   - **Ubuntu VM / Docker** – Deployment environment.
   - **NGINX**

- ***📘 Mini Guide:***
   1. **Deploy a Sample Service**  
      Example: NGINX running on Ubuntu VM or Docker container.
   
   2. **Monitor with Prometheus**  
      Configure Prometheus to scrape metrics and monitor uptime.

   3. **Set Alert Thresholds**  
      Define rules like:
      - Service down
      - CPU usage > 90%

   4. **Trigger Alertmanager Webhook**  
      On alert, Alertmanager calls a webhook that triggers an Ansible playbook.

   5. **Run Ansible Playbook**  
      The playbook restarts the failed service or reboots the system if needed.

- ***📁 Project Structure:***
   - self_healing_infra/
      -   │    ├── restart_nginx.yml
      -   │    ├── prometheus.yml
      -   │    ├── alert.rules.yml
      -   │    ├── alertmanager.yml 
      -   │    ├── Webhook_listener
      -   │            └── webhook.py
      -   │    ├── README.md
      -   │    ├── screenshots & logs
  
  - ***🎬 Demo: Test and Capture:***
      - Stop NGINX manually:
      - Prometheus detects failure up{job="nginx"} == 0
      - Alertmanager fires alert Alert routed to webhook:
      - NGINX restarts automatically Verified via   "systemctl status nginx" :

  - ***📦 Deliverables:***
      - ✅ Prometheus configuration files.
      - ✅ Alertmanager webhook setup.
      - ✅ Webhook listener.
      - ✅ Ansible playbook for recovery.
      - ✅ Demo logs or screenshots showing auto-healing in action.
   
  - ***📚 Notes:***
      - You can extend this setup to monitor other services or metrics (e.g., CPU, memory).
      - For production, secure the webhook and use remote Ansible hosts.

  - ***🙌 Credits:***
      - Developed by ***ᴀꜱᴍᴀᴛuʟʟᴀн кнαη***  
      - Aspiring DevOps Engineer  
      - Focused on building resilient, automated infrastructure using open-source tools

