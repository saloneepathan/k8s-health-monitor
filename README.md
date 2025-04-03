# Kubernetes Health Monitor 🚀

## Overview
K8s Health Monitor is a **Python-based monitoring tool** that integrates with **Prometheus** and **Alertmanager** to track Kubernetes cluster health, CPU/memory usage, and node performance. It triggers alerts via **Slack and Email** when thresholds are exceeded.

---

## Features
✅ Monitor **CPU & Memory usage** of Kubernetes nodes  
✅ Fetch real-time metrics from **Prometheus API**  
✅ **Slack & Email alerts** for threshold breaches  
✅ Configurable **alert levels**  

---

## Prerequisites
📌 **Install Dependencies**:  
```bash
pip install requests
```
📌 **Set Up Prometheus & Alertmanager**  
- Ensure Prometheus is running and configured correctly.  
- The API should be accessible at: `http://localhost:9090/api/v1/query`  
- Slack webhook & SMTP email setup is required.  

---

## Installation & Usage
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourrepo/k8s-health-monitor.git
cd k8s-health-monitor
```

### **2️⃣ Configure Environment Variables**
Edit the script and set up:  
- **Prometheus API URL**  
- **Slack Webhook URL**  
- **Email SMTP Settings**  

### **3️⃣ Run the Monitor**
```bash
python k8s_health_monitor.py
```

---

## Configuration
You can modify **thresholds** inside `k8s_health_monitor.py`:
```python
CPU_THRESHOLD = 80  # Adjust as needed
MEMORY_THRESHOLD = 80
```

---

## Alerts & Notifications
🔹 **Slack Alerts**: Configured via Slack Webhook  
🔹 **Email Alerts**: Uses SMTP for notifications  
🔹 **Console Logs**: Alerts are printed in CLI  

---

## Future Enhancements (Coming Soon) 🚀
🔹 **Grafana Integration** for visual dashboards  
🔹 **K8s Deployment** as a CronJob  
🔹 **Logging with Elasticsearch**  

---

## License
📜 MIT License
