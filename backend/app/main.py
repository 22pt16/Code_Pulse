from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine
from app.api.parser_routes import router as parser_router
from app.api.indexer_routes import router as indexer_router

app = FastAPI(
    title="CodePulse",
    description="Semantic Code Intelligence Engine",
    version="0.1.0"
)
app.include_router(parser_router)
app.include_router(indexer_router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "CodePulse Backend"
    }

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "database": "connected",
            "result": result.scalar()
        }