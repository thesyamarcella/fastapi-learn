from sqlalchemy import Column, Integer
from .database import Base

class TeachingAssignment(Base):
    __tablename__ = 'teaching_assignment'

    id_teaching_assignment = Column(Integer, primary_key=True, autoincrement=True)
    id_mata_kuliah = Column(Integer)
    id_dosen = Column(Integer)
    id_kelas = Column(Integer)
