from sqlalchemy.orm import Session
import models

def login(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.username == username, models.User.password == password).first()