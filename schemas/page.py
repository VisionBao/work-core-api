from pydantic import BaseModel
from typing import Optional


class PageBase(BaseModel):
    pid: Optional[int] = None
    project_id: int
    name: str
    file_name: Optional[str] = None


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int

    class Config:
        orm_mode = True
