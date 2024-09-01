from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    full_name: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    full_name: str

    class Config:
        orm_mode = True