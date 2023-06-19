from schemas.course import CourseCreate
from sqlalchemy.orm import Session
import models
import pandas as pd
from database import engine


def get_courses(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Course).all()


def create_course(db: Session, course: CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def update_course_data_file(db: Session, course_id: int, file: str):
    db.query(models.Course).filter(models.Course.id == course_id).update({"data_file": file})
    db.commit()
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def add_students(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    pd.read_excel(f'data/courses/{db_course.data_file}').to_sql('students', con=engine, if_exists='append', index=False)
    db.commit()
    return {"message": "Test students added"}