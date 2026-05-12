from fastapi import APIRouter

from app.parser.python_parser import PythonCodeParser

router = APIRouter()

@router.get("/parse")

def parse_code():

    parser = PythonCodeParser()

    result = parser.parse_file(
        "../sample_repo/auth.py"
    )

    return result