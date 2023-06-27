from schemas.candidate import CandidateCreate
from sqlalchemy.orm import Session
from models import models


def get_candidates(db: Session):
    return db.query(models.Candidate).where(models.Candidate.dignity_id == 1).all()


def get_candidates_by_list(db: Session, list_id: int):
    return db.query(models.Candidate).where(models.Candidate.list_id == list_id).all()


def get_candidate(db: Session, candidate_id: int):
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()


def create_candidate(db: Session, candidate: CandidateCreate):
    db_candidate = models.Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


def update_candidate(db: Session, candidate_id: int, file: str):
    db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id).update({"photo": file})
    db.commit()
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()


def delete_candidate(db: Session, candidate_id: int):
    db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id).delete()
    db.commit()
    return True


def update_candidate_by_id(db: Session, candidate_id: int, candidate: CandidateCreate):
    db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id).update(candidate.dict())
    db.commit()
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
