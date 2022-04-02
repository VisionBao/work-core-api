from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/languages', response_model=list[schemas.Language])
def get_languages(db: Session = Depends(get_db)):
    db_languages = crud.get_languages(db)
    return db_languages


@router.get('/language', response_model=schemas.Language)
def get_languages(lang_id: int = None, lang_code: str = None, db: Session = Depends(get_db)):
    db_language = None
    if lang_id:
        db_language = crud.get_language_by_id(db, lang_id)

    if lang_code:
        db_language = crud.get_language_by_code(db, lang_code)

    if db_language is None:
        raise HTTPException(status_code=404, detail="error")
    else:
        return db_language


