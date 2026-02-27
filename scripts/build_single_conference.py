import argparse
from pathlib import Path
from builders import PageBuilder

ap = argparse.ArgumentParser(description="Build a single conference's pages.")
ap.add_argument('trec', type=str, help='TREC conference to build (e.g., "trec8").')

args = ap.parse_args()

base_path = Path("./metadata")
build_path = Path("./browser/docs")

def main():
    page_builder = PageBuilder(base_path=base_path)
    page_builder.build(trec=args.trec, build_path=build_path, overwrite=False)


if __name__ == '__main__':
    main()
