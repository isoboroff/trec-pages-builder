# trec-pages-builder

## overview

- `resources/input/`: All resources to create the JSON-formatted metadata are located here.
- `browser/`: Markdown (`docs`) and HTML (`site`) files of the browser can be found here.
- `metadata/`: JSON-formatted metadata
- `scripts/`: The build scripts can be found here. 

## steps to build the browser pages

Create a virtual environment and activate it: 
```
python -m venv .venv && . ./.venv/bin/activate
```

Install the packages:
```
pip install -r requirements.txt
```

Convert the metadata to JSON-formatted files that can be found in `metadata/` afterwards:
```
python scripts/metadata_to_json.py
```

Optionally, you can create a SQLite database from the JSON files, e.g., to use it with the REST-API:
```
python scripts/create_db_from_json.py
```

Build all Markdown browser files (`metadata_to_json.py` needs to be executed first, see above):
```
python scripts/build_all_conferences.py
```

Alternatively, you can build Markdown files for a specific conference:
```
python scripts/build_single_conference.py
```

Once the files in browser/docs/ are generated, run the following command to build the HTML files. 
```
cd browser/src/ && mkdocs build 
```

Optionally, you can run the browser locally to double-check the results:
```
mkdocs serve
```

The browser HTML files can then be pushed to [https://github.com/usnistgov/trec-browser](https://github.com/usnistgov/trec-browser).
