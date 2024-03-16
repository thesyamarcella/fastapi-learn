from pydantic import BaseModel
from typing import Optional

class KetersediaanDosenBase(BaseModel):
    id_dosen: int
    hari: str
    jam_mulai: str
    jam_selesai: str
    preferensi: Optional[str] = None

class KetersediaanDosenCreate(KetersediaanDosenBase):
    pass

class KetersediaanDosen(KetersediaanDosenBase):
    id_preferensi: int

    class Config:
        orm_mode = True

class KetersediaanDosenUpdate(KetersediaanDosenBase):
    pass
