from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from repositories import dignities as crud
import schemas.dignity as dignity_schema

dignity_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@dignity_router.get("/", response_model=list[dignity_schema.Dignity])
def read_dignities(db: Session = Depends(get_db)):
    dignities = crud.get_dignities(db)
    return dignities


@dignity_router.post("/", response_model=dignity_schema.Dignity)
def create_dignity(dignity: dignity_schema.DignityCreate, db: Session = Depends(get_db)):
    db_dignity = crud.create_dignity(db=db, dignity=dignity)
    return db_dignity
