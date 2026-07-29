from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Job
from .ai import generate_image_prompt
from dotenv import load_dotenv

load_dotenv()
router=APIRouter()



@router.post("/generate")
def generate(product_name: str, description: str, db: Session = Depends(get_db)):
    prompt = generate_image_prompt(product_name, description)

    # Placeholder image
    image_url = "https://placehold.co/512x512/png?text=AI+Placeholder"

    job = Job(
        product_name=product_name,
        description=description,
        prompt=prompt,
        image_url=image_url,
        status="completed"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job

@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.get("/health")
def health():
    return {"status": "healthy"}
