from pydantic import BaseModel
from typing import Optional


class ProjectBase(BaseModel):
    symbol: str
    name: str
    langs: str
    content: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
