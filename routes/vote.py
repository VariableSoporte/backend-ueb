from fastapi import APIRouter, Depends
import schemas.student as student_schema

from database import SessionLocal

from repositories import votes_repository as crud
from sqlalchemy.orm import Session

votes_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
