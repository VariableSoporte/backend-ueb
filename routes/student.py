from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal
from repositories import students as crud
from sqlalchemy.orm import Session
from schemas.student import StudentCourse, StudentCreate, StudentEdit, Student

students = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@students.get("/voters/")
def read_voters(db: Session = Depends(get_db)):
    try:
        voters = crud.get_voters(db)
        return voters
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@students.get("/{identification_card}", response_model=StudentCourse)
def read_student(identification_card: str, db: Session = Depends(get_db)):
    try:
        db_student = crud.get_student_by_identification_card(
            db, identification_card=identification_card)
        return db_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@students.get("/pending-voters/")
def read_pending_voters(db: Session = Depends(get_db)):
    try:
        voters = crud.get_pending_voters(db)
        return voters
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@students.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentEdit, db: Session = Depends(get_db)):
    try:
        student = crud.update_student(db, student_id, student)
        return student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@students.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student = crud.delete_student(db, student_id)
        return student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@students.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        db_student = crud.get_student_by_identification_card(
            db, identification_card=student.identification_card)
        if db_student:
            raise HTTPException(status_code=400, detail="Student already registered")
        student = crud.create_student(db, student)
        return student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
