import json

from sqlalchemy.orm import Session

import models
import schemas


def create_value(db: Session, value: schemas.ValueCreate):
    db_value = models.Value(**value.dict())
    db.add(db_value)
    db.commit()
    db.refresh(db_value)
    return db_value


def create_values(db: Session, value_list: list[schemas.ValueCreate]):
    db_value_list = []
    for value in value_list:
        db_value = models.Value(**value.dict())
        db_value_list.append(db_value)
    db.bulk_save_objects(db_value_list)
    db.commit()
    return db_value_list


def get_values_by_key(db: Session, key: str):
    return db.query(models.Value).filter(models.Value.key == key).all()


def delete_value(db: Session, value_id: int):
    db_values = db.query(models.Value).filter(models.Value.id == value_id).delete(synchronize_session=False)
    db.commit()
    return db_values


def delete_value_by_key(db: Session, key: str):
    db_value = db.query(models.Value).filter(models.Value.key == key).delete()
    db.commit()
    return db_value


def get_value(db: Session, key: str, lang_id: int):
    return db.query(models.Value).filter(models.Value.key == key).filter(models.Value.lang_id == lang_id).first()


def update_values(db: Session, value_list: list[schemas.Value]):
    value_list_new = []
    for value in value_list:
        value_list_new.append(value.dict())
    if len(value_list) > 0:
        db.bulk_update_mappings(models.Value, value_list_new)
        db.commit()
    return value_list_new
