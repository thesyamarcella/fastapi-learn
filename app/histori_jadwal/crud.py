from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_histori_jadwal(histori_jadwal: schemas.HistoriJadwalCreate, db: Session):
    db_histori_jadwal = models.HistoriJadwal(**histori_jadwal.dict())
    db.add(db_histori_jadwal)
    db.commit()
    db.refresh(db_histori_jadwal)
    return db_histori_jadwal

def get_histori_jadwal(histori_jadwal_id: int, db: Session):
    return db.query(models.HistoriJadwal).filter(models.HistoriJadwal.id_histori == histori_jadwal_id).first()

def get_all_histori_jadwal(db: Session) -> List[models.HistoriJadwal]:
    return db.query(models.HistoriJadwal).all()

def update_histori_jadwal(histori_jadwal_id: int, histori_jadwal: schemas.HistoriJadwalUpdate, db: Session):
    db_histori_jadwal = db.query(models.HistoriJadwal).filter(models.HistoriJadwal.id_histori == histori_jadwal_id).first()
    if db_histori_jadwal:
        for var, value in vars(histori_jadwal).items():
            setattr(db_histori_jadwal, var, value) if value else None
        db.add(db_histori_jadwal)
        db.commit()
        db.refresh(db_histori_jadwal)
    return db_histori_jadwal

def delete_histori_jadwal(histori_jadwal_id: int, db: Session):
    db_histori_jadwal = db.query(models.HistoriJadwal).filter(models.HistoriJadwal.id_histori == histori_jadwal_id).first()
    if db_histori_jadwal:
        db.delete(db_histori_jadwal)
        db.commit()
    return db_histori_jadwal
