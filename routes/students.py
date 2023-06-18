from fastapi import APIRouter, Depends
import schemas.student as student_schema

from database import SessionLocal

from repositories import students_repository as crud
from sqlalchemy.orm import Session


student_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@student_router.get("/", response_model=list[student_schema.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@student_router.post("/", response_model=student_schema.Student)
def create_student(student: student_schema.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, student=student)
    return db_student