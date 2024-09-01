from fastapi import FastAPI, Depends
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

@app.put("/update-account/{account_id}")
def update_account(account_id: int, account: schemas.AccountUpdate, db: Session = Depends(get_db)):
    return crud.update_account(db=db, account_id=account_id, account=account)

@app.get("/account/{account_id}")
def get_account(account_id: int, db: Session = Depends(get_db)):
    return crud.get_account(db=db, account_id=account_id)