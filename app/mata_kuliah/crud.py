
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_matkul(matkul: schemas.MatkulCreate, db: Session):
    db_matkul = models.Matkul(**matkul.dict())
    db.add(db_matkul)
    db.commit()
    db.refresh(db_matkul)
    return db_matkul

def get_matkul(matkul_id: int, db: Session):
    return db.query(models.Matkul).filter(models.Matkul.id == matkul_id).first()

def get_all_matkuls(db: Session) -> List[models.Matkul]:
    return db.query(models.Matkul).all()

def update_matkul(matkul_id: int, matkul: schemas.MatkulUpdate, db: Session):
    db_matkul = db.query(models.Matkul).filter(models.Matkul.id == matkul_id).first()
    if db_matkul:
        for var, value in vars(matkul).items():
            setattr(db_matkul, var, value) if value else None
        db.add(db_matkul)
        db.commit()
        db.refresh(db_matkul)
    return db_matkul

def delete_matkul(matkul_id: int, db: Session):
    db_matkul = db.query(models.Matkul).filter(models.Matkul.id == matkul_id).first()
    if db_matkul:
        db.delete(db_matkul)
        db.commit()
    return db_matkul


