from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db.database import Base
import datetime


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    file_name = Column(String(255))
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
