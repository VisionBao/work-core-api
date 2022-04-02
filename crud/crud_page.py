from sqlalchemy.orm import Session

import models
import schemas


def get_page_by_id(db: Session, page_id: int):
    return db.query(models.Page).filter(models.Page.id == page_id).first()


def get_pages(db: Session, project_id: int):
    return db.query(models.Page).filter(models.Page.project_id == project_id).all()


def delete_page(db: Session, page_id: int):
    db_page = db.query(models.Page).filter(models.Page.id == page_id).delete()
    db.commit()
    return db_page


def create_page(db: Session, page: schemas.PageCreate):
    db_page = models.Page(**page.dict())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page
