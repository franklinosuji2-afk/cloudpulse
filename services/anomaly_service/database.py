from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://cloudpulse:cloudpulse@localhost:5432/telemetry"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)