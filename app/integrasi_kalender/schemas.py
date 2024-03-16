from pydantic import BaseModel
from typing import Optional

class IntegrasiKalenderBase(BaseModel):
    id_pengguna_google: str
    id_dosen: int
    id_mahasiswa: int
    token_autentikasi: str

class IntegrasiKalenderCreate(IntegrasiKalenderBase):
    pass

class IntegrasiKalender(IntegrasiKalenderBase):
    id_integrasi: int

    class Config:
        orm_mode = True

class IntegrasiKalenderUpdate(IntegrasiKalenderBase):
    id_integrasi: int
