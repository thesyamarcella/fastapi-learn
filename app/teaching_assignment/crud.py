from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_teaching_assignment(teaching_assignment: schemas.TeachingAssignmentCreate, db: Session):
    db_teaching_assignment = models.TeachingAssignment(**teaching_assignment.dict())
    db.add(db_teaching_assignment)
    db.commit()
    db.refresh(db_teaching_assignment)
    return db_teaching_assignment

def get_teaching_assignment(teaching_assignment_id: int, db: Session):
    return db.query(models.TeachingAssignment).filter(models.TeachingAssignment.id_teaching_assignment == teaching_assignment_id).first()

def get_all_teaching_assignments(db: Session) -> List[models.TeachingAssignment]:
    return db.query(models.TeachingAssignment).all()

def update_teaching_assignment(teaching_assignment_id: int, teaching_assignment: schemas.TeachingAssignmentUpdate, db: Session):
    db_teaching_assignment = db.query(models.TeachingAssignment).filter(models.TeachingAssignment.id_teaching_assignment == teaching_assignment_id).first()
    if db_teaching_assignment:
        for var, value in vars(teaching_assignment).items():
            setattr(db_teaching_assignment, var, value) if value else None
        db.add(db_teaching_assignment)
        db.commit()
        db.refresh(db_teaching_assignment)
    return db_teaching_assignment

def delete_teaching_assignment(teaching_assignment_id: int, db: Session):
    db_teaching_assignment = db.query(models.TeachingAssignment).filter(models.TeachingAssignment.id_teaching_assignment == teaching_assignment_id).first()
    if db_teaching_assignment:
        db.delete(db_teaching_assignment)
        db.commit()
    return db_teaching_assignment
