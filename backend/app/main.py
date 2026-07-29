from .routes import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .models import Job

app = FastAPI(
    title="GlitrAI Mini Content Engine",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create database tables
Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to GlitrAI Mini Content Engine"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }