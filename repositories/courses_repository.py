from schemas.course import CourseCreate
from sqlalchemy.orm import Session
import models


def get_courses(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Course).all()


def create_course(db: Session, course: CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
