from sqlalchemy.orm import Session

import models


def get_languages(db: Session):
    return db.query(models.Language).all()


def get_language_by_id(db: Session, lang_id: int):
    return db.query(models.Language).filter(models.Language.id == lang_id).first()


def get_language_by_code(db: Session, lang_code: str):
    return db.query(models.Language).filter(models.Language.lang_code == lang_code).first()
