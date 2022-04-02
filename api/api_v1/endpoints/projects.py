from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/add-project', response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_symbol(db, project.symbol)
    if db_project:
        raise HTTPException(status_code=400, detail="Project already registered")
    return crud.create_project(db, project)


@router.get('/project', response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.get('/projects', response_model=list[schemas.Project])
def get_project(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_projects = crud.get_projects(db, skip, limit)
    return db_projects
