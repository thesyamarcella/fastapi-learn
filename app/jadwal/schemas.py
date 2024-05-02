from pydantic import BaseModel
from typing import List, Optional

class JadwalBase(BaseModel):
    id_mata_kuliah: int
    id_dosen: int
    id_ruangan: int
    hari: str
    jam_mulai: str
    jam_selesai: str

class JadwalCreate(JadwalBase):
    pass

class Jadwal(JadwalBase):
    id_jadwal: int

    class Config:
        orm_mode = True

class JadwalUpdate(JadwalBase):
    pass
