from sqlalchemy import Column, Integer, String, Time
from .database import Base

class Jadwal(Base):
    __tablename__ = 'jadwal'

    id_jadwal = Column(Integer, primary_key=True, autoincrement=True)
    id_mata_kuliah = Column(Integer)
    id_dosen = Column(Integer)
    id_ruangan = Column(Integer)
    hari = Column(String(20))
    jam_mulai = Column(Time)
    jam_selesai = Column(Time)
