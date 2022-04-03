from sqlalchemy.orm import Session

import models


def get_languages(db: Session):
    return db.query(models.Language).all()


def get_language(db: Session, lang_id: int = None, lang_code: str = None):
    db_language = db.query(models.Language)
    if lang_id:
        db_language = db_language.filter(models.Language.id == lang_id)
    if lang_code:
        db_language = db_language.filter(models.Language.lang_code == lang_code)
    return db_language.first()
