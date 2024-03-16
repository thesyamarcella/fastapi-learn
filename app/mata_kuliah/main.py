
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

@app.get("/matkuls/{matkul_id}", response_model=schemas.Matkul)
def read_matkul(matkul_id: int, db: Session = Depends(get_db)):
    return crud.get_matkul(matkul_id, db)

@app.post("/matkuls/", response_model=schemas.Matkul)
def create_matkul(user: schemas.MatkulCreate, db: Session = Depends(get_db)):
    return crud.create_matkul(user, db)

@app.get("/matkuls/", response_model=List[schemas.Matkul])
def read_matkuls(db: Session = Depends(get_db)):
    matkuls = crud.get_all_matkuls(db)
    return matkuls

@app.put("/matkuls/{matkul_id}", response_model=schemas.Matkul)
def update_matkul(matkul_id: int, matkul: schemas.MatkulUpdate, db: Session = Depends(get_db)):
    return crud.update_matkul(matkul_id, matkul, db)

@app.delete("/matkuls/{matkul_id}", response_model=schemas.Matkul)
def delete_matkul(matkul_id: int, db: Session = Depends(get_db)):
    return crud.delete_matkul(matkul_id, db)

