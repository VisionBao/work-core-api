import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base


class Value(Base):
    __tablename__ = "values"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), nullable=False)
    lang_id = Column(Integer, nullable=False)
    value = Column(String(255))
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
