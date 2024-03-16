
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_kelas(kelas: schemas.KelasCreate, db: Session):
    db_kelas = models.Kelas(**kelas.dict())
    db.add(db_kelas)
    db.commit()
    db.refresh(db_kelas)
    return db_kelas

def get_kelas(kelas_id: int, db: Session):
    return db.query(models.Kelas).filter(models.Kelas.id == kelas_id).first()

def get_all_kelas(db: Session) -> List[models.Kelas]:
    return db.query(models.Kelas).all()

def update_kelas(kelas_id: int, kelas: schemas.KelasUpdate, db: Session):
    db_kelas = db.query(models.Kelas).filter(models.Kelas.id == kelas_id).first()
    if db_kelas:
        for var, value in vars(kelas).items():
            setattr(db_kelas, var, value) if value else None
        db.add(db_kelas)
        db.commit()
        db.refresh(db_kelas)
    return db_kelas

def delete_kelas(kelas_id: int, db: Session):
    db_kelas = db.query(models.Kelas).filter(models.Kelas.id == kelas_id).first()
    if db_kelas:
        db.delete(db_kelas)
        db.commit()
    return db_kelas



