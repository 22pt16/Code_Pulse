from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pathlib import Path

from app.db.session import get_db
from app.services.indexer_service import RepositoryIndexer
from app.services.persistence_service import PersistenceService

router = APIRouter()

@router.post("/index-store")

def index_and_store(db: Session = Depends(get_db)):

    repo_root = Path(__file__).resolve().parents[3]
    sample_repo = repo_root / "repositories" / "sample_repo"
    indexer = RepositoryIndexer()
    indexed_data = indexer.index_repository(sample_repo)
    persistence_service = PersistenceService()
    persistence_service.save_indexed_data(
        db,
        indexed_data
    )

    return {
        "message": "Repository indexed and stored successfully",
        "indexed_files": len(indexed_data)
    }