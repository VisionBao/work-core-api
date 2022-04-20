from sqlalchemy.orm import Session

import models
import schemas


def create_folder(db: Session, folder: schemas.FoldertCreate):
    db_folder = models.Folder(**folder.dict())
    db.add(db_folder)
    db.commit()
    folder = db.refresh(db_folder)
    return db_folder
