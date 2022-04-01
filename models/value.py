
from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Value(Base):
    __tablename__ = "values"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), nullable=False)
    lang_id = Column(Integer, nullable=False)
    value = Column(String(255))
