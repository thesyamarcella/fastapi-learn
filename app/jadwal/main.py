from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/jadwal/{jadwal_id}", response_model=schemas.Jadwal)
def read_jadwal(jadwal_id: int, db: Session = Depends(get_db)):
    return crud.get_jadwal(jadwal_id, db)

@app.post("/jadwal/", response_model=schemas.Jadwal)
def create_jadwal(jadwal: schemas.JadwalCreate, db: Session = Depends(get_db)):
    return crud.create_jadwal(jadwal, db)

@app.get("/jadwal/", response_model=List[schemas.Jadwal])
def read_jadwals(db: Session = Depends(get_db)):
    jadwals = crud.get_all_jadwal(db)
    return jadwals

@app.put("/jadwal/{jadwal_id}", response_model=schemas.Jadwal)
def update_jadwal(jadwal_id: int, jadwal: schemas.JadwalUpdate, db: Session = Depends(get_db)):
    return crud.update_jadwal(jadwal_id, jadwal, db)

@app.delete("/jadwal/{jadwal_id}", response_model=schemas.Jadwal)
def delete_jadwal(jadwal_id: int, db: Session = Depends(get_db)):
    return crud.delete_jadwal(jadwal_id, db)
