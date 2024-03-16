from fastapi import FastAPI, Depends
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

@app.post("/histori_jadwal/", response_model=schemas.HistoriJadwal)
def create_histori_jadwal(histori_jadwal: schemas.HistoriJadwalCreate, db: Session = Depends(get_db)):
    return crud.create_histori_jadwal(histori_jadwal, db)

@app.get("/histori_jadwal/{histori_jadwal_id}", response_model=schemas.HistoriJadwal)
def read_histori_jadwal(histori_jadwal_id: int, db: Session = Depends(get_db)):
    return crud.get_histori_jadwal(histori_jadwal_id, db)

@app.get("/histori_jadwal/", response_model=List[schemas.HistoriJadwal])
def read_all_histori_jadwal(db: Session = Depends(get_db)):
    return crud.get_all_histori_jadwal(db)

@app.put("/histori_jadwal/{histori_jadwal_id}", response_model=schemas.HistoriJadwal)
def update_histori_jadwal(histori_jadwal_id: int, histori_jadwal: schemas.HistoriJadwalUpdate, db: Session = Depends(get_db)):
    return crud.update_histori_jadwal(histori_jadwal_id, histori_jadwal, db)

@app.delete("/histori_jadwal/{histori_jadwal_id}", response_model=schemas.HistoriJadwal)
def delete_histori_jadwal(histori_jadwal_id: int, db: Session = Depends(get_db)):
    return crud.delete_histori_jadwal(histori_jadwal_id, db)
