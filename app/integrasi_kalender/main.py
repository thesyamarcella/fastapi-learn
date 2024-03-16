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

@app.get("/integrasi_kalender/{integrasi_kalender_id}", response_model=schemas.IntegrasiKalender)
def read_integrasi_kalender(integrasi_kalender_id: int, db: Session = Depends(get_db)):
    return crud.get_integrasi_kalender(integrasi_kalender_id, db)

@app.post("/integrasi_kalender/", response_model=schemas.IntegrasiKalender)
def create_integrasi_kalender(integrasi_kalender: schemas.IntegrasiKalenderCreate, db: Session = Depends(get_db)):
    return crud.create_integrasi_kalender(integrasi_kalender, db)

@app.get("/integrasi_kalender/", response_model=List[schemas.IntegrasiKalender])
def read_integrasi_kalenders(db: Session = Depends(get_db)):
    return crud.get_all_integrasi_kalender(db)

@app.put("/integrasi_kalender/{integrasi_kalender_id}", response_model=schemas.IntegrasiKalender)
def update_integrasi_kalender(integrasi_kalender_id: int, integrasi_kalender: schemas.IntegrasiKalenderUpdate, db: Session = Depends(get_db)):
    return crud.update_integrasi_kalender(integrasi_kalender_id, integrasi_kalender, db)

@app.delete("/integrasi_kalender/{integrasi_kalender_id}", response_model=schemas.IntegrasiKalender)
def delete_integrasi_kalender(integrasi_kalender_id: int, db: Session = Depends(get_db)):
    return crud.delete_integrasi_kalender(integrasi_kalender_id, db)
