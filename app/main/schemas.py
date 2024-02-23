from pydantic import BaseModel
from typing import List, Optional
class RoomBase(BaseModel):
    name: str
    capacity: int
    is_available: Optional[bool] = True

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True

class RoomUpdate(RoomBase):
    id: int
    
class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    name: str

class User(UserBase):
    id: int
    room_id: Optional[int]

    class Config:
        orm_mode = True
        
        
