from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, Progress
from app.models.schemas import ProgressResponse, ChatRequest, ChatResponse
from app.services.auth import AuthService
from app.services.ai_tutor import AITutorService
from datetime import datetime

router = APIRouter(prefix="/api/tutor", tags=["tutor"])


@router.post("/chat", response_model=ChatResponse)
async def chat_with_tutor(
    request: ChatRequest, token: str, db: Session = Depends(get_db)
):
    """Chat with the AI language tutor"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Initialize AI tutor service
    ai_tutor = AITutorService()

    # Prepare conversation history
    history = []
    for msg in request.conversation_history:
        history.append({"role": msg.role, "content": msg.content})

    # Get response from AI tutor
    response = await ai_tutor.chat(
        request.message, history, proficiency_level="beginner"
    )

    # Update user's last activity
    progress = db.query(Progress).filter(Progress.user_id == user.id).first()
    if progress:
        progress.last_activity = datetime.utcnow()
        db.commit()

    return ChatResponse(
        response=response["response"],
        suggestions=response["suggestions"],
        corrections=response["corrections"],
    )


@router.get("/progress", response_model=ProgressResponse)
async def get_user_progress(token: str, db: Session = Depends(get_db)):
    """Get user's learning progress"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    progress = db.query(Progress).filter(Progress.user_id == user.id).first()
    if not progress:
        # Create progress record
        progress = Progress(user_id=user.id, language="german")
        db.add(progress)
        db.commit()

    return ProgressResponse(
        total_lessons_completed=progress.total_lessons_completed,
        total_vocabulary_learned=progress.total_vocabulary_learned,
        current_streak=progress.current_streak,
        last_activity=progress.last_activity,
        languages=[progress.language],
    )


@router.post("/lesson/generate")
async def generate_lesson(topic: str, difficulty: str = "beginner", token: str = ""):
    """Generate a new lesson using AI"""
    if token:
        email = AuthService.verify_token(token)
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    ai_tutor = AITutorService()
    lesson = ai_tutor.generate_lesson(topic, difficulty)
    return lesson


@router.post("/vocabulary/exercise")
async def generate_vocabulary_exercise(
    words: list[str], exercise_type: str = "multiple_choice", token: str = ""
):
    """Generate vocabulary exercises"""
    if token:
        email = AuthService.verify_token(token)
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    ai_tutor = AITutorService()
    exercise = ai_tutor.generate_vocabulary_exercise(words, exercise_type)
    return exercise
