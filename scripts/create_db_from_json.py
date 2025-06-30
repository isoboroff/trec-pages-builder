import json
import numpy as np
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


base_path = Path("metadata")
sqlite_filepath = "db.sqlite"

# utility functions

def load_json(file_path: Path):
    """Load a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def safe_json_dumps(value):
    """Dump JSON safely, replacing null-like structures with empty string."""
    try:
        result = json.dumps(value)
        return "" if result in ['[]', '{}', 'null', '""'] else result
    except (TypeError, ValueError):
        return value


def extract_trec_name(file_path: Path) -> str:
    """Extract TREC name from file path."""
    return file_path.parent.name


def load_from_files(pattern: str, parse_fn):
    """Load and parse JSONs using a given function from matching files."""
    records = []
    for file_path in base_path.glob(pattern):
        records.extend(parse_fn(file_path))
    return pd.DataFrame(records)

# loaders for each table

def load_all_runs():
    def parse(file_path):
        runs = load_json(file_path)
        return [run for track_runs in runs.values() for run in track_runs]

    return load_from_files('trec*/runs.json', parse)


def load_all_participants():
    def parse(file_path):
        participants = load_json(file_path)
        return list(participants.values())

    return load_from_files('trec*/participants.json', parse)


def load_all_publications():
    def parse(file_path):
        trec = extract_trec_name(file_path)
        records = []
        for track, track_pubs in load_json(file_path).items():
            for metadata in track_pubs.values():
                metadata.update({'trec': trec, 'track': track})
                records.append(metadata)
        return records

    return load_from_files('trec*/publications.json', parse)


def load_all_datasets():
    def parse(file_path):
        trec = extract_trec_name(file_path)
        datasets = load_json(file_path)
        return [{**metadata, 'trec': trec, 'track': track} for track, metadata in datasets.items()]

    return load_from_files('trec*/datasets.json', parse)


def load_all_tracks():
    def parse(file_path):
        trec = extract_trec_name(file_path)
        tracks = load_json(file_path)
        return [{**metadata, 'trec': trec, 'track': track} for track, metadata in tracks.items()]

    return load_from_files('trec*/tracks.json', parse)


def load_all_results():
    def parse(file_path):
        trec = extract_trec_name(file_path)
        results = load_json(file_path)
        records = [
            {
                'trec': trec,
                'track': track,
                'runid': runid,
                'eval': evaluation,
                'topic': topic,
                'measure': measure,
                'score': score
            }
            for track, track_results in results.items()
            for runid, evaluations in track_results.items()
            for evaluation, topics in evaluations.items()
            for topic, measures in topics.items()
            for measure, score in measures.items()
        ]
        return records

    return load_from_files('trec*/results.json', parse)

# main data loading

def load_tables(engine):
    def dump_columns(df, cols):
        for col in cols:
            if col in df.columns:
                df[col] = df[col].apply(safe_json_dumps)
        return df.replace(r"", np.nan, regex=True)

    runs = load_all_runs()
    if 'other' in runs.columns:
        runs['other'] = runs['other'].apply(json.dumps)
    runs = runs.replace(r"", np.nan, regex=True)
    runs.to_sql('runs', engine, if_exists='replace', index=False)

    load_all_participants().replace(r"", np.nan, regex=True).to_sql('participants', engine, if_exists='replace', index=False)

    load_all_publications().replace(r"", np.nan, regex=True).to_sql('publications', engine, if_exists='replace', index=False)

    datasets = dump_columns(load_all_datasets(), ['corpus', 'topics', 'qrels', 'ir_datasets', 'trec_webpage', 'other'])
    datasets.to_sql('datasets', engine, if_exists='replace', index=False)

    tracks = dump_columns(load_all_tracks(), ['tasks'])
    tracks.to_sql('tracks', engine, if_exists='replace', index=False)

    load_all_results().replace(r"", np.nan, regex=True).to_sql('results', engine, if_exists='replace', index=False)


# main

def main():
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base = declarative_base()
    Base.metadata.drop_all(engine)
    load_tables(engine)


if __name__ == '__main__':
    main()