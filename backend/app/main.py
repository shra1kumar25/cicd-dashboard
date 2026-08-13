from fastapi import FastAPI

from app.api.projects import router as projects_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CI/CD Dashboard API",
    version="1.0.0",
    description="Backend API for the CI/CD Dashboard",
)

app.include_router(projects_router)


@app.get("/")
def home():
    return {
        "message": "CI/CD Dashboard API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
