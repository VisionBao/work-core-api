
from sqlalchemy import  Column, Integer, String
from db.database import Base


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    lang_code = Column(String(255), nullable=False)
    en_des = Column(String(255), nullable=False)
    cn_des = Column(String(255))
