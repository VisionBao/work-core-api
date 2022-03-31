from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Project(BaseModel):
    id: Optional[int] = None
    symbol: str
    name: str
    langs: str
    content: Optional[str] = None


class User(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    access = Column(String(255))
    langs = Column(String(255))
    content = Column(String(255))
