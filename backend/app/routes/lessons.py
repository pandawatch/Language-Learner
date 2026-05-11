from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, Lesson, UserLesson
from app.models.schemas import LessonResponse
from app.services.auth import AuthService
from app.services.ai_tutor import AITutorService
from typing import List
from datetime import datetime

router = APIRouter(prefix="/api/lessons", tags=["lessons"])

# Sample lessons
SAMPLE_LESSONS = [
    {
        "title": "Greetings 101",
        "language": "german",
        "difficulty": 1,
        "content": "Hallo! Guten Morgen! Gute Nacht!",
        "exercise": "What does 'Hallo' mean?",
    },
    {
        "title": "Basic Numbers",
        "language": "german",
        "difficulty": 1,
        "content": "eins, zwei, drei, vier, fünf",
        "exercise": "Count from 1 to 5 in German",
    },
    {
        "title": "Daily Phrases",
        "language": "german",
        "difficulty": 2,
        "content": "Wie geht's? Das ist sehr gut. Auf Wiedersehen!",
        "exercise": "Translate these phrases to English",
    },
]


@router.get("/", response_model=List[LessonResponse])
async def get_lessons(db: Session = Depends(get_db)):
    """Get all available lessons"""
    lessons = db.query(Lesson).filter(Lesson.language == "german").all()
    if not lessons:
        # Initialize with sample lessons
        for lesson_data in SAMPLE_LESSONS:
            lesson = Lesson(**lesson_data)
            db.add(lesson)
        db.commit()
        lessons = db.query(Lesson).filter(Lesson.language == "german").all()
    return lessons


@router.get("/german", response_model=List[LessonResponse])
async def get_german_lessons(db: Session = Depends(get_db)):
    """Get German lessons"""
    lessons = db.query(Lesson).filter(Lesson.language == "german").all()
    if not lessons:
        # Initialize with sample lessons
        for lesson_data in SAMPLE_LESSONS:
            lesson = Lesson(**lesson_data)
            db.add(lesson)
        db.commit()
        lessons = db.query(Lesson).filter(Lesson.language == "german").all()
    return lessons


@router.get("/{lesson_id}", response_model=LessonResponse)
async def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """Get a specific lesson"""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@router.post("/{lesson_id}/complete")
async def complete_lesson(
    lesson_id: int, token: str, score: int, db: Session = Depends(get_db)
):
    """Mark a lesson as completed"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    # Check if already completed
    user_lesson = (
        db.query(UserLesson)
        .filter(UserLesson.user_id == user.id, UserLesson.lesson_id == lesson_id)
        .first()
    )

    if user_lesson:
        user_lesson.completed = True
        user_lesson.score = score
        user_lesson.completed_at = datetime.utcnow()
    else:
        user_lesson = UserLesson(
            user_id=user.id,
            lesson_id=lesson_id,
            completed=True,
            score=score,
            completed_at=datetime.utcnow(),
        )
        db.add(user_lesson)

    db.commit()
    return {"message": "Lesson completed", "score": score}


@router.post("/generate")
async def generate_lesson(topic: str, difficulty: str = "beginner"):
    """Generate a new lesson using AI"""
    ai_service = AITutorService()
    lesson = ai_service.generate_lesson(topic, difficulty)
    return lesson
