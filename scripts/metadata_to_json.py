import json
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine


def main():
    # Set paths
    output_dir = Path('./metadata')
    json_dir = Path('./json')
    sqlite_filepath = './sample-db.sqlite'

    # Create database engine
    engine = create_engine(f"sqlite:///{sqlite_filepath}")

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
        (output_dir / trec_conf).mkdir(parents=True, exist_ok=True)

    # Function to split and write JSON metadata by TREC conference
    def split_json(json_path):
        with open(json_path) as f:
            json_data = json.load(f)
            file_name = json_path.name
            for trec_conf, track_data in json_data.items():
                output_path = output_dir / trec_conf / file_name
                with open(output_path, 'w') as f_out:
                    json.dump(track_data, f_out, indent=4)

    # Process metadata JSON files
    for metadata_file in ['abstracts', 'datasets', 'publications', 'tracks']:
        split_json(json_dir / f'{metadata_file}.json')

    # Function to write JSON data
    def write_json(data, trec_conf, filename):
        path = output_dir / trec_conf / filename
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


if __name__ == '__main__':
    main()
