from pydantic import BaseModel
from typing import List, Optional
class DosenBase(BaseModel):
    
    nip: str
    nidn: str
    id_pegawai: int
    inisial: str
    gelar_depan: str
    nama_depan: str
    nama_belakang: str
    gelar_belakang: str
    alamat: str
    agama: str
    telp_seluler: str

class DosenCreate(DosenBase):
    pass

class Dosen(DosenBase):
    id: int

    class Config:
        orm_mode = True

class DosenUpdate(DosenBase):
    id: int
    
class DosenBase(BaseModel):
    nip: str
    nidn: str
    id_pegawai: int
    inisial: str
    gelar_depan: str
    nama_depan: str
    nama_belakang: str
    gelar_belakang: str
    alamat: str
    agama: str
    telp_seluler: str

        
