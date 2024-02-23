from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from fastapi import UploadFile

# class File(Base):
#     __tablename__ = "files"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), index=True)
#     contents = Column(LargeBinary)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    age = Column(Integer)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship("Room", back_populates="users")

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    capacity = Column(Integer)
    is_available = Column(Boolean, default=True)
    users = relationship("User", back_populates="room")
