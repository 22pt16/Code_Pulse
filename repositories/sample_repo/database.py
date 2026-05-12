from sqlalchemy import create_engine

DATABASE_URL = "postgresql://localhost/codepulse"

engine = create_engine(DATABASE_URL)

def get_db():
    return engine.connect()