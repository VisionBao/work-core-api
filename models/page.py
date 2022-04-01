
from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True, index=True)
    pid = Column(Integer)
    project_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    file_name = Column(String(255))
