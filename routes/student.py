from fastapi import APIRouter, Depends
from config.database import SessionLocal
from repositories import students as crud
from sqlalchemy.orm import Session

students = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@students.get("/voters/")
def read_voters(db: Session = Depends(get_db)):
    voters = crud.get_voters(db)
    return voters


@students.get("/{identification_card}")
def read_student(identification_card: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_identification_card(
        db, identification_card=identification_card)
    return db_student


@students.get("/pending-voters/")
def read_pending_voters(db: Session = Depends(get_db)):
    voters = crud.get_pending_voters(db)
    return voters
