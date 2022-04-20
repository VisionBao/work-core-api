from pydantic import BaseModel
from typing import Optional


class PageBase(BaseModel):
    folder_id: int
    project_id: int
    name: str
    file_name: Optional[str] = None


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int
    create_date: str
    last_modified: str

    class Config:
        orm_mode = True
