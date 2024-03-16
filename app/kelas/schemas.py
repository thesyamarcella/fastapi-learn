from pydantic import BaseModel
from typing import List, Optional

class KelasBase(BaseModel):
    nama_kelas: str
    kuota: int
    id_prodi: int
    id_dosen_wali: int
    inisial: str
    nama: str

class KelasCreate(KelasBase):
    pass

class Kelas(KelasBase):
    id: int

    class Config:
        orm_mode = True

class KelasUpdate(KelasBase):
    id: int

class UserBase(BaseModel):
    nama_kelas: str
    kuota: int
    id_prodi: int
    id_dosen_wali: int
    inisial: str
    nama: str
