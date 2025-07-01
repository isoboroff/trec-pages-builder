from pathlib import Path
from builders import PageBuilder


base_path = Path("metadata")


def main():
    page_builder = PageBuilder(base_path=base_path)
    page_builder.metadata_to_json(json_input=Path("./json"), db_input=Path("./sample-db.sqlite"))


if __name__ == '__main__':
    main()
