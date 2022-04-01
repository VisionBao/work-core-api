from pydantic import BaseModel
from typing import Optional


class KeyBase(BaseModel):
    key: str
    project_id: Optional[int] = None
    page_id: Optional[int] = None
    lang_id: int
    value: str


class KeyCreate(KeyBase):
    pass


class Key(KeyBase):

    class Config:
        orm_mode = True
