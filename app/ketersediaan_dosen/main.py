from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ketersediaan_dosen/", response_model=schemas.KetersediaanDosen)
def create_ketersediaan_dosen(ketersediaan_dosen: schemas.KetersediaanDosenCreate, db: Session = Depends(get_db)):
    return crud.create_ketersediaan_dosen(ketersediaan_dosen, db)

@app.get("/ketersediaan_dosen/{ketersediaan_dosen_id}", response_model=schemas.KetersediaanDosen)
def read_ketersediaan_dosen(ketersediaan_dosen_id: int, db: Session = Depends(get_db)):
    return crud.get_ketersediaan_dosen(ketersediaan_dosen_id, db)

@app.get("/ketersediaan_dosen/", response_model=List[schemas.KetersediaanDosen])
def read_all_ketersediaan_dosen(db: Session = Depends(get_db)):
    return crud.get_all_ketersediaan_dosen(db)

@app.put("/ketersediaan_dosen/{ketersediaan_dosen_id}", response_model=schemas.KetersediaanDosen)
def update_ketersediaan_dosen(ketersediaan_dosen_id: int, ketersediaan_dosen: schemas.KetersediaanDosenUpdate, db: Session = Depends(get_db)):
    return crud.update_ketersediaan_dosen(ketersediaan_dosen_id, ketersediaan_dosen, db)

@app.delete("/ketersediaan_dosen/{ketersediaan_dosen_id}", response_model=schemas.KetersediaanDosen)
def delete_ketersediaan_dosen(ketersediaan_dosen_id: int, db: Session = Depends(get_db)):
    return crud.delete_ketersediaan_dosen(ketersediaan_dosen_id, db)
