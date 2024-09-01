from pydantic import BaseModel
from datetime import datetime

class AccountBase(BaseModel):
    account_type: str
    balance: float
    customer_id: int

class AccountUpdate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    updated_at: datetime

    class Config:
        orm_mode = True