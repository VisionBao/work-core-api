
import datetime

from sqlalchemy import Column, Integer, String, DateTime

from db.database import Base


class Folder(Base):
    __tablename__ = "folder"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
