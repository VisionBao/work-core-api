
from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    access = Column(String(255))
    langs = Column(String(255))
    content = Column(String(255))
