from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    loan_type = Column(String, index=True)
    amount = Column(Float)
    interest_rate = Column(Float)
    duration_months = Column(Integer)
    applied_on = Column(DateTime, default=datetime.utcnow)
    customer_id = Column(Integer)