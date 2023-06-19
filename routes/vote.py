from fastapi import APIRouter, Depends
import schemas.votes_null as votes_null_schema

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

@votes_router.post("/vote/{student_id}/{list_id}")
def vote_for_list(student_id: int, list_id: int, db: Session = Depends(get_db)):
    student = crud.vote_for_list(db, student_id, list_id)
    return student

@votes_router.post("/null/{student_id}")
def vote_null(student_id: int, db: Session = Depends(get_db)):
    student = crud.vote_null(db, student_id)
    return student

@votes_router.post("/blank/{student_id}")
def blank_vote(student_id: int, db: Session = Depends(get_db)):
    student = crud.blank_vote(db, student_id)
    return student

@votes_router.get("/nulls_blanks/", response_model=votes_null_schema.VotesNull)
def get_nulls_blanks(db: Session = Depends(get_db)):
    nulls_blanks = crud.get_null_blank_votes(db)
    return nulls_blanks