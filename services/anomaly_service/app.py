import requests
from fastapi import FastAPI
from sqlalchemy import text
from services.anomaly_service.database import SessionLocal
from services.anomaly_service.detector import detect_anomaly

app = FastAPI()


@app.get("/")
def root():
    return {"service": "anomaly-service"}


@app.get("/detect")
def detect():
    db = SessionLocal()

    result = db.execute(
        text("""
            SELECT metric_value
            FROM metrics
            WHERE metric_name='cpu_usage'
            ORDER BY timestamp ASC
        """)
    )

    values = [row[0] for row in result]
    db.close()

    return detect_anomaly(values)