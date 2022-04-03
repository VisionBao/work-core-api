from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/add-key', response_model=schemas.Key)
def create_key(key: schemas.KeyCreate, db: Session = Depends(get_db)):
    check_key(db, key=key.key, project_id=key.project_id, page_id=key.page_id)
    return crud.create_key(db, key)


@router.get('/get-key', response_model=schemas.Key)
def get_key(key: str, db: Session = Depends(get_db)):
    check_key(db, key=key)
    return crud.get_key(db, key)


@router.get('/get-keys', response_model=list[schemas.Key])
def get_keys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_keys = crud.get_keys(db, skip, limit)
    return db_keys


@router.get('/get_keys_by_project_id', response_model=list[schemas.Key])
def get_keys(project_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    check_key(db, project_id=project_id)
    return crud.get_keys_by_project_id(db, project_id=project_id)


@router.get('/get_keys_by_page_id', response_model=list[schemas.Key])
def get_keys(page_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    check_key(db, page_id=page_id)
    return crud.get_keys_by_page_id(db, page_id)


@router.post('/delete-key')
def create_key(key: str, db: Session = Depends(get_db)):
    check_key(db, key=key)
    crud.delete_value_by_key(db, key)
    return crud.delete_key(db, key)


@router.post('update_key')
def update_key(key: schemas.Key, db: Session = Depends(get_db)):
    check_key(db, key.key, project_id=key.project_id, page_id=key.page_id, update=True)
    return crud.update_key(db, key)


def check_key(db, key=None, project_id=None, page_id=None, update=False):
    if key:
        db_key = crud.get_key(db, key)
        if db_key and bool(1-update):
            raise HTTPException(status_code=400, detail="Key already registered")
        if db_key is None and update:
            raise HTTPException(status_code=400, detail="Key not found")

    if project_id:
        db_project = crud.get_project(db, project_id)
        if db_project is None:
            raise HTTPException(status_code=400, detail="Project not found")

    if page_id:
        db_page = crud.get_page_by_id(db, page_id)
        if db_page is None:
            raise HTTPException(status_code=400, detail="Page not found")
        if project_id and project_id != db_page.project_id:
            raise HTTPException(status_code=400, detail="Page and Project not Match")
