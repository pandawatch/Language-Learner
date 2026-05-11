from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.db.database import get_db
from app.db.models import User
from app.models.schemas import UserRegister, UserLogin, TokenResponse, UserResponse
from app.services.auth import AuthService
import os

router = APIRouter(prefix="/api/auth", tags=["auth"])

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


@router.post("/register", response_model=TokenResponse)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    hashed_password = AuthService.hash_password(user_data.password)
    user = User(
        email=user_data.email, username=user_data.username, hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    user_response = UserResponse(
        id=user.id, email=user.email, username=user.username, created_at=user.created_at
    )

    return TokenResponse(access_token=access_token, token_type="bearer", user=user_response)


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """Login a user"""
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not AuthService.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    user_response = UserResponse(
        id=user.id, email=user.email, username=user.username, created_at=user.created_at
    )

    return TokenResponse(access_token=access_token, token_type="bearer", user=user_response)


@router.post("/verify")
async def verify_token(token: str):
    """Verify a token"""
    email = AuthService.verify_token(token)
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    return {"email": email, "valid": True}
