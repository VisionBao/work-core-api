from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/add-page', response_model=schemas.Page)
def create_page(page: schemas.PageCreate, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, page.project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if page.pid:
        db_page = crud.get_page_by_id(db, page.pid)
        if db_page is None:
            raise HTTPException(status_code=404, detail="Pid not found")

    return crud.create_page(db, page)


@router.get('/get_page', response_model=schemas.Page)
def get_page(page_id: int, db: Session = Depends(get_db)):
    db_page = crud.get_page_by_id(db, page_id)
    if db_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return db_page


@router.get('/get-pages', response_model=list[schemas.Page])
def get_page(project_id: int, db: Session = Depends(get_db)):
    db_pages = crud.get_pages(db, project_id)
    return db_pages


@router.get('/delete_page')
def get_page(page_id: int, db: Session = Depends(get_db)):
    db_page = crud.get_page_by_id(db, page_id)
    if db_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return crud.delete_page(db, page_id)
