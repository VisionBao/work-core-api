from pydantic import BaseModel
from typing import Optional

class FolderBase(BaseModel):
    project_id: int
    name: str


class FolderCreate(FolderBase):
    f_project_id: Optional[int] = 0
    pass


class Folder(FolderBase):
    id: int
    create_date: str
    last_modified: str

    class Config:
        orm_mode = True
