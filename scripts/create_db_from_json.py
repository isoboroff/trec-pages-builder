from pathlib import Path
from builders import DBBuilder


base_path = Path("./metadata")


def main():
    db_builder = DBBuilder(base_path=base_path)
    db_builder.create_db_from_json(sqlite_filepath=Path("./db.sqlite"))


if __name__ == '__main__':
    main()
