from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from fastapi import UploadFile

class Matkul(Base):
    __tablename__ = "mata_kuliah"
    
    id = Column(Integer, primary_key=True, index=True)
    nama_ruangan = Column(String(5), index=True)
    kapasitas = Column(Integer)
    nama_gedung = Column(String(25), index=True)
    id_mata_kuliah = Column(Integer)
    kd_mata_kuliah = Column(String(14))
    nama_mata_kuliah = Column(String(47))
    nama_mata_kuliah_english  = Column(String(84))  
    sks = Column(Integer)
    semester = Column(String(8))
    tingkat_mata_kuliah = Column(Integer)
    index_minimum = Column(String(8))
    id_program_studi  = Column(Integer)
    nama_prodi = Column(String(22))
    nama_prodi_en = Column(String(20))


