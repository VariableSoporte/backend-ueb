from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from repositories import lists_repository as crud
import schemas.list as list_schema

list_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@list_router.get("/", response_model=list[list_schema.List])
def read_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lists = crud.get_lists(db, skip=skip, limit=limit)
    return lists

@list_router.post("/", response_model=list_schema.List)
def create_list(list: list_schema.ListCreate, db: Session = Depends(get_db)):
    db_list = crud.create_list(db=db, list=list)
    return db_list