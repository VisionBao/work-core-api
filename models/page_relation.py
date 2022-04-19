from sqlalchemy import Column, Integer, DateTime
from db.database import Base
import datetime


class PageRelation(Base):
    __tablename__ = "pages_relation"
    ancestor = Column(Integer, nullable=False, primary_key=True)
    descendant = Column(Integer, nullable=False, primary_key=True)
    distance = Column(Integer, nullable=False)
    project_id = Column(Integer, nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
