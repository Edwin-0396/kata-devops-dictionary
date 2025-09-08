import requests
import numpy as np

PROMETHEUS_URL = "http://prometheus:9090/api/v1/query"

# Query dictionary lookups over 5m window
QUERY = 'sum by (result) (rate(dictionary_requests_total[5m]))'

def fetch_metrics():
    response = requests.get(PROMETHEUS_URL, params={"query": QUERY})
    response.raise_for_status()
    data = response.json()["data"]["result"]
    return {item["metric"]["result"]: float(item["value"][1]) for item in data}

def detect_anomaly(metrics):
    # Simple z-score anomaly detection
    values = list(metrics.values())
    if not values:
        return None
    mean = np.mean(values)
    std = np.std(values)
    anomalies = {k: v for k, v in metrics.items() if abs(v - mean) > 2 * std}
    return anomalies

if __name__ == "__main__":
    metrics = fetch_metrics()
    anomalies = detect_anomaly(metrics)
    if anomalies:
        print("🚨 Anomaly detected:", anomalies)
    else:
        print("✅ Metrics within normal range")
