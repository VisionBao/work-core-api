from sqlalchemy.orm import Session

import models


def get_languages(db: Session):
    return db.query(models.Language).all()
