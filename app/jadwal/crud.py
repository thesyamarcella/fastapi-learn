from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_jadwal(jadwal: schemas.JadwalCreate, db: Session):
    db_jadwal = models.Jadwal(**jadwal.dict())
    db.add(db_jadwal)
    db.commit()
    db.refresh(db_jadwal)
    return db_jadwal

def get_jadwal(jadwal_id: int, db: Session):
    return db.query(models.Jadwal).filter(models.Jadwal.id_jadwal == jadwal_id).first()

def get_all_jadwal(db: Session) -> List[models.Jadwal]:
    return db.query(models.Jadwal).all()

def update_jadwal(jadwal_id: int, jadwal: schemas.JadwalUpdate, db: Session):
    db_jadwal = db.query(models.Jadwal).filter(models.Jadwal.id_jadwal == jadwal_id).first()
    if db_jadwal:
        for var, value in vars(jadwal).items():
            setattr(db_jadwal, var, value) if value else None
        db.add(db_jadwal)
        db.commit()
        db.refresh(db_jadwal)
    return db_jadwal

def delete_jadwal(jadwal_id: int, db: Session):
    db_jadwal = db.query(models.Jadwal).filter(models.Jadwal.id_jadwal == jadwal_id).first()
    if db_jadwal:
        db.delete(db_jadwal)
        db.commit()
    return db_jadwal
