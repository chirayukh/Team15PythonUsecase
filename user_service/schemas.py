from pydantic import BaseModel,validator
from datetime import date

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

class User(UserBase):
    id: int

    class Config:
        orm_mode = True      