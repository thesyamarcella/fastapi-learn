from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from .database import Base

class HistoriJadwal(Base):
    __tablename__ = "histori_jadwal"

    id_histori = Column(Integer, primary_key=True, index=True)
    id_jadwal = Column(Integer)
    tanggal_perubahan = Column(Date)
    aksi = Column(String(50))
    pengguna = Column(String(100))
    catatan = Column(Text)
