from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
import crud, models
# from schemas.candidate import CandidateCreate, Candidate
# from schemas.dignity import DignityCreate, Dignity
# from schemas.student import StudentCreate, Student
# from schemas.course import CourseCreate, Course
import schemas.candidate as candidate_schema
import schemas.dignity as dignity_schema
import schemas.student as student_schema
import schemas.course as course_schema
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/courses/", response_model=course_schema.Course)
def create_course(course: course_schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.create_course(db=db, course=course)
    return db_course

@app.get("/courses/", response_model=list[course_schema.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@app.get("/students/", response_model=list[student_schema.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.post("/students/", response_model=student_schema.Student)
def create_student(student: student_schema.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, student=student)
    return db_student

@app.get("/dignities/", response_model=list[dignity_schema.Dignity])
def read_dignities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dignities = crud.get_dignities(db, skip=skip, limit=limit)
    return dignities

@app.post("/dignities/", response_model=dignity_schema.Dignity)
def create_dignity(dignity: dignity_schema.DignityCreate, db: Session = Depends(get_db)):
    db_dignity = crud.create_dignity(db=db, dignity=dignity)
    return db_dignity

@app.get("/candidates/", response_model=list[candidate_schema.Candidate])
def read_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    candidates = crud.get_candidates(db, skip=skip, limit=limit)
    return candidates

@app.post("/candidates/", response_model=candidate_schema.Candidate)
def create_candidate(candidate: candidate_schema.CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = crud.create_candidate(db=db, candidate=candidate)
    return db_candidate