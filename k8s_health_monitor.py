import requests
import json
import smtplib
from email.mime.text import MIMEText

# Prometheus API URL (Adjust to your setup)
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Alert Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage

# Slack Webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/slack/webhook"

# Email Alert Config
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_SENDER = "alert@example.com"
EMAIL_RECEIVER = "admin@example.com"
EMAIL_PASSWORD = "yourpassword"


def query_prometheus(query):
    """Fetch metrics from Prometheus"""
    response = requests.get(PROMETHEUS_URL, params={"query": query})
    data = response.json()
    return data["data"]["result"]


def check_cluster_health():
    """Check CPU and Memory usage for nodes"""
    cpu_usage = query_prometheus("100 - (avg by (instance) (irate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)")
    memory_usage = query_prometheus("(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100")
    alerts = []

    for node in cpu_usage:
        usage = float(node["value"][1])
        if usage > CPU_THRESHOLD:
            alerts.append(f"🚨 High CPU Usage on {node['metric']['instance']}: {usage}%")

    for node in memory_usage:
        usage = float(node["value"][1])
        if usage > MEMORY_THRESHOLD:
            alerts.append(f"🚨 High Memory Usage on {node['metric']['instance']}: {usage}%")

    return alerts


def send_slack_alert(message):
    """Send alert to Slack"""
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})


def send_email_alert(message):
    """Send alert via email"""
    msg = MIMEText(message)
    msg["Subject"] = "🚨 Kubernetes Health Alert"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())


def main():
    alerts = check_cluster_health()
    for alert in alerts:
        print(alert)
        send_slack_alert(alert)
        send_email_alert(alert)

if __name__ == "__main__":
    main()
