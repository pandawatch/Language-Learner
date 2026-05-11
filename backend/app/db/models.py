from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    lessons = relationship("UserLesson", back_populates="user")
    vocabulary = relationship("UserVocabulary", back_populates="user")
    progress = relationship("Progress", back_populates="user")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    language = Column(String, default="german")
    difficulty = Column(Integer, default=1)  # 1-5
    content = Column(Text)
    exercise = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_lessons = relationship("UserLesson", back_populates="lesson")


class UserLesson(Base):
    __tablename__ = "user_lessons"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    completed = Column(Boolean, default=False)
    score = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="lessons")
    lesson = relationship("Lesson", back_populates="user_lessons")


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    german = Column(String, index=True)
    english = Column(String)
    pronunciation = Column(String, nullable=True)
    part_of_speech = Column(String)  # noun, verb, adjective, etc.
    difficulty = Column(Integer, default=1)  # 1-5
    category = Column(String, default="general")
    language = Column(String, default="german")

    user_vocabulary = relationship("UserVocabulary", back_populates="vocabulary")


class UserVocabulary(Base):
    __tablename__ = "user_vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vocabulary_id = Column(Integer, ForeignKey("vocabulary.id"))
    times_reviewed = Column(Integer, default=0)
    times_correct = Column(Integer, default=0)
    next_review = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="vocabulary")
    vocabulary = relationship("Vocabulary", back_populates="user_vocabulary")


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_lessons_completed = Column(Integer, default=0)
    total_vocabulary_learned = Column(Integer, default=0)
    current_streak = Column(Integer, default=0)
    last_activity = Column(DateTime, nullable=True)
    language = Column(String, default="german")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="progress")
