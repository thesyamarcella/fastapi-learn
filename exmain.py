from fastapi import FastAPI, HTTPException
from typing import List
from fastapi import Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Inisialisasi FastAPI
app = FastAPI()

# Koneksi ke database MySQL menggunakan SQLAlchemy
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_learn"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Deklarasi Base untuk model
Base = declarative_base()

# Model untuk Room
class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    capacity = Column(Integer)
    is_available = Column(Boolean, default=True)

# Membuat tabel di database
Base.metadata.create_all(bind=engine)

# Kelas Pydantic untuk validasi data ruangan
class RoomCreate(BaseModel):
    name: str
    capacity: int
    is_available: bool = True

# Kelas Pydantic untuk validasi respon
class RoomOut(BaseModel):
    id: int
    name: str
    capacity: int
    is_available: bool

# Membuat SessionLocal untuk setiap request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fungsi untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint untuk membuat ruangan baru
@app.post("/rooms/", response_model=RoomOut)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# Endpoint untuk mendapatkan semua ruangan
@app.get("/rooms/", response_model=List[RoomOut])
def get_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    rooms = db.query(Room).offset(skip).limit(limit).all()
    return rooms

# Endpoint untuk mendapatkan ruangan berdasarkan ID
@app.get("/rooms/{room_id}", response_model=RoomOut)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
