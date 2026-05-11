from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class VocabularyItem(BaseModel):
    id: int
    german: str
    english: str
    pronunciation: Optional[str]
    part_of_speech: str
    difficulty: int  # 1-5

    class Config:
        from_attributes = True


class LessonResponse(BaseModel):
    id: int
    title: str
    language: str
    difficulty: int
    content: str
    exercise: str

    class Config:
        from_attributes = True


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    language: str = "german"


class ChatRequest(BaseModel):
    message: str
    language: str = "german"
    conversation_history: Optional[list[ChatMessage]] = []


class ChatResponse(BaseModel):
    response: str
    suggestions: list[str]
    corrections: Optional[str]


class ProgressResponse(BaseModel):
    total_lessons_completed: int
    total_vocabulary_learned: int
    current_streak: int
    last_activity: Optional[datetime]
    languages: list[str]

    class Config:
        from_attributes = True
