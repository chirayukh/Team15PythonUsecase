from fastapi import FastAPI, Depends,status
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

@app.post("/apply-loan/",status_code=status.HTTP_201_CREATED)
def apply_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return crud.create_loan(db=db, loan=loan)

@app.get("/loans/{customer_id}")
def get_loan(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_loan_by_customer_Id(db=db, customer_id=customer_id)


@app.put("/loans/{customer_id}/{loanno}")
def update_loan(customer_id: int,loanno: str ,loan_data: schemas.LoanUpdate,db: Session = Depends(get_db)):
    return crud.update_loan(db=db, customer_id=customer_id,loan_no=loanno, loan_data=loan_data)




