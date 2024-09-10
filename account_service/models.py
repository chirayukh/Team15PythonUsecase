from sqlalchemy import Column, Integer, String, Float
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)
    balance = Column(Float, default=0.0)
    owner_id = Column(Integer)  # Foreign key to a User (if needed)