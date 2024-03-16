from pydantic import BaseModel
from typing import Optional

class HistoriJadwalBase(BaseModel):
    id_jadwal: int
    tanggal_perubahan: Optional[str]
    aksi: str
    pengguna: str
    catatan: Optional[str]

class HistoriJadwalCreate(HistoriJadwalBase):
    pass

class HistoriJadwalUpdate(HistoriJadwalBase):
    id_histori: int

class HistoriJadwal(HistoriJadwalBase):
    id_histori: int

    class Config:
        orm_mode = True
