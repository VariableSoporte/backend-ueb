from schemas.votes_null import VotesNullCreate
from sqlalchemy.orm import Session
import models
from repositories import students_repository as crud_students


def vote_for_list(db: Session, student_id: int, list_id: int):
    student = crud_students.get_student(db, student_id)
    if student.can_vote == False:
        return False
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.query(models.List).filter(models.List.id == list_id).update({"votes": models.List.votes + 1})
    db.commit()
    return True

def vote_null(db: Session, student_id: int):
    student = crud_students.get_student(db, student_id)
    if student.can_vote == False:
        return False
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.query(models.VotesNull).update({"null_votes": models.VotesNull.null_votes + 1})
    db.commit()
    return True

def blank_vote(db: Session, student_id: int):
    student = crud_students.get_student(db, student_id)
    if student.can_vote == False:
        return False
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.query(models.VotesNull).update({"blank_votes": models.VotesNull.blank_votes + 1})
    db.commit()
    return True

def get_null_blank_votes(db: Session):
    return db.query(models.VotesNull).first()

def add_null_blank_votes(db: Session, votes_null: VotesNullCreate):
    db_votes_null = models.VotesNull(**votes_null.dict())
    db.add(db_votes_null)
    db.commit()
    db.refresh(db_votes_null)
    return db_votes_null

def count_null_blank_votes(db: Session):
    return db.query(models.VotesNull).count()
