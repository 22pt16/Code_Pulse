from pathlib import Path
from app.parser.python_parser import PythonCodeParser

class RepositoryIndexer:

    def __init__(self):
        self.parser = PythonCodeParser()

    def index_repository(self, repo_path):
        indexed_data = []
        repo_path = Path(repo_path)
        python_files = repo_path.rglob("*.py")

        for file_path in python_files:
            try:
                parsed_result = self.parser.parse_file(file_path)
                indexed_data.append(parsed_result)

            except Exception as error:

                indexed_data.append({
                    "file": str(file_path),
                    "error": str(error)
                })
        return indexed_data