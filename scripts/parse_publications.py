from pathlib import Path
from builders import MetadataWriter


base_path = Path("./metadata")
json_input = Path("./resources/input/json")
db_input = Path("./resources/input/sample-db.sqlite")
bibtex_input = Path("./resources/input/bibtex")


def main():
    metadata_writer = MetadataWriter(base_path=base_path,
                                    json_input=json_input,
                                    db_input=db_input,
                                    bibtex_input=bibtex_input)

    metadata_writer.parse_publications()


if __name__ == '__main__':
    main()
