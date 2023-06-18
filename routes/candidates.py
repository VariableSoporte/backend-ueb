from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from repositories import candidates_repository as crud
import schemas.candidate as candidate_schema

candidate_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@candidate_router.get("/", response_model=list[candidate_schema.Candidate])
def read_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    candidates = crud.get_candidates(db, skip=skip, limit=limit)
    return candidates


@candidate_router.post("/", response_model=candidate_schema.Candidate)
def create_candidate(candidate: candidate_schema.CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = crud.create_candidate(db=db, candidate=candidate)
    return db_candidate
