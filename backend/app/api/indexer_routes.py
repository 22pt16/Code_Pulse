from fastapi import APIRouter
from pathlib import Path

from app.services.indexer_service import RepositoryIndexer
router = APIRouter()

@router.get("/index")

def index_repository():

    repo_root = Path(__file__).resolve().parents[3]
    sample_repo = repo_root / "repositories" / "sample_repo"
    indexer = RepositoryIndexer()
    result = indexer.index_repository(sample_repo)

    return {
        "repository": str(sample_repo),
        "indexed_files": len(result),
        "results": result
    }