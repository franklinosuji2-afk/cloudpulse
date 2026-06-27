from datetime import datetime, timedelta

EVENTS = []

def add_event(event_type: str, service: str, metadata: dict = None):
    EVENTS.append({
        "timestamp": datetime.utcnow(),
        "event_type": event_type,
        "service": service,
        "metadata": metadata or {}
    })


def get_events():
    return EVENTS


def get_recent_events(window_seconds: int = 300):
    now = datetime.utcnow()
    cutoff = now - timedelta(seconds=window_seconds)

    return [
        e for e in EVENTS
        if e["timestamp"] >= cutoff
    ]