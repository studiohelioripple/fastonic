from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from db import get_db, User

router = APIRouter()


class UserCreate(BaseModel):
    name: str
    email: EmailStr


@router.get("/")
def home():
    return {"message": "FastAPI + MySQL running on ParsPack"}


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(400, "Email already exists")

    new_user = User(
        name=user.name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
