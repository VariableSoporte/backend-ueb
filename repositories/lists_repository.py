from schemas.list import ListCreate
from sqlalchemy.orm import Session
import models


def get_lists(db: Session, skip: int = 1, limit: int = 100):
    return db.query(models.List).all()

def create_list(db: Session, list: ListCreate):
    db_list = models.List(**list.dict())
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list
