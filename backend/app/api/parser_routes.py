from fastapi import APIRouter
from pathlib import Path

from app.parser.python_parser import PythonCodeParser

router = APIRouter()

@router.get("/parse")
def parse_code():

    parser = PythonCodeParser()
    repo_path = Path(__file__).resolve().parents[3]
    file_path = repo_path / "repositories" / "sample_repo" / "auth.py"
    result = parser.parse_file(file_path)
    return result