from fastapi import APIRouter, Depends
from config.database import SessionLocal
from repositories import students as crud
from sqlalchemy.orm import Session
from schemas.student import StudentCreate, StudentEdit, Student

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


@students.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentEdit, db: Session = Depends(get_db)):
    student = crud.update_student(db, student_id, student)
    return student


@students.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    return student