from sqlalchemy import Integer, Column, String, BigInteger, DateTime
from db.database import Base
import datetime


class Key(Base):
    __tablename__ = "keys"
    key = Column(String(255), primary_key=True)
    project_id = Column(Integer)
    page_id = Column(Integer)
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
