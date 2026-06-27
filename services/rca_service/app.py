from fastapi import FastAPI
from services.rca_service.engine import correlate
from services.rca_service.event_store import add_event

app = FastAPI()


@app.post("/event")
def create_event(event_type: str, service: str):
    add_event(event_type, service)
    return {"status": "event recorded"}


@app.get("/analyze")
def analyze():
    anomaly = {
        "z_score": 3.2,
        "severity": "critical"
    }

    return correlate(anomaly)

@app.get("/")
def root():
    return {"service": "rca-service"}
