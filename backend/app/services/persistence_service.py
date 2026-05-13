from app.models.file_model import File
from app.models.symbol_model import Symbol
from app.services.embedding_service import EmbeddingService

class PersistenceService:

    def save_indexed_data(self, db, indexed_data):

        for file_data in indexed_data:
            embedding_service = EmbeddingService()
            file_record = File(
                path=file_data["file"]
            )

            db.add(file_record)
            db.commit()
            db.refresh(file_record)

            # Save functions
            for function in file_data["functions"]:

                    embedding_text = f"""
                    Function: {function["name"]}
                    Docstring: {function["docstring"]}
                    """

                    embedding = embedding_service.generate_embedding(
                        embedding_text
                    )
                    symbol = Symbol(
                    file_id=file_record.id,
                    name=function["name"],
                    symbol_type="function",
                    start_line=function["start_line"],
                    end_line=function["end_line"],
                    docstring=function["docstring"],
                    embedding=embedding
                )

            db.add(symbol)

            # Save classes
            for class_data in file_data["classes"]:

                embedding_text = f"""
                Class: {class_data["name"]}
                Methods: {", ".join(class_data["methods"])}
                Docstring: {class_data["docstring"]}
                """

                embedding = embedding_service.generate_embedding(
                    embedding_text
                )
                symbol = Symbol(
                    file_id=file_record.id,
                    name=class_data["name"],
                    symbol_type="class",
                    start_line=class_data["start_line"],
                    end_line=class_data["end_line"],
                    docstring=class_data["docstring"],
                    embedding=embedding
                )

                db.add(symbol)

            db.commit()