from fastapi import APIRouter, Depends
import schemas.student as student_schema

from database import SessionLocal

from repositories import students_repository as crud
from sqlalchemy.orm import Session

test_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @test_router.get("/voters")
# def test():
#     return True


@test_router.get("/voters/")
def read_voters(db: Session = Depends(get_db)):
    voters = crud.get_voters(db)
    return voters

@test_router.get("/{identification_card}")
def read_student(identification_card: str, db: Session = Depends(get_db)):
    # return identification_card
    db_student = crud.get_student_by_identification_card(
        db, identification_card=identification_card)
    return db_student

@test_router.get("/pending-voters/")
def read_pending_voters(db: Session = Depends(get_db)):
    voters = crud.get_pending_voters(db)
    return voters
