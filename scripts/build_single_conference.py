from pathlib import Path
from builders import PageBuilder


base_path = Path("metadata")
build_path = Path("./browser/src/docs")
trec = 'trec8'


def main():
    page_builder = PageBuilder(base_path=base_path, build_path=build_path)
    page_builder.build(conference=trec, overwrite=False)


if __name__ == '__main__':
    main()
