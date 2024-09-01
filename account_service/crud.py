from sqlalchemy.orm import Session
from . import models, schemas

def update_account(db: Session, account_id: int, account: schemas.AccountUpdate):
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if db_account:
        for key, value in account.dict().items():
            setattr(db_account, key, value)
        db.commit()
        db.refresh(db_account)
    return db_account

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()