from fastapi import FastAPI, Depends, HTTPException

import crud
import schemas
from db.database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
from models import Project

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/add-project', response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.get_project_by_symbol(db, project.symbol)
    if db_project:
        raise HTTPException(status_code=400, detail="Project already registered")
    return crud.create_project(db, project)


@app.get('/project', response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@app.get('/projects', response_model=list[schemas.Project])
def get_project(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_projects = crud.get_projects(db, skip, limit)
    return db_projects
