import os
import re 
import json
import pandas as pd
from tqdm import tqdm
import yaml
from sqlalchemy import create_engine
from docutils.nodes import make_id
import numpy as np
from pathlib import Path
from sqlalchemy.orm import declarative_base


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


def load_from_files(base_path: Path, pattern: str, parse_fn) -> pd.DataFrame:
    """Load and parse JSONs using a given function from matching files."""
    records = []
    for file_path in base_path.glob(pattern):
        records.extend(parse_fn(file_path))
    return pd.DataFrame(records)


def dump_columns(df, cols):
    for col in cols:
        if col in df.columns:
            df[col] = df[col].apply(safe_json_dumps)
    return df.replace(r"", np.nan, regex=True)


# loaders for each table
def load_all_runs(base_path):
    def parse(file_path):
        runs = load_json(file_path)
        return [run for track_runs in runs.values() for run in track_runs]

    return load_from_files(base_path, 'trec*/runs.json', parse)


def load_all_participants(base_path):
    def parse(file_path):
        participants = load_json(file_path)
        return list(participants.values())

    return load_from_files(base_path, 'trec*/participants.json', parse)


def load_all_publications(base_path):
    def parse(file_path):
        trec = extract_trec_name(file_path)
        records = []
        for track, track_pubs in load_json(file_path).items():
            for metadata in track_pubs.values():
                metadata.update({'trec': trec, 'track': track})
                records.append(metadata)
        return records

    return load_from_files(base_path, 'trec*/publications.json', parse)


def load_all_datasets(base_path):
    def parse(file_path):
        trec = extract_trec_name(file_path)
        datasets = load_json(file_path)
        return [{**metadata, 'trec': trec, 'track': track} for track, metadata in datasets.items()]

    return load_from_files(base_path, 'trec*/datasets.json', parse)


def load_all_tracks(base_path):
    def parse(file_path):
        trec = extract_trec_name(file_path)
        tracks = load_json(file_path)
        return [{**metadata, 'trec': trec, 'track': track} for track, metadata in tracks.items()]

    return load_from_files(base_path, 'trec*/tracks.json', parse)


def load_all_results(base_path):
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

    return load_from_files(base_path, 'trec*/results.json', parse)


class DBBuilder:
    def __init__(self, base_path=Path("./metadata")):
        self.base_path=base_path
        self.runs = load_all_runs(self.base_path)
        self.participants = load_all_participants(self.base_path)
        self.publications = load_all_publications(self.base_path)
        self.datasets = load_all_datasets(self.base_path)
        self.tracks = load_all_tracks(self.base_path)
        self.results = load_all_results(self.base_path)


    def load_tables(self, engine):
        if 'other' in self.runs.columns:
            self.runs['other'] = self.runs['other'].apply(json.dumps)
        self.runs = self.runs.replace(r"", np.nan, regex=True)
        self.runs.to_sql('runs', engine, if_exists='replace', index=False)
        self.participants.replace(r"", np.nan, regex=True).to_sql('participants', engine, if_exists='replace', index=False)
        self.publications.replace(r"", np.nan, regex=True).to_sql('publications', engine, if_exists='replace', index=False)
        self.datasets = dump_columns(self.datasets, ['corpus', 'topics', 'qrels', 'ir_datasets', 'trec_webpage', 'other'])
        self.datasets.to_sql('datasets', engine, if_exists='replace', index=False)
        self.tracks = dump_columns(self.tracks, ['tasks'])
        self.tracks.to_sql('tracks', engine, if_exists='replace', index=False)
        self.results.replace(r"", np.nan, regex=True).to_sql('results', engine, if_exists='replace', index=False)


    def create_db_from_json(self, sqlite_filepath):
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
        Base = declarative_base()
        Base.metadata.drop_all(engine)
        self.load_tables(engine)


class PageBuilder:
    def __init__(self, base_path=Path("./metadata")):
        self.base_path=base_path
        self.runs = load_all_runs(self.base_path)
        self.participants = load_all_participants(self.base_path)
        self.publications = load_all_publications(self.base_path)
        self.datasets = load_all_datasets(self.base_path)
        self.tracks = load_all_tracks(self.base_path)
        self.results = load_all_results(self.base_path)


    def build_all(self, build_path, overwrite=False):

        return None 
    

    def build(self, conference, build_path, overwrite=False):

        return None
    

    def metadata_to_json(self, json_input, db_input):

        # Create database engine
        engine = create_engine(f"sqlite:///{db_input}")

        # Load tables
        tables = {
            'runs': pd.read_sql_table('runs', engine),
            'participants': pd.read_sql_table('participants', engine),
            'publications': pd.read_sql_table('publications', engine),
            'tracks': pd.read_sql_table('tracks', engine),
            'datasets': pd.read_sql_table('datasets', engine),
            'results': pd.read_sql_table('results', engine)
        }

        # Create output directories per TREC conference
        for trec_conf in tables['tracks']['trec'].unique():
            (self.base_path / trec_conf).mkdir(parents=True, exist_ok=True)

        # Function to split and write JSON metadata by TREC conference
        def split_json(json_path):
            with open(json_path) as f:
                json_data = json.load(f)
                file_name = json_path.name
                for trec_conf, track_data in json_data.items():
                    output_path = self.base_path / trec_conf / file_name
                    with open(output_path, 'w') as f_out:
                        json.dump(track_data, f_out, indent=4)

        # Process metadata JSON files
        for metadata_file in ['abstracts', 'datasets', 'publications', 'tracks']:
            split_json(json_input / f'{metadata_file}.json')

        # Function to write JSON data
        def write_json(data, trec_conf, filename):
            path = self.base_path / trec_conf / filename
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)

        # Process runs
        for trec_conf in tables['runs']['trec'].unique():
            df_runs = tables['runs'][tables['runs']['trec'] == trec_conf]
            output = {}
            for track, group in df_runs.groupby('track'):
                output[track] = []
                for row in group.to_dict(orient='records'):
                    if row.get('other'):
                        row['other'] = json.loads(row['other'])
                    row.pop('index', None)
                    output[track].append(row)
            write_json(output, trec_conf, 'runs.json')

        # Process participants
        for trec_conf in tables['participants']['trec'].unique():
            df_participants = tables['participants'][tables['participants']['trec'] == trec_conf]
            output = {
                row['pid']: {k: v for k, v in row.items() if k != 'index'}
                for row in df_participants.to_dict(orient='records')
            }
            write_json(output, trec_conf, 'participants.json')

        # Process results
        for trec_conf in tables['results']['trec'].unique():
            df_results = tables['results'][tables['results']['trec'] == trec_conf]
            output = {}
            for track, track_df in df_results.groupby('track'):
                runs_output = {}
                for runid, run_df in track_df.groupby('runid'):
                    evals_output = {}
                    for eval_name, eval_df in run_df.groupby('eval'):
                        topics_output = {}
                        for topic, topic_df in eval_df.groupby('topic'):
                            measures_scores = {
                                row['measure']: row['score']
                                for _, row in topic_df.iterrows()
                            }
                            topics_output[topic] = measures_scores
                        evals_output[eval_name] = topics_output
                    runs_output[runid] = evals_output
                output[track] = runs_output
            write_json(output, trec_conf, 'results.json')
