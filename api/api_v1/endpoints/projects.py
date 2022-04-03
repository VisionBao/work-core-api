import json

from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session
import utils

router = APIRouter()


@router.post('/add-project', response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    project_check(db=db,
                  symbol=project.symbol,
                  lang_default=project.lang_default,
                  langs=project.langs
                  )
    project.langs = json.dumps(fix_lang(project.lang_default, json.loads(project.langs)))
    return crud.create_project(db, project)


@router.get('/project', response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project_check(db, project_id=project_id)
    db_project = crud.get_project(db, project_id)
    return db_project


@router.get('/projects', response_model=list[schemas.Project])
def get_project(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_projects = crud.get_projects(db, skip, limit)
    return db_projects


@router.post('/delete_project')
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project_check(db, project_id=project_id)
    db_status = crud.delete_project(db, project_id)
    return db_status


@router.post('/update_project')
def update_project(project: schemas.Project, db: Session = Depends(get_db)):
    project_check(db,
                  project_id=project.id,
                  symbol=project.symbol,
                  lang_default=project.lang_default,
                  langs=project.langs
                  )
    project.langs = json.dumps(fix_lang(project.lang_default, json.loads(project.langs)))
    return crud.update_project(db, project)


def project_check(db: Session, project_id=None, symbol=None, lang_default=None, langs=None):
    if project_id:
        db_project = crud.get_project(db, project_id)
        if db_project is None:
            raise HTTPException(status_code=404, detail="Project not found")

    if symbol:
        db_project = crud.get_project_by_symbol(db, symbol)
        if db_project:
            raise HTTPException(status_code=400, detail="Project already registered")

    if project_id and symbol:
        db_project = crud.get_project_by_symbol(db, symbol)
        if db_project is None or db_project.symbol != symbol:
            raise HTTPException(status_code=400, detail="Project already registered or Symbol error")

    if lang_default and langs:
        if not utils.check_json_format(langs):
            raise HTTPException(status_code=400, detail="support languages error")

        langs_list = json.loads(langs)
        if not isinstance(langs_list, list):
            raise HTTPException(status_code=400, detail="support languages not found")

        for lang in fix_lang(lang_default, langs_list):
            if not isinstance(lang, int):
                raise HTTPException(status_code=400, detail="support languages error")
            db_language = crud.get_language(db, lang)
            if db_language is None:
                raise HTTPException(status_code=400, detail="support language not found")


def fix_lang(lang_default: int, langs: list):
    lang_list = []
    lang_list.extend(langs)
    lang_list.append(lang_default)
    lang_list = list(set(lang_list))
    lang_list.sort()
    return lang_list
