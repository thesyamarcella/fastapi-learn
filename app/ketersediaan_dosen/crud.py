from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_ketersediaan_dosen(ketersediaan_dosen: schemas.KetersediaanDosenCreate, db: Session):
    db_ketersediaan_dosen = models.KetersediaanDosen(**ketersediaan_dosen.dict())
    db.add(db_ketersediaan_dosen)
    db.commit()
    db.refresh(db_ketersediaan_dosen)
    return db_ketersediaan_dosen

def get_ketersediaan_dosen(ketersediaan_dosen_id: int, db: Session):
    return db.query(models.KetersediaanDosen).filter(models.KetersediaanDosen.id_preferensi == ketersediaan_dosen_id).first()

def get_all_ketersediaan_dosen(db: Session) -> List[models.KetersediaanDosen]:
    return db.query(models.KetersediaanDosen).all()

def update_ketersediaan_dosen(ketersediaan_dosen_id: int, ketersediaan_dosen: schemas.KetersediaanDosenUpdate, db: Session):
    db_ketersediaan_dosen = db.query(models.KetersediaanDosen).filter(models.KetersediaanDosen.id_preferensi == ketersediaan_dosen_id).first()
    if db_ketersediaan_dosen:
        for var, value in vars(ketersediaan_dosen).items():
            setattr(db_ketersediaan_dosen, var, value) if value else None
        db.add(db_ketersediaan_dosen)
        db.commit()
        db.refresh(db_ketersediaan_dosen)
    return db_ketersediaan_dosen

def delete_ketersediaan_dosen(ketersediaan_dosen_id: int, db: Session):
    db_ketersediaan_dosen = db.query(models.KetersediaanDosen).filter(models.KetersediaanDosen.id_preferensi == ketersediaan_dosen_id).first()
    if db_ketersediaan_dosen:
        db.delete(db_ketersediaan_dosen)
        db.commit()
    return db_ketersediaan_dosen
