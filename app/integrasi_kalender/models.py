from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from fastapi import UploadFile

class IntegrasiKalender(Base):
    __tablename__ = "integrasi_kalender"

    id_integrasi = Column(Integer, primary_key=True, index=True)
    id_pengguna_google = Column(String(100))
    id_dosen = Column(Integer)
    id_mahasiswa = Column(Integer)
    token_autentikasi = Column(String(256))

