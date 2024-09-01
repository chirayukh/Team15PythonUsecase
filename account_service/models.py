from sqlalchemy import Column, Integer, String
from .database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_type = Column(String, index=True)
    balance = Column(Float)
    customer_id = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow)