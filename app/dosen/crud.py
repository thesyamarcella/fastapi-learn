
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_dosen(dosen: schemas.DosenCreate, db: Session):
    db_dosen = models.Dosen(**dosen.dict())
    db.add(db_dosen)
    db.commit()
    db.refresh(db_dosen)
    return db_dosen

def get_dosen(dosen_id: int, db: Session):
    return db.query(models.Dosen).filter(models.Dosen.id == dosen_id).first()

def get_all_dosens(db: Session) -> List[models.Dosen]:
    return db.query(models.Dosen).all()

def update_dosen(dosen_id: int, dosen: schemas.DosenUpdate, db: Session):
    db_dosen = db.query(models.Dosen).filter(models.Dosen.id == dosen_id).first()
    if db_dosen:
        for var, value in vars(dosen).items():
            setattr(db_dosen, var, value) if value else None
        db.add(db_dosen)
        db.commit()
        db.refresh(db_dosen)
    return db_dosen

def delete_dosen(dosen_id: int, db: Session):
    db_dosen = db.query(models.Dosen).filter(models.Dosen.id == dosen_id).first()
    if db_dosen:
        db.delete(db_dosen)
        db.commit()
    return db_dosen


