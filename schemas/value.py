from pydantic import BaseModel
from typing import Optional


class ValueBase(BaseModel):
    key: str
    lang_id: int
    value: str


class ValueCreate(ValueBase):
    pass


class Value(ValueBase):
    id: int
    create_date: str
    last_modified: str

    class Config:
        orm_mode = True
