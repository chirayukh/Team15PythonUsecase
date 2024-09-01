from fastapi import FastAPI
from . import models, schemas, crud
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/login/")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.authenticate_user(db=db, user=user)