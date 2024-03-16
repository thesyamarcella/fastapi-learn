from pydantic import BaseModel
from typing import List, Optional
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    id: int
    
class UserBase(BaseModel):
    username: str
    password: str

        


