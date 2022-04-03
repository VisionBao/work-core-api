from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/add-key', response_model=schemas.Key)
def create_key(key: schemas.KeyCreate, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key.key)
    db_project = crud.get_project(db, key.project_id)
    if db_project is None:
        raise HTTPException(status_code=400, detail="Project not found")
    if key.page_id:
        db_page = crud.get_page_by_id(db, key.page_id)
        if db_page is None:
            raise HTTPException(status_code=400, detail="Page not found")
    if db_key:
        raise HTTPException(status_code=400, detail="Key already registered")
    return crud.create_key(db, key)


@router.get('/get-key', response_model=schemas.Key)
def get_key(key: str, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key)
    if db_key is None:
        raise HTTPException(status_code=400, detail="Key does not exist")
    return db_key


@router.get('/get-keys', response_model=list[schemas.Key])
def get_keys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_keys = crud.get_keys(db, skip, limit)
    return db_keys


@router.get('/get_keys_by_project_id', response_model=list[schemas.Key])
def get_keys(project_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return crud.get_keys_by_project_id(db, project_id=project_id)


@router.get('/get_keys_by_page_id', response_model=list[schemas.Key])
def get_keys(page_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_page = crud.get_page_by_id(db, page_id)
    if db_page is None:
        raise HTTPException(status_code=404, detail="page not found")
    return crud.get_keys_by_page_id(db, page_id)


@router.post('/delete-key')
def create_key(key: str, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key)
    if db_key is None:
        raise HTTPException(status_code=400, detail="Key does not exist")
    crud.delete_value_by_key(db, key)
    return crud.delete_key(db, key)
