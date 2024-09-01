from pydantic import BaseModel
from datetime import datetime

class LoanBase(BaseModel):
    loan_type: str
    amount: float
    interest_rate: float
    duration_months: int
    customer_id: int

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    applied_on: datetime

    class Config:
        orm_mode = True