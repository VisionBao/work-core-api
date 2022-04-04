from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/add-page', response_model=schemas.RestfulModel[schemas.Page])
def create_page(page: schemas.PageCreate, db: Session = Depends(get_db)):
    check_page(db, page.name, name_check=True, project_id=page.project_id, pid=page.pid)
    return schemas.RestfulModel(data=crud.create_page(db, page))


@router.get('/get_page', response_model=schemas.RestfulModel[schemas.Page])
def get_page(page_id: int, db: Session = Depends(get_db)):
    check_page(db, page_id=page_id)
    return schemas.RestfulModel(data=crud.get_page_by_id(db, page_id))


@router.get('/get-pages', response_model=schemas.RestfulModel[list[schemas.Page]])
def get_page(project_id: int, db: Session = Depends(get_db)):
    db_pages = crud.get_pages(db, project_id)
    return schemas.RestfulModel(data=db_pages)


@router.post('/delete_page', response_model=schemas.RestfulModel)
def get_page(page_id: int, db: Session = Depends(get_db)):
    check_page(db, page_id=page_id)
    return schemas.RestfulModel(data=crud.delete_page(db, page_id))


@router.post('/update_page', response_model=schemas.RestfulModel)
def update_page(page: schemas.Page, db: Session = Depends(get_db)):
    check_page(db, page.name, name_check=True, page_id=page.id, project_id=page.project_id, pid=page.pid)
    return schemas.RestfulModel(data=crud.update_page(db, page))


def check_page(db: Session, name=None, name_check=False, page_id=None, pid=None, project_id=None, file_name=None):
    if name is None and name_check:
        raise HTTPException(status_code=404, detail="Project not found")
    if page_id:
        db_page = crud.get_page_by_id(db, page_id)
        if db_page is None:
            raise HTTPException(status_code=404, detail="Page not found")

    if pid:
        db_page = crud.get_page_by_id(db, pid)
        if db_page is None:
            raise HTTPException(status_code=404, detail="Pid not found")

    if project_id:
        db_project = crud.get_project(db, project_id)
        if db_project is None:
            raise HTTPException(status_code=404, detail="Project not found")

    if file_name:
        pass

    if page_id and project_id:
        db_page = crud.get_page_by_id(db, page_id)
        if db_page.project_id != project_id:
            raise HTTPException(status_code=404, detail="Project id error")
