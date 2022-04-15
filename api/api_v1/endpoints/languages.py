from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/languages', response_model=schemas.RestfulModel[schemas.ListModel])
def get_languages(db: Session = Depends(get_db)):
    db_languages = crud.get_languages(db)
    return schemas.RestfulModel(
        data=schemas.ListModel(list=db_languages,
                               total=len(db_languages)
                               )
    )


@router.get('/language', response_model=schemas.RestfulModel[schemas.Language])
def get_languages(lang_id: int = None, lang_code: str = None, db: Session = Depends(get_db)):
    db_language = crud.get_language(db, lang_id, lang_code)

    if db_language is None:
        raise HTTPException(status_code=404, detail="error")
    else:
        return schemas.RestfulModel(data=db_language)
