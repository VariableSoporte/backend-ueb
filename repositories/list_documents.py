from schemas.list_documents import ListDocumentCreate
from sqlalchemy.orm import Session
from models import models


def create_list_document(db: Session, list_document: ListDocumentCreate):
    db_list_document = models.ListDocument(**list_document.dict())
    db.add(db_list_document)
    db.commit()
    db.refresh(db_list_document)
    return db_list_document


def get_list_documents_by_list(db: Session, list_id: int):
    return db.query(models.ListDocument).filter(models.ListDocument.list_id == list_id).all()


def update_list_document(db: Session, list_document_id: int, file: str):
    db.query(models.ListDocument).filter(
        models.ListDocument.id == list_document_id).update({"file": file})
    db.commit()
    return db.query(models.ListDocument).filter(models.ListDocument.id == list_document_id).first()


def delete_list_document(db: Session, list_document_id: int):
    db.query(models.ListDocument).filter(
        models.ListDocument.id == list_document_id).delete()
    db.commit()
    return True


def get_list_document(db: Session, list_document_id: int):
    return db.query(models.ListDocument).filter(models.ListDocument.id == list_document_id).first()


def update_list_document(db: Session, list_document_id: int, document: str):
    db.query(models.ListDocument).filter(
        models.ListDocument.id == list_document_id).update({"document": document})
    db.commit()
    return db.query(models.ListDocument).filter(models.ListDocument.id == list_document_id).first()


def delete_list_document(db: Session, list_document_id: int):
    db.query(models.ListDocument).filter(
        models.ListDocument.id == list_document_id).delete()
    db.commit()
    return True
