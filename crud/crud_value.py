from sqlalchemy.orm import Session

import models
import schemas


def create_value(db: Session, project: schemas.ValueCreate):
    db_value = models.Project(**project.dict())
    db.add(db_value)
    db.commit()
    db.refresh(db_value)
    return db_value


def create_values(db: Session, value_list: list[schemas.ValueCreate]):
    db_value_list = []
    for value in value_list:
        db_value = models.Project(**value.dict())
        db_value_list.append(db_value)
    db.bulk_insert_mappings(db_value_list)
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
    return db.query(models.Value).filter(models.Value.key == key and models.Value.lang_id == lang_id).first()


def update_values(db: Session, value_list: list[schemas.Value]):
    db_value_list = []
    for value in value_list:
        db_value = models.Project(**value.dict())
        db_value_list.append(db_value)
    db.bulk_update_mappings(db_value_list)
    db.commit()
    return db_value_list