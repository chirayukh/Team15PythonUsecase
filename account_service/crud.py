from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException
import random

# Generate random account number
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

# Create an account
def create_account(db: Session, account: schemas.AccountCreate):
    account_number = generate_account_number()
    db_account = models.Account(
        account_number=account_number,
        account_type=account.account_type,
        balance=account.balance,
        customer_id =account.customer_id
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

# Update an account
def update_account(db: Session, customer_id: int, account_data: schemas.AccountUpdate):
    account = db.query(models.Account).filter(models.Account.customer_id== customer_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    if account_data.account_type:
        account.account_type = account_data.account_type
    if account_data.balance:
        account.balance = account_data.balance

    db.commit()
    db.refresh(account)
    return account

# Retrieve account by ID
def get_account(db: Session, customer_id: int):
    account = db.query(models.Account).filter(models.Account.customer_id == customer_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account