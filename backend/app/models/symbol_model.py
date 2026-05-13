from sqlalchemy import Column, Integer, String, ForeignKey, Text

from app.db.database import Base

class Symbol(Base):

    __tablename__ = "symbols"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    name = Column(String, nullable=False)
    symbol_type = Column(String)
    start_line = Column(Integer)
    end_line = Column(Integer)
    docstring = Column(Text, nullable=True)