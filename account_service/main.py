from fastapi import FastAPI, Depends, HTTPException
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
@app.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db=db, account=account)

# Update an existing account
@app.put("/accounts/{account_id}", response_model=schemas.Account)
def update_account(account_id: int, account_data: schemas.AccountUpdate, db: Session = Depends(get_db)):
    return crud.update_account(db=db, account_id=account_id, account_data=account_data)

# Get account details by ID
@app.get("/accounts/{account_id}", response_model=schemas.Account)
def get_account(account_id: int, db: Session = Depends(get_db)):
    return crud.get_account(db=db, account_id=account_id)