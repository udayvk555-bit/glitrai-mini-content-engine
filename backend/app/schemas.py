from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GenerateRequest(BaseModel):
    product_name: str
    description: str


class JobResponse(BaseModel):
    id: int
    product_name: str
    description: str
    prompt: Optional[str] = None
    image_url: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True