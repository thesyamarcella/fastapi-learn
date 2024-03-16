from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from fastapi import UploadFile


class Room(Base):
    __tablename__ = "ruangan"

    id = Column(Integer, primary_key=True, index=True)
    nama_ruangan = Column(String(5), index=True)
    kapasitas = Column(Integer)
    nama_gedung = Column(String(25), index=True)

