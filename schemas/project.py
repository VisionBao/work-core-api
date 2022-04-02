from pydantic import BaseModel
from typing import Optional


class ProjectBase(BaseModel):
    symbol: str
    name: str
    langs: Optional[str] = None
    content: Optional[str] = None
    access: Optional[str] = None
    lang_default: int


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
