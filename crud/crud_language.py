from sqlalchemy.orm import Session

import models


def get_languages(db: Session):
    return db.query(models.Language).all()


def get_language(db: Session, lang_id: int):
    return db.query(models.Language).filter(models.Language.id == lang_id).first()
