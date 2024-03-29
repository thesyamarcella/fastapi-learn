

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


@app.get("/rooms/{room_id}", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    return crud.get_room(room_id, db)

@app.post("/rooms/", response_model=schemas.Room)
def create_room(user: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(user, db)

@app.get("/rooms/", response_model=List[schemas.Room])
def read_rooms(db: Session = Depends(get_db)):
    rooms = crud.get_all_rooms(db)
    return rooms

@app.put("/rooms/{room_id}", response_model=schemas.Room)
def update_room(room_id: int, room: schemas.RoomUpdate, db: Session = Depends(get_db)):
    return crud.update_room(room_id, room, db)

@app.delete("/rooms/{room_id}", response_model=schemas.Room)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    return crud.delete_room(room_id, db)