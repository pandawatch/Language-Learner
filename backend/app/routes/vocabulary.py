from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User, Vocabulary, UserVocabulary
from app.models.schemas import VocabularyItem
from app.services.auth import AuthService
from datetime import datetime, timedelta
from typing import List

router = APIRouter(prefix="/api/vocabulary", tags=["vocabulary"])

# Sample German vocabulary data
SAMPLE_VOCABULARY = [
    {"german": "Hallo", "english": "Hello", "part_of_speech": "interjection", "difficulty": 1},
    {"german": "Guten Morgen", "english": "Good morning", "part_of_speech": "phrase", "difficulty": 1},
    {"german": "Danke", "english": "Thank you", "part_of_speech": "interjection", "difficulty": 1},
    {"german": "Bitte", "english": "Please", "part_of_speech": "interjection", "difficulty": 1},
    {"german": "Ja", "english": "Yes", "part_of_speech": "adverb", "difficulty": 1},
    {"german": "Nein", "english": "No", "part_of_speech": "adverb", "difficulty": 1},
    {"german": "Wasser", "english": "Water", "part_of_speech": "noun", "difficulty": 2},
    {"german": "Brot", "english": "Bread", "part_of_speech": "noun", "difficulty": 2},
    {"german": "Katze", "english": "Cat", "part_of_speech": "noun", "difficulty": 2},
    {"german": "Hund", "english": "Dog", "part_of_speech": "noun", "difficulty": 2},
    {"german": "Haus", "english": "House", "part_of_speech": "noun", "difficulty": 1},
    {"german": "Baum", "english": "Tree", "part_of_speech": "noun", "difficulty": 2},
]


def get_current_user(token: str, db: Session = Depends(get_db)):
    """Get current user from token"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[VocabularyItem])
async def get_vocabulary(db: Session = Depends(get_db)):
    """Get all available vocabulary"""
    vocab = db.query(Vocabulary).all()
    if not vocab:
        # Initialize with sample vocabulary if empty
        for word in SAMPLE_VOCABULARY:
            vocab_item = Vocabulary(**word, category="basic", language="german")
            db.add(vocab_item)
        db.commit()
        vocab = db.query(Vocabulary).all()
    return vocab


@router.get("/user", response_model=List[VocabularyItem])
async def get_user_vocabulary(token: str, db: Session = Depends(get_db)):
    """Get vocabulary learned by the current user"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_vocab = (
        db.query(Vocabulary)
        .join(UserVocabulary)
        .filter(UserVocabulary.user_id == user.id)
        .all()
    )
    return user_vocab


@router.post("/add")
async def add_vocabulary_for_user(
    vocab_id: int, token: str, db: Session = Depends(get_db)
):
    """Add vocabulary to user's learning list"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    vocab = db.query(Vocabulary).filter(Vocabulary.id == vocab_id).first()
    if not vocab:
        raise HTTPException(status_code=404, detail="Vocabulary not found")

    # Check if already added
    existing = (
        db.query(UserVocabulary)
        .filter(UserVocabulary.user_id == user.id, UserVocabulary.vocabulary_id == vocab_id)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Already in vocabulary list")

    # Add to user's vocabulary
    user_vocab = UserVocabulary(
        user_id=user.id, vocabulary_id=vocab_id, next_review=datetime.utcnow()
    )
    db.add(user_vocab)
    db.commit()

    return {"message": "Vocabulary added successfully"}


@router.post("/mark-correct")
async def mark_correct(vocab_id: int, token: str, db: Session = Depends(get_db)):
    """Mark vocabulary as correctly answered"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_vocab = (
        db.query(UserVocabulary)
        .filter(UserVocabulary.user_id == user.id, UserVocabulary.vocabulary_id == vocab_id)
        .first()
    )
    if not user_vocab:
        raise HTTPException(status_code=404, detail="Vocabulary entry not found")

    user_vocab.times_reviewed += 1
    user_vocab.times_correct += 1
    # Schedule next review in 1 day (can use spaced repetition algorithm)
    user_vocab.next_review = datetime.utcnow() + timedelta(days=1)

    db.commit()
    return {"message": "Marked as correct"}
