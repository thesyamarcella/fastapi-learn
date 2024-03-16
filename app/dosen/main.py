# main.py
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

@app.get("/dosen/{dosen_id}", response_model=schemas.Dosen)
def read_dosen(dosen_id: int, db: Session = Depends(get_db)):
    return crud.get_dosen(dosen_id, db)

@app.post("/dosen/", response_model=schemas.Dosen)
def create_dosen(user: schemas.DosenCreate, db: Session = Depends(get_db)):
    return crud.create_dosen(user, db)

@app.get("/dosen/", response_model=List[schemas.Dosen])
def read_dosens(db: Session = Depends(get_db)):
    dosens = crud.get_all_dosens(db)
    return dosens

@app.put("/dosen/{dosen_id}", response_model=schemas.Dosen)
def update_dosen(dosen_id: int, dosen: schemas.DosenUpdate, db: Session = Depends(get_db)):
    return crud.update_dosen(dosen_id, dosen, db)

@app.delete("/dosen/{dosen_id}", response_model=schemas.Dosen)
def delete_dosen(dosen_id: int, db: Session = Depends(get_db)):
    return crud.delete_dosen(dosen_id, db)

