import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
import utils
from api.deps import get_db

router = APIRouter()


@router.post('/add-folder', response_model=schemas.RestfulModel[schemas.Folder])
def create_project(folder: schemas.FolderCreate, db: Session = Depends(get_db)):
    return schemas.RestfulModel(data=crud.create_folder(db, folder))

@router.get('/folders', response_model=schemas.RestfulModel[schemas.Project])
def get_project(project_id: int, db: Session = Depends(get_db)):
    project_check(db, project_id=project_id)
    db_project = crud.get_project(db, project_id)
    return schemas.RestfulModel(data=db_project)