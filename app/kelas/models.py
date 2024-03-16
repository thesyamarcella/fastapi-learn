from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Kelas(Base):
    __tablename__ = 'kelas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_kelas = Column(String(10))
    kuota = Column(Integer)
    id_prodi = Column(Integer)
    nama_prodi = Column(String(22))
    id_dosen_wali = Column(Integer)
    inisial = Column(String(3))
    nama = Column(String(36))

