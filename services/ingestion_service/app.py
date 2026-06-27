from fastapi import FastAPI
from services.ingestion_service.database import engine, SessionLocal
from services.ingestion_service.models import Base, Metric
import random

app = FastAPI()

Base.metadata.create_all(bind=engine)


def generate_metric():
    # 90% normal load
    if random.random() < 0.9:
        return random.uniform(40, 60)
    # 10% anomaly spike
    return random.uniform(150, 250)


@app.get("/")
def root():
    return {"service": "ingestion-service", "status": "healthy"}


@app.post("/collect")
def collect():
    db = SessionLocal()

    metric = Metric(
        metric_name="cpu_usage",
        metric_value=generate_metric(),
        service_name="checkout-service"
    )

    db.add(metric)
    db.commit()
    db.close()

    return {"status": "metric stored"}


@app.get("/metrics")
def metrics():
    db = SessionLocal()
    rows = db.query(Metric).all()

    results = [
        {
            "metric": row.metric_name,
            "value": row.metric_value,
            "service": row.service_name,
            "timestamp": row.timestamp
        }
        for row in rows
    ]

    db.close()
    return results