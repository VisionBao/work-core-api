from sqlalchemy.orm import Session

import models
import schemas


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def get_project_by_symbol(db: Session, project_symbol: str):
    return db.query(models.Project).filter(models.Project.symbol == project_symbol).first()


def get_projects(db: Session, current: int = None, limit: int = None):
    if current:
        return db.query(models.Project).offset(current).limit(limit).all()
    return db.query(models.Project).all()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_status = db.query(models.Project).filter(models.Project.id == project_id).delete()
    db.commit()
    return db_status


def update_project(db: Session, project: schemas.Project):
    db_status = db.query(models.Project).filter(models.Project.id == project.id).update(project.dict())
    db.commit()
    return db_status
