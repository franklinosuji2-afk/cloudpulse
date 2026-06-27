import statistics
import requests

WINDOW_SIZE = 10

def detect_anomaly(values):
    if len(values) < WINDOW_SIZE:
        return {
            "status": "warming_up",
            "data_points": len(values),
            "required": WINDOW_SIZE
        }

    window = values[-WINDOW_SIZE:]
    mean = statistics.mean(window)
    std_dev = statistics.stdev(window)
    latest = window[-1]

    if std_dev == 0:
        z_score = 0
    else:
        z_score = abs((latest - mean) / std_dev)

    if z_score > 3:
        severity = "critical"
    elif z_score > 2:
        severity = "warning"
    else:
        severity = "normal"

    if severity != "normal":
        try:
            requests.post(
                "http://127.0.0.1:8002/event",
                params={
                    "event_type": "anomaly_detected",
                    "service": "checkout-service"
                },
                timeout=2
            )
        except Exception as e:
            print(f"RCA service unavailable: {e}")

    return {
        "latest_value": latest,
        "mean_window": mean,
        "std_dev": std_dev,
        "z_score": round(z_score, 2),
        "severity": severity
    }
