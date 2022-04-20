from pydantic import BaseModel
from typing import Optional


class KeyBase(BaseModel):
    key: str
    project_id: Optional[int] = None
    page_id: Optional[int] = None


class KeyCreate(KeyBase):
    pass


class Key(KeyBase):
    create_date: str
    last_modified: str

    class Config:
        orm_mode = True
