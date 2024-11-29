from pydantic import BaseModel,validator, EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    address: str
    state: str
    country: str
    dob: date
    contact_no: int

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    full_name: str
    address: str
    state: str
    country: str
    dob: date
    contact_no: int
    disabled: bool    

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    address: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    dob: Optional[date] = None
    contact_no: Optional[int] = None
    disabled: Optional[bool] = None  

class User(UserBase):
    id: int

    class Config:
        orm_mode = True      