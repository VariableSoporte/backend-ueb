from schemas.votes import VotesCreate
from sqlalchemy.orm import Session
import models

def get_votes(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.Votes).all()

def get_votes_by_list(db: Session, list_id: int):
    return db.query(models.Votes).filter(models.Votes.list_id == list_id).all()
