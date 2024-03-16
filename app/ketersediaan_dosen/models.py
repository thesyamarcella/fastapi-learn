from sqlalchemy import Column, Integer, String, Time
from .database import Base

class KetersediaanDosen(Base):
    __tablename__ = "ketersediaan_dosen"

    id_preferensi = Column(Integer, primary_key=True, index=True)
    id_dosen = Column(Integer)
    hari = Column(String(20))
    jam_mulai = Column(Time)
    jam_selesai = Column(Time)
    preferensi = Column(String(20))
