from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    prompt = Column(Text)

    image_url = Column(Text)

    status = Column(
        String(30),
        default="pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )