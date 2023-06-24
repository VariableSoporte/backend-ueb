from schemas.list import ListCreate
from sqlalchemy.orm import Session
from models import models


def get_lists(db: Session):
    return db.query(models.List).order_by(models.List.votes.desc()).all()


def get_lists_unorder(db: Session):
    return db.query(models.List).all()


def get_list(db: Session, list_id: int):
    return db.query(models.List).filter(models.List.id == list_id).first()


def create_list(db: Session, list: ListCreate):
    db_list = models.List(**list.dict())
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


def update_list_logo(db: Session, list_id: int, file: str):
    db.query(models.List).filter(
        models.List.id == list_id).update({"logo": file})
    db.commit()
    return db.query(models.List).filter(models.List.id == list_id).first()


def update_list(db: Session, list_id: int, list: ListCreate):
    db.query(models.List).filter(models.List.id == list_id).update(
        {"name": list.name})
    list = db.query(models.List).filter(models.List.id == list_id).first()
    db.commit()
    return list


def delete_list(db: Session, list_id: int):
    db.query(models.List).filter(models.List.id == list_id).delete()
    db.commit()
    return True
