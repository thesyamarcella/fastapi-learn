from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from fastapi import UploadFile


class Dosen(Base):
    __tablename__ = "dosen"

    id = Column(Integer, primary_key=True, index=True)
    nip = Column(String(19))
    nidn = Column(String(10))
    id_pegawai = Column(Integer)
    inisial = Column(String(3))
    gelar_depan = Column(String(11))
    nama_depan = Column(String(27))
    nama_belakang = Column(String(14))
    gelar_belakang = Column(String(65))
    alamat = Column(String(110))
    agama = Column(String(12))
    telp_seluler = Column(String(27))

