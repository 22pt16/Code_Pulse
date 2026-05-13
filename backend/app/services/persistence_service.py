from app.models.file_model import File
from app.models.symbol_model import Symbol


class PersistenceService:

    def save_indexed_data(self, db, indexed_data):

        for file_data in indexed_data:

            file_record = File(
                path=file_data["file"]
            )

            db.add(file_record)
            db.commit()
            db.refresh(file_record)

            # Save functions
            for function in file_data["functions"]:

                symbol = Symbol(
                    file_id=file_record.id,
                    name=function["name"],
                    symbol_type="function",
                    start_line=function["start_line"],
                    end_line=function["end_line"],
                    docstring=function["docstring"]
                )

                db.add(symbol)

            # Save classes
            for class_data in file_data["classes"]:

                symbol = Symbol(
                    file_id=file_record.id,
                    name=class_data["name"],
                    symbol_type="class",
                    start_line=class_data["start_line"],
                    end_line=class_data["end_line"],
                    docstring=class_data["docstring"]
                )

                db.add(symbol)

            db.commit()