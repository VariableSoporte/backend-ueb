from schemas.votes import VotesCreate
from sqlalchemy.orm import Session
import models
from repositories import students_repository as crud_students

def get_votes(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Votes).all()

def get_votes_by_list(db: Session, list_id: int):
    return db.query(models.Votes).filter(models.Votes.list_id == list_id).all()

def vote(db: Session, student: int, list_id: int):
    # db.query(models.Votes).filter(models.Votes.student == student).update({"list_id": list_id})
    # db.commit()
    # return db.query(models.Votes).filter(models.Votes.student == student).first()
    crud_students.update_student_can_vote(db, student, False)
    db.query(models.Votes).filter(models.Votes.list_id == list_id).update({"votes": models.Votes.votes + 1})
    db.commit()
    return True
