import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser(description="Assemble JSON metadata files into a single file.")
ap.add_argument('input_dir', type=Path, help='Directory of conference directories containing JSON metadata files.')
ap.add_argument('filename', type=str, help='JSON file in each subdirectory to include.')
ap.add_argument('output_file', type=Path, help='Output file to write the assembled JSON data.')

args = ap.parse_args()

big = {}

for directory in args.input_dir.iterdir():
    if directory.is_dir():
        json_file = directory / args.filename
        if json_file.exists():
            with open(json_file, 'r') as f:
                big[directory.name] = json.load(f)

final = dict(sorted(big.items(), key=lambda item: int(item[0][4:])))

with open(args.output_file, 'w') as f:
    json.dump(final, f, indent=2)
