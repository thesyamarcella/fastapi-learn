from pydantic import BaseModel
from typing import List, Optional

class TeachingAssignmentBase(BaseModel):
    id_mata_kuliah: int
    id_dosen: int
    id_kelas: int

class TeachingAssignmentCreate(TeachingAssignmentBase):
    pass

class TeachingAssignment(TeachingAssignmentBase):
    id_teaching_assignment: int

    class Config:
        orm_mode = True

class TeachingAssignmentUpdate(TeachingAssignmentBase):
    pass
