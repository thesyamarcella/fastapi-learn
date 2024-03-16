
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_integrasi_kalender(integrasi_kalender: schemas.IntegrasiKalenderCreate, db: Session):
    db_integrasi_kalender = models.IntegrasiKalender(**integrasi_kalender.dict())
    db.add(db_integrasi_kalender)
    db.commit()
    db.refresh(db_integrasi_kalender)
    return db_integrasi_kalender

def get_integrasi_kalender(integrasi_kalender_id: int, db: Session):
    return db.query(models.IntegrasiKalender).filter(models.IntegrasiKalender.id_integrasi == integrasi_kalender_id).first()

def get_all_integrasi_kalender(db: Session) -> List[models.IntegrasiKalender]:
    return db.query(models.IntegrasiKalender).all()

def update_integrasi_kalender(integrasi_kalender_id: int, integrasi_kalender: schemas.IntegrasiKalenderUpdate, db: Session):
    db_integrasi_kalender = db.query(models.IntegrasiKalender).filter(models.IntegrasiKalender.id_integrasi == integrasi_kalender_id).first()
    if db_integrasi_kalender:
        for var, value in vars(integrasi_kalender).items():
            setattr(db_integrasi_kalender, var, value) if value else None
        db.add(db_integrasi_kalender)
        db.commit()
        db.refresh(db_integrasi_kalender)
    return db_integrasi_kalender

def delete_integrasi_kalender(integrasi_kalender_id: int, db: Session):
    db_integrasi_kalender = db.query(models.IntegrasiKalender).filter(models.IntegrasiKalender.id_integrasi == integrasi_kalender_id).first()
    if db_integrasi_kalender:
        db.delete(db_integrasi_kalender)
        db.commit()
    return db_integrasi_kalender
