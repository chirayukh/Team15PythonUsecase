from sqlalchemy import Column, Integer, String, DateTime, Boolean,Date,BigInteger
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    first_name=Column(String,index=True,nullable=False)
    last_name=Column(String,index=True,nullable=False)
    full_name = Column(String,nullable=False)
    address= Column(String,nullable=False)
    state=Column(String,nullable=False)
    country= Column(String,nullable=False)
    dob = Column(Date, nullable=False) 
    contact_no= Column(BigInteger,unique=True, nullable=False) 
    disabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)