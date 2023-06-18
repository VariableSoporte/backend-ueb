from sqlalchemy.orm import Session
from schemas.candidate import CandidateCreate
from schemas.dignity import DignityCreate
from schemas.student import StudentCreate
from schemas.course import CourseCreate
import models

def get_students(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Student).all()

def create_student(db: Session, student: StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_courses(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Course).all()

def create_course(db: Session, course: CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_dignities(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Dignity).all()

def create_dignity(db: Session, dignity: DignityCreate):
    db_dignity = models.Dignity(**dignity.dict())
    db.add(db_dignity)
    db.commit()
    db.refresh(db_dignity)
    return db_dignity

def get_candidates(db: Session, skip: int = 1, limit: int = 100):
    # Para que se muestren solo los presidentes se debe usar un where
    return db.query(models.Candidate).where(models.Candidate.dignity_id == 1).all()

def create_candidate(db: Session, candidate: CandidateCreate):
    db_candidate = models.Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate