from schemas.dignity import DignityCreate
from sqlalchemy.orm import Session
from models import models


def get_dignities(db: Session):
    return db.query(models.Dignity).all()


def create_dignity(db: Session, dignity: DignityCreate):
    db_dignity = models.Dignity(**dignity.dict())
    db.add(db_dignity)
    db.commit()
    db.refresh(db_dignity)
    return db_dignity

