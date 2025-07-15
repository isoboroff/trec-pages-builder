from pathlib import Path
from builders import metadata_to_json


base_path = Path("./metadata")
json_input = Path("./json")
db_input = Path("./sample-db.sqlite")
bibtex_input = Path("./bibtex")


def main():
    metadata_to_json(base_path=base_path, 
                     json_input=json_input, 
                     db_input=db_input,
                     bibtex_input=bibtex_input)


if __name__ == '__main__':
    main()
