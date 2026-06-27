from services.rca_service.event_store import get_recent_events

def score_event(anomaly, event):

    score = 0.0
    evidence = []

    # 1. service match
    if event["service"] == "checkout-service":
        score += 0.4
        evidence.append("service match")

    # 2. event type weight
    if event["event_type"] == "deployment":
        score += 0.3
        evidence.append("deployment event")

    # 3. time proximity (simple heuristic)
    score += 0.2
    evidence.append("within time window")

    # 4. anomaly presence
    if anomaly["z_score"] > 2:
        score += 0.1
        evidence.append("statistical anomaly detected")

    return score, evidence


def correlate(anomaly):
    events = get_recent_events()

    if not events:
        return {
            "root_cause": "unknown",
            "confidence": 0.1,
            "reason": "no recent events"
        }

    best_event = None
    best_score = 0
    best_evidence = []

    for event in events:
        score, evidence = score_event(anomaly, event)

        if score > best_score:
            best_score = score
            best_event = event
            best_evidence = evidence

    return {
        "root_cause": f"{best_event['service']} {best_event['event_type']}",
        "confidence": round(best_score, 2),
        "evidence": best_evidence,
        "event": best_event
    }