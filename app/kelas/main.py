# main.py

from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
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

@app.get("/kelas/{kelas_id}", response_model=schemas.Kelas)
def read_kelas(kelas_id: int, db: Session = Depends(get_db)):
    return crud.get_kelas(kelas_id, db)

@app.post("/kelas/", response_model=schemas.Kelas)
def create_kelas(user: schemas.KelasCreate, db: Session = Depends(get_db)):
    return crud.create_kelas(user, db)

@app.get("/kelas/", response_model=List[schemas.Kelas])
def read_kelas(db: Session = Depends(get_db)):
    kelas = crud.get_all_kelas(db)
    return kelas

@app.put("/kelas/{kelas_id}", response_model=schemas.Kelas)
def update_kelas(kelas_id: int, kelas: schemas.KelasUpdate, db: Session = Depends(get_db)):
    return crud.update_kelas(kelas_id, kelas, db)

@app.delete("/kelas/{kelas_id}", response_model=schemas.Kelas)
def delete_kelas(kelas_id: int, db: Session = Depends(get_db)):
    return crud.delete_kelas(kelas_id, db)


