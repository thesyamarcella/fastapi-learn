from pydantic import BaseModel
from typing import List, Optional
class MatkulBase(BaseModel):
    id_mata_kuliah:	int
    kd_mata_kuliah: str
    nama_mata_kuliah: str
    nama_mata_kuliah_english: str	
    sks: int
    semester: str
    tingkat_mata_kuliah: int
    index_minimum: str
    id_program_studi: int
    nama_prodi: str
    nama_prodi_en: str

class MatkulCreate(MatkulBase):
    pass

class Matkul(MatkulBase):
    id: int

    class Config:
        orm_mode = True

class MatkulUpdate(MatkulBase):
    id: int
    
class MatkulBase(BaseModel):
    id_mata_kuliah:	int
    kd_mata_kuliah: str
    nama_mata_kuliah: str
    nama_mata_kuliah_english: str	
    sks: int
    semester: str
    tingkat_mata_kuliah: int
    index_minimum: str
    id_program_studi: int
    nama_prodi: str
    nama_prodi_en: str

        


