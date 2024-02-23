
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_user(user: schemas.UserCreate, db: Session):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()

def update_user(user_id: int, user: schemas.UserUpdate, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

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
