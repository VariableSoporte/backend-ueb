from fastapi import APIRouter, Depends
from database import SessionLocal
from repositories import user_repository as crud
from sqlalchemy.orm import Session

user_router = APIRouter()

@user_router.post("/login")
def login(username: str, password: str, db: Session = Depends(crud.get_db)):
    user = crud.login(db, username, password)
    if user:
        return True
    else:
        return False