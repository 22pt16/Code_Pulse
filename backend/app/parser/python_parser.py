import ast
from pathlib import Path


class PythonCodeParser:

    def parse_file(self, file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        tree = ast.parse(source_code)

        parsed_data = {
            "file": str(file_path),
            "imports": [],
            "functions": [],
            "classes": []
        }

        for node in ast.walk(tree):

            # Imports
            if isinstance(node, ast.Import):
                for alias in node.names:
                    parsed_data["imports"].append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module
                parsed_data["imports"].append(module)

            # Functions
            elif isinstance(node, ast.FunctionDef):

                parsed_data["functions"].append({
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                    "docstring": ast.get_docstring(node)
                })

            # Classes
            elif isinstance(node, ast.ClassDef):

                methods = []

                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        methods.append(item.name)

                parsed_data["classes"].append({
                    "name": node.name,
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                    "methods": methods,
                    "docstring": ast.get_docstring(node)
                })

        return parsed_data