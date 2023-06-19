from schemas.student import StudentCreate
from sqlalchemy.orm import Session
import models
import pandas as pd
from database import engine


def get_students(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Student).all()


def create_student(db: Session, student: StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
