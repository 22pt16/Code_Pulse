from app.db.database import engine, Base

from app.models.file_model import File
from app.models.symbol_model import Symbol


def init_database():

    Base.metadata.create_all(bind=engine)