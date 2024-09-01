from sqlalchemy.orm import Session
from . import models, schemas
from .utils import get_password_hash, verify_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user and verify_password(user.password, db_user.hashed_password):
        return db_user
    return None