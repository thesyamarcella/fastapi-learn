
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_room(room: schemas.RoomCreate, db: Session):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_room(room_id: int, db: Session):
    return db.query(models.Room).filter(models.Room.id == room_id).first()

def get_all_rooms(db: Session) -> List[models.Room]:
    return db.query(models.Room).all()

def update_room(room_id: int, room: schemas.RoomUpdate, db: Session):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        for var, value in vars(room).items():
            setattr(db_room, var, value) if value else None
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
    return db_room

def delete_room(room_id: int, db: Session):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room
