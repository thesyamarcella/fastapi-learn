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


@app.get("/teaching_assignments/{teaching_assignment_id}", response_model=schemas.TeachingAssignment)
def read_teaching_assignment(teaching_assignment_id: int, db: Session = Depends(get_db)):
    return crud.get_teaching_assignment(teaching_assignment_id, db)

@app.post("/teaching_assignments/", response_model=schemas.TeachingAssignment)
def create_teaching_assignment(teaching_assignment: schemas.TeachingAssignmentCreate, db: Session = Depends(get_db)):
    return crud.create_teaching_assignment(teaching_assignment, db)

@app.get("/teaching_assignments/", response_model=List[schemas.TeachingAssignment])
def read_teaching_assignments(db: Session = Depends(get_db)):
    teaching_assignments = crud.get_all_teaching_assignments(db)
    return teaching_assignments

@app.put("/teaching_assignments/{teaching_assignment_id}", response_model=schemas.TeachingAssignment)
def update_teaching_assignment(teaching_assignment_id: int, teaching_assignment: schemas.TeachingAssignmentUpdate, db: Session = Depends(get_db)):
    return crud.update_teaching_assignment(teaching_assignment_id, teaching_assignment, db)

@app.delete("/teaching_assignments/{teaching_assignment_id}", response_model=schemas.TeachingAssignment)
def delete_teaching_assignment(teaching_assignment_id: int, db: Session = Depends(get_db)):
    return crud.delete_teaching_assignment(teaching_assignment_id, db)
