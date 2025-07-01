from pathlib import Path
from builders import PageBuilder


base_path = Path("metadata")
build_path = Path("./browser/src/docs")


def main():
    page_builder = PageBuilder(base_path=base_path, build_path=build_path)
    page_builder.build_all(overwrite=False)


if __name__ == '__main__':
    main()
