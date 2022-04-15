from sqlalchemy.orm import Session

import models
import schemas


def create_key(db: Session, key: schemas.KeyCreate):
    db_key = models.Key(**key.dict())
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key


def get_key(db: Session, key: str):
    db_key = db.query(models.Key).filter(models.Key.key == key).first()
    return db_key


def get_keys(db: Session, current: int = 0, limit: int = 100):
    return db.query(models.Key).offset(current).limit(limit).all()


def get_keys_by_project_id(db: Session, project_id: int):
    return db.query(models.Key).filter(models.Key.project_id == project_id).all()


def get_keys_by_page_id(db: Session, page_id: int):
    return db.query(models.Key).filter(models.Key.page_id == page_id).all()


def delete_key(db: Session, key: str):
    db_key = db.query(models.Key).filter(models.Key.key == key).delete()
    db.commit()
    return db_key


def update_key(db: Session, key: schemas.Key):
    db_status = db.query(models.Key).filter(models.Key.key == key.key).update(key.dict())
    db.commit()
    return db_status
