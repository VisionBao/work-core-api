from pydantic import BaseModel
from typing import Optional


class ValueBase(BaseModel):
    key: str
    lang_id: str
    value: str


class ValueCreate(ValueBase):
    pass


class Value(ValueBase):
    id: int

    class Config:
        orm_mode = True
