from fastapi import FastAPI, Depends
import models, schemas, crud
from database import engine, SessionLocal
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

@app.post("/apply-loan/")
def apply_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return crud.create_loan(db=db, loan=loan)

@app.get("/loans/{loan_id}")
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    return crud.get_loan(db=db, loan_id=loan_id)