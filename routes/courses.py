from fastapi import APIRouter, Depends
import schemas.course as course_schema
from database import SessionLocal
from repositories import courses_repository as crud
from sqlalchemy.orm import Session

course_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@course_router.post("/", response_model=course_schema.Course)
def create_course(course: course_schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.create_course(db=db, course=course)
    return db_course

@course_router.get("/", response_model=list[course_schema.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses
