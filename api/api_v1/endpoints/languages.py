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
