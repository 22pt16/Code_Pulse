from sqlalchemy import Column, Integer, String
from app.db.database import Base


class File(Base):

    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, unique=True, nullable=False)
    language = Column(String, default="python")