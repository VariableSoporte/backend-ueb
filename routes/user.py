from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from repositories import users as crud
from sqlalchemy.orm import Session

user_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/login/{username}/{password}")
def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        user = crud.login(db, username, password)
        if user:
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
