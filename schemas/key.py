from pydantic import BaseModel
from typing import Optional


class KeyBase(BaseModel):
    key: str
    project_id: Optional[int] = None
    page_id: Optional[int] = None


class KeyCreate(KeyBase):
    pass


class Key(KeyBase):

    class Config:
        orm_mode = True
