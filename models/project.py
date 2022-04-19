from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
import datetime


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    access = Column(String(255))
    lang_default = Column(Integer, nullable=False)
    langs = Column(String(255))
    content = Column(String(255))
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
