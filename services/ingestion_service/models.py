from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from services.ingestion_service.database import Base


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)
    metric_name = Column(String)
    metric_value = Column(Float)
    service_name = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)