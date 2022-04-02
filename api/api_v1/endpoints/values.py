from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException

import crud
import schemas
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/get_values', response_model=list[schemas.Value])
def get_values_by_key(key: str, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key)
    if db_key is None:
        raise HTTPException(status_code=404, detail="key not found")
    return crud.get_values_by_key(db, key)


@router.get('/delete_value', response_model=schemas.Value)
def get_values_by_key(key: str, db: Session = Depends(get_db)):
    db_key = crud.get_key(db, key)
    if db_key is None:
        raise HTTPException(status_code=404, detail="key not found")
    return crud.get_values_by_key(db, key)


@router.post('/add-values', response_model=list[schemas.Value])
def create_values(values: list[schemas.ValueCreate], db: Session = Depends(get_db)):
    db_value_creat = []
    db_value_update = []
    db_values = []
    for value in values:
        db_key = crud.get_key(db, value.key)
        if db_key is None:
            raise HTTPException(status_code=404, detail="key not found")
    for value in values:
        db_value = crud.get_value(db, value.key, value.lang_id)
        if db_value is None:
            db_value = db_value_creat.append(db_value)
        else:
            db_value = db_value_update.append(db_value)
        db_values.append(db_value)
    return db_values
