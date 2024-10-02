from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new account
@app.post("/accounts/", status_code=status.HTTP_201_CREATED,response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db=db, account=account)

# Update an existing account
@app.put("/accounts/{customer_id}", response_model=schemas.Account)
def update_account(customer_id: int, account_data: schemas.AccountUpdate, db: Session = Depends(get_db)):
    return crud.update_account(db=db, customer_id=customer_id, account_data=account_data)

# Get account details by ID
@app.get("/accounts/{customer_id}", response_model=schemas.Account)
def get_account(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_account(db=db, customer_id=customer_id)