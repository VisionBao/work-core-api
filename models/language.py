from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from db.database import Base
import datetime


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    lang_code = Column(String(255), nullable=False)
    en_des = Column(String(255), nullable=False)
    cn_des = Column(String(255))
    create_date = Column(DateTime, default=datetime.datetime.now)
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
