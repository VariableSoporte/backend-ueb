from schemas.votes_null import VotesCreate
from sqlalchemy.orm import Session
import models
from repositories import students_repository as crud_students


def vote_for_list(db: Session, list_id: int, student_id: int):
    db.query(models.List).filter(models.List.id == list_id).update({"votes": models.List.votes + 1})
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.commit()
    return True

def vote_null(db: Session, student_id: int):
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.query(models.VotesNull).update({"null_votes": models.VotesNull.null_votes + 1})
    db.commit()
    return True

def blank_vote(db: Session, student_id: int):
    db.query(models.Student).filter(models.Student.id == student_id).update({"can_vote": False})
    db.query(models.VotesNull).update({"blank_votes": models.VotesNull.blank_votes + 1})
    db.commit()
    return True

def get_null_blank_votes(db: Session):
    return db.query(models.VotesNull).first()
