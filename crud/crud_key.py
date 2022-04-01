from sqlalchemy.orm import Session

import models
import schemas


def get_keys_by_project_id(db: Session, project_id: str):
    return db.query(models.Key).filter(models.Key.project_id == project_id).all()


def get_keys_by_page_id(db: Session, page_id: str):
    return db.query(models.Key).filter(models.Key.page_id == page_id).all()


def get_key(db: Session):
    return db.query(models.Key).all()


def create_key(db: Session, key: schemas.KeyCreate):
    db_key = models.Key(**key.dict())
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key


def delete_key(db: Session, key: str):
    db_key = db.query(models.Key).filter(models.Key.key == key).delete()
    db.commit()
    return db_key
