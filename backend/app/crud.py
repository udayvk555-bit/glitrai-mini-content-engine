from sqlalchemy.orm import Session
from .models import Job

def get_jobs(db: Session):
    return db.query(Job).all()