from pydantic import BaseModel
from typing import List, Optional
class RoomBase(BaseModel):
    nama_ruangan: str
    kapasitas: int
    nama_gedung: str

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True

class RoomUpdate(RoomBase):
    id: int
    

        
