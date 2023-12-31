from fastapi import APIRouter, Depends
import schemas.votes_null as votes_null_schema

from config.database import SessionLocal

from repositories import votes as crud
from sqlalchemy.orm import Session

vote_router = APIRouter()

if crud.count_null_blank_votes(db=SessionLocal()) == 0:
    votes_null = votes_null_schema.VoteNullCreate(null_votes=0, blank_votes=0)
    crud.add_null_blank_votes(db=SessionLocal(), votes_null=votes_null)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@vote_router.post("/vote/{student_id}/{list_id}")
def vote_for_list(student_id: int, list_id: int, db: Session = Depends(get_db)):
    student = crud.vote_for_list(db, student_id, list_id)
    return student
    # return student_id

@vote_router.post("/null/{student_id}")
def vote_null(student_id: int, db: Session = Depends(get_db)):
    student = crud.vote_null(db, student_id)
    return student

@vote_router.post("/blank/{student_id}")
def blank_vote(student_id: int, db: Session = Depends(get_db)):
    student = crud.blank_vote(db, student_id)
    return student

@vote_router.get("/nulls-blanks/")
def get_nulls_blanks(db: Session = Depends(get_db)):
    nulls_blanks = crud.get_null_blank_votes(db)
    return nulls_blanks