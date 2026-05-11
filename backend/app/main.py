from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base
from app.routes import auth, lessons, vocabulary, tutor
from app.db.models import User, Lesson, Vocabulary, UserLesson, UserVocabulary, Progress
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Language Learner API",
    description="AI-powered language learning platform",
    version="1.0.0",
)

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(lessons.router)
app.include_router(vocabulary.router)
app.include_router(tutor.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Language Learner API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
