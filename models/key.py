
from sqlalchemy import Integer, Column, String
from db.database import Base


class Key(Base):
    __tablename__ = "keys"
    key = Column(String(255), primary_key=True)
    project_id = Column(Integer)
    page_id = Column(Integer)
