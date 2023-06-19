from fastapi import UploadFile, File
from schemas.candidate import CandidateCreate
from sqlalchemy.orm import Session
import models


def get_candidates(db: Session, skip: int = 1, limit: int = 100):
    # Para que se muestren solo los presidentes se debe usar un where
    return db.query(models.Candidate).where(models.Candidate.dignity_id == 1).all()

def get_candidates_by_list(db: Session, list_id: int):
    return db.query(models.Candidate).where(models.Candidate.list_id == list_id).all()


def create_candidate(db: Session, candidate: CandidateCreate):
    db_candidate = models.Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def update_candidate(db: Session, candidate_id: int, file: str):
    db.query(models.Candidate).filter(models.Candidate.id == candidate_id).update({"photo": file})
    db.commit()
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()

def get_candidate(db: Session, candidate_id: int):
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
    
