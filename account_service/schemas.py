from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    account_type: str
    balance: Optional[float] = 0.0
    owner_id: int  # Reference to the user who owns the account

class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    account_type: Optional[str] = None
    balance: Optional[float] = None

class Account(AccountBase):
    id: int
    account_number: str

    class Config:
        orm_mode = True