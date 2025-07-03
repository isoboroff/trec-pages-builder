import os
import re 
import json
from typing import List, Tuple
import pandas as pd
from tqdm import tqdm
import yaml
from sqlalchemy import create_engine
from docutils.nodes import make_id
import numpy as np
from pathlib import Path
from sqlalchemy.orm import declarative_base


# ---> begin: utility functions <---
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


# ---> PageBuilder utitility functions <---
def is_json(data: str) -> bool:
    """Return True if the string is valid JSON, otherwise False."""
    if not data:
        return False
    try:
        json.loads(data)
        return True
    except (ValueError, TypeError):
        return False


def convert(json_data: str, bold: bool = False, single_key: str = None) -> str:
    """Convert JSON-formatted or plain string into markdown-formatted reference(s)."""
    if is_json(json_data):
        entries = json.loads(json_data)
        return ' | '.join(
            f"[{'**`' + k + '`**' if bold else '`' + k + '`'}]({v})"
            for k, v in entries.items()
        )

    key = single_key or json_data
    label = f"**`{key}`**" if bold else f"`{key}`"
    return f"[{label}]({json_data})"


def trec_year(trec_name: str) -> int:
    """Return the year of a TREC iteration based on its name."""
    if trec_name == 'trec-covid':
        return 2020
    match = re.search(r'\d+', trec_name)
    return 1991 + int(match.group()) if match else None


def track_map(tracks) -> dict:
    """Return a nested dictionary mapping TREC -> track -> full name."""
    result = {}
    for trec, group in tracks.groupby('trec'):
        result[trec] = {
            row.track: row.fullname
            for row in group.drop_duplicates(subset=['track']).itertuples()
        }

# ---> end: utility functions <---


# ---> begin: table loaders <---
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

# ---> end: table loaders <---


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
    def __init__(self, base_path: Path = Path("./metadata"), build_path: Path = Path("./browser/src/docs")):
        self.base_path=base_path
        self.build_path=build_path

        # Load metadata
        self.runs = load_all_runs(self.base_path)
        self.participants = load_all_participants(self.base_path)
        self.publications = load_all_publications(self.base_path)
        self.datasets = load_all_datasets(self.base_path)
        self.tracks = load_all_tracks(self.base_path)
        self.results = load_all_results(self.base_path)

        # Initialize missing metadata
        self.no_input = self._init_missing_input()
        self.no_appendix = self._init_missing_appendix()
        self.no_proceedings = self._init_missing_proceedings()
        self.no_runs = self._init_missing_runs()
        self.no_participants = self._init_missing_participants()
        self.no_data = self._init_missing_data()
        self.no_summary = self._init_missing_summary()


    def _get_trec_track_pairs(self) -> List[Tuple[str, str]]:
        return [(row.trec, row.track) for row in self.tracks.itertuples(index=False)]


    def _init_missing_input(self) -> List[Tuple[str, str]]:
        no_input = []
        for trec, track in self._get_trec_track_pairs():
            r = self.runs[(self.runs['trec'] == trec) & (self.runs['track'] == track)]
            if r['input_url'].isna().all():
                no_input.append((trec, track))
        return no_input


    def _init_missing_appendix(self) -> List[Tuple[str, str]]:
        no_appendix = []
        for trec, track in self._get_trec_track_pairs():
            r = self.runs[(self.runs['trec'] == trec) & (self.runs['track'] == track)]
            if r['appendix_url'].isna().all():
                no_appendix.append((trec, track))
        return no_appendix


    def _init_missing_participants(self) -> List[Tuple[str, str]]:
        no_participants = []
        for trec, track in self._get_trec_track_pairs():
            r = self.runs[(self.runs['trec'] == trec) & (self.runs['track'] == track)]
            if r.empty:
                no_participants.append((trec, track))
        return no_participants


    def _init_missing_runs(self) -> List[Tuple[str, str]]:
        no_runs = []
        for trec, track in self._get_trec_track_pairs():
            r = self.runs[(self.runs['trec'] == trec) & (self.runs['track'] == track)]
            if r.empty:
                no_runs.append((trec, track))
        return no_runs


    def _init_missing_proceedings(self) -> List[Tuple[str, str]]:
        no_proceedings = []
        for trec, track in self._get_trec_track_pairs():
            p = self.publications[(self.publications['trec'] == trec) & (self.publications['track'] == track)]
            if p.empty:
                no_proceedings.append((trec, track))
        return no_proceedings


    def _init_missing_data(self) -> List[Tuple[str, str]]:
        no_data = []
        nd = self.datasets[
            self.datasets[['corpus', 'topics', 'qrels', 'ir_datasets', 'trec_webpage', 'other']].isna().all(axis=1)
        ]
        no_data = [(row.trec, row.track) for row in nd.itertuples(index=False)]
        return no_data


    def _init_missing_summary(self) -> List[Tuple[str, str]]:

        no_summary = []

        # Tracks with online summaries but no implemented parser
        no_parsing = [ 
            ('trec32', 'crisis'), ('trec32', 'trials'), ('trec32', 'deep'), 
            ('trec32', 'ikat'), ('trec32', 'neuclir'), ('trec32', 'atomic'), 
            ('trec32', 'product'), ('trec32', 'tot'), ('trec31', 'crisis'), 
            ('trec31', 'fair'), ('trec30', 'fair'), ('trec29', 'fair'), 
            ('trec28', 'fair'), ('trec27', 'incident'), ('trec26', 'rts'), 
            ('trec25', 'realtime'), ('trec24', 'domain'), ('trec24', 'tempsumm'), 
            ('trec21', 'crowd'), ('trec19', 'session'), ('trec17', 'relfdbk'), 
            ('trec17', 'million-query'), ('trec16', 'qa'), ('trec15', 'qa'), 
            ('trec14', 'qa'), ('trec13', 'qa'), ('trec12', 'qa'), 
            ('trec11', 'qa'), ('trec10', 'qa'), ('trec9', 'qa'), 
            ('trec8', 'qa'), ('trec8', 'xlingual'), ('trec7', 'filtering'), 
            ('trec4', 'filtering')
        ]

        # Known exceptions that should not be flagged as missing summaries
        summary_exceptions = {
            ('trec-covid', f'round{i}') for i in range(1, 6)
        }.union({
            ('trec19', 'chemical'),
            ('trec11', 'xlingual'),
            ('trec5', 'dbmerge')
        })

        for trec, track in self._get_trec_track_pairs():
            r = self.runs[(self.runs['trec'] == trec) & (self.runs['track'] == track)]
            if r['summary_url'].isna().all() and (trec, track) not in summary_exceptions:
                no_summary.append((trec, track))

        no_summary += no_parsing

        return no_summary


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


    def format_bibtex(self, bibtex: str) -> str:
        return bibtex.strip().replace('\n', '\n\t')


    def format_abstract(self, abstract: str) -> str:
        return f'??? abstract "Abstract"\n\t\n\t{abstract}\n\t\n\n' if abstract else ''


    def format_bibtex_block(self, bibtex: str, biburl: str) -> str:
        return f'??? quote "Bibtex [:material-link-variant:]({biburl}) "\n\t```\n\t{bibtex}\n\t```\n\n'


    def proceedings_page_content(self, trec, track, publications, runs, tracks):
        """Generate the proceedings page of a track."""
        
        pubs = publications[(publications['track'] == track) & (publications['trec'] == trec)]
        track_row = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].iloc[0]
        track_fullname = track_row.fullname

        content = f"# Proceedings - {track_fullname} {trec_year(trec)}\n\n"

        # Add overview paper if available
        overview = pubs[pubs['pid'] == 'overview']
        if not overview.empty:
            o = overview.iloc[0]
            content += f"#### {o.title}\n\n"
            content += f"_{o.author}_\n\n"
            content += f"- :material-file-pdf-box: **Paper:** [{o.url}]({o.url})\n"
            content += self.format_abstract(o.abstract)
            content += self.format_bibtex_block(self.format_bibtex(o.bibtex), o.get('biburl', ''))

        # Add individual papers
        for pub in pubs.itertuples():
            if pub.pid == 'overview':
                continue

            content += f"#### {pub.title}\n\n"
            content += f"_{pub.author}_\n\n"

            # Link to participants page
            if (trec, track) not in self.no_participants:
                content += f"- :fontawesome-solid-user-group: **Participant:** [{pub.pid}](./participants.md#{pub.pid.lower()})\n"

            # Link to paper
            content += f"- :material-file-pdf-box: **Paper:** [{pub.url}]({pub.url})\n"

            # Link to runs
            track_runs = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['pid'] == pub.pid)]
            if not track_runs.empty:
                run_links = ' | '.join(
                    f"[{r.runid}](./runs.md#{r.runid.lower()})" for r in track_runs.itertuples()
                )
                content += f"- :material-file-search: **Runs:** {run_links}\n\n"
            else:
                content += '\n'

            content += self.format_abstract(pub.abstract)
            content += self.format_bibtex_block(self.format_bibtex(pub.bibtex), pub.biburl)

        return content


    def get_run_metadata_links(self, run_row, trec, track, publications):
        links = []
        run_url_id = run_row.runid.lower().replace('.', '')
        links.append(f'[**`Metadata`**](./runs.md#{run_url_id})')

        participant_id = run_row.pid.lower().replace('.', '')
        links.append(f'[**`Participants`**](./participants.md#{participant_id})')

        pub_match = publications[
            (publications['trec'] == trec) & 
            (publications['track'] == track) & 
            (publications['pid'] == run_row.pid)
        ]
        if not pub_match.empty:
            title_id = make_id(pub_match.iloc[0].title)
            links.append(f'[**`Proceedings`**](./proceedings.md#{title_id})')

        if run_row.input_url:
            links.append(convert(run_row.input_url, bold=True, single_key='Input'))
        if run_row.summary_url:
            links.append(convert(run_row.summary_url, bold=True, single_key='Summary'))
        if run_row.appendix_url:
            links.append(convert(run_row.appendix_url, bold=True, single_key='Appendix'))

        return ' | '.join(links)


    def results_page_content(self, trec, track, tracks, runs, results, publications):
        """Generate the results page of a track."""

        track_row = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].iloc[0]
        track_fullname = track_row.fullname

        content = "---\nsearch:\n  exclude: true\n---\n\n"
        content += f"# Results - {track_fullname} {trec_year(trec)}\n\n"

        # Get run IDs and summary results
        runids = runs[(runs['trec'] == trec) & (runs['track'] == track)].runid.unique()

        if track == 'session':
            runids = set(''.join(runid.split('.')[:-1]) for runid in runids)

        summaries = results[
            (results['trec'] == trec) & 
            (results['track'] == track) & 
            (results['measure'] == 'summary')
        ]

        for runid in runids:
            _summaries = summaries[summaries['runid'] == runid]
            if _summaries.empty:
                continue

            content += f"#### {runid}\n"

            run_query = (runs['trec'] == trec) & (runs['track'] == track)
            run = runs[run_query & (runs['runid'] == (runid + '.RL1' if track == 'session' else runid))]
            if not run.empty:
                run_row = run.iloc[0]
                content += self.get_run_metadata_links(run_row, trec, track, publications) + "\n"

            for summary in _summaries.itertuples():
                content += f'??? example "summary ({summary.eval})"\n\t```\n{summary.score}\n\t```\n'

            content += "---\n"

        return content


    def runs_page_content(self, trec, track, publications, runs, tracks):
        """Generate the runs page of a track."""

        _runs = runs[(runs['trec'] == trec) & (runs['track'] == track)]
        _runs = _runs.sort_values(by='runid', key=lambda col: col.str.lower())

        # Track title and year
        track_fullname = tracks[
            (tracks['trec'] == trec) & (tracks['track'] == track)
        ].fullname.iloc[0]
        
        content = f"# Runs - {track_fullname} {trec_year(trec)}\n\n"

        for run in _runs.itertuples():
            # Base reference to participant
            participant_url_id = run.pid.lower().replace('.', '')
            # if (trec, track) in no_summary or runid not in results[(results['trec'] == trec) & (results['track'] == track)]['runid']:
            if (trec, track) in self.no_summary:
                ref = f"[**`Participants`**](./participants.md#{participant_url_id})"
            else:
                result_url_id = ''.join(run.runid.lower().split('.')[:-1]) if track == 'session' else run.runid.lower().replace('.', '')
                ref = f"[**`Results`**](./results.md#{result_url_id}) | [**`Participants`**](./participants.md#{participant_url_id})"

            # Reference to proceeding paper
            pub = publications[
                (publications['trec'] == trec) & 
                (publications['track'] == track) & 
                (publications['pid'] == run.pid)
            ]
            if not pub.empty:
                title_id = make_id(pub.iloc[0].title)
                ref += f" | [**`Proceedings`**](./proceedings.md#{title_id})"

            # Input/Summary/Appendix links
            for label, url in [('Input', run.input_url), ('Summary', run.summary_url), ('Appendix', run.appendix_url)]:
                if url:
                    ref += f" | {convert(url, bold=True, single_key=label)}"

            # Metadata block
            content += f"""#### {run.runid}  
    {ref}  

    - :material-rename: **Run ID:** {run.runid}  
    - :fontawesome-solid-user-group: **Participant:** {run.pid}  
    - :material-format-text: **Track:** {track_fullname}  
    - :material-calendar: **Year:** {run.year}  
    """
            if run.date:
                content += f"- :material-upload: **Submission:** {run.date}  \n"
            if run.type:
                content += f"- :fontawesome-solid-user-gear: **Type:** {run.type}  \n"
            if run.task:
                content += f"- :material-text-search: **Task:** {run.task}  \n"
            if run.md5 and len(run.md5) == 32:
                content += f"- :material-fingerprint: **MD5:** `{run.md5.strip()}`  \n"
            if run.description:
                content += f"- :material-text: **Run description:** {run.description.strip()}  \n"
            if run.other:
                try:
                    repository = json.loads(run.other).get("repository")
                    if repository:
                        content += f"- :material-code-tags: **Code:** [{repository}]({repository})  \n"
                except Exception:
                    pass

            content += "\n---\n"

        return content


    def participants_page_content(self, trec, track, participants, runs, tracks):
        """Generate the participants page of a track."""

        # Filter relevant runs
        _runs = runs[(runs['trec'] == trec)]
        pids = _runs.sort_values(by='pid', key=lambda col: col.str.lower()).pid.unique()

        # Track title and year
        track_fullname = tracks[
            (tracks['trec'] == trec) & (tracks['track'] == track)
        ].fullname.iloc[0]
        
        content = f"# Participants - {track_fullname} {trec_year(trec)}\n\n"

        for pid in pids:
            p_runs = runs[
                (runs['pid'] == pid) & 
                (runs['trec'] == trec) & 
                (runs['track'] == track)
            ]

            if p_runs.empty:
                continue

            # Get participant metadata
            part_info = participants[
                (participants['trec'] == trec) & 
                (participants['pid'] == pid)
            ]
            name = part_info.name.iloc[0] if not part_info.empty else ""
            organization = part_info.organization.iloc[0] if not part_info.empty else ""

            # Format run references
            run_refs = [
                f"[{row.runid}](./runs.md#{row.runid.lower().replace('.', '')})"
                for row in p_runs.itertuples()
            ]
            run_list = " | ".join(run_refs)

            # Add participant section
            content += f"#### {pid}\n"
            if name:
                content += f"- :fontawesome-solid-user-group: **Name:** {name}\n"
            if organization:
                content += f"- :octicons-organization-16: **Organization:** {organization}\n"
            if run_list:
                content += f"- :material-file-search: **Runs:** {run_list}\n"
            content += "\n---\n"

        return content


    def track_overview_page_content(self, trec, track, tracks):
        """Generate the content of a track overview page."""

        # Extract the track row once
        track_row = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].iloc[0]

        # Quick access links
        quick_access_parts = []
        if (trec, track) not in self.no_proceedings:
            quick_access_parts.append('[`Proceedings`](./proceedings.md)')
        if (trec, track) not in self.no_data:
            quick_access_parts.append('[`Data`](./data.md)')
        if (trec, track) not in self.no_summary:
            quick_access_parts.append('[`Results`](./results.md)')
        if (trec, track) not in self.no_runs:
            quick_access_parts.append('[`Runs`](./runs.md)')
        if (trec, track) not in self.no_participants:
            quick_access_parts.append('[`Participants`](./participants.md)')
        quick_access = ' | '.join(quick_access_parts)

        # Page header and description
        heading = f"# Overview - {track_row.fullname} {trec_year(trec)}"
        description = track_row.description or ""
        content = f"{heading}\n\n{quick_access}\n\n{{==\n\n{description}\n\n==}}\n\n"

        # Track coordinators
        if track_row.coordinators:
            coordinators_md = "\n".join(f"- {coord.strip()}" for coord in track_row.coordinators.split(':') if coord.strip())
            if coordinators_md:
                content += f":fontawesome-solid-user-group: **Track coordinator(s):**\n\n{coordinators_md}\n\n"

        # Track tasks
        if track_row.tasks:
            try:
                # task_dict = json.loads(track_row.tasks)
                task_dict = track_row.tasks
                if task_dict:
                    content += ":material-text-search: **Tasks:**\n\n"
                    for task, description in task_dict.items():
                        content += f"- `{task}`: {description}\n"
                    content += "\n"
            except json.JSONDecodeError:
                pass  # Silently skip malformed JSON

        # Web page
        if track_row.webpage:
            content += f":fontawesome-solid-globe: **Track Web Page:** [`{track_row.webpage}`]({track_row.webpage})\n\n"

        content += "---\n\n"
        return content


    def overview_page_covid(self, trec, tracks):
        """Generate the overview page of TREC-COVID."""

        # Title
        content = f"# TREC-COVID {trec_year(trec)}\n\n"

        # Quick access links for each round (track)
        quick_access = ''
        for track in tracks[tracks['trec'] == trec].track.unique():
            quick_access_parts = [f"[`Overview`](./{track}/overview.md)"]
            if (trec, track) not in self.no_proceedings:
                quick_access_parts.append(f"[`Proceedings`](./{track}/proceedings.md)")
            if (trec, track) not in self.no_data:
                quick_access_parts.append(f"[`Data`](./{track}/data.md)")
            if (trec, track) not in self.no_summary:
                quick_access_parts.append(f"[`Results`](./{track}/results.md)")
            if (trec, track) not in self.no_runs:
                quick_access_parts.append(f"[`Runs`](./{track}/runs.md)")
            if (trec, track) not in self.no_participants:
                quick_access_parts.append(f"[`Participants`](./{track}/participants.md)")
            
            round_name = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
            quick_access_round = f"**{round_name}:** " + " | ".join(quick_access_parts) + "\n\n"
            quick_access += quick_access_round

        # Use round1 as the main reference for general description, coordinators, and webpage
        base_track = 'round1'
        base_row = tracks[(tracks['trec'] == trec) & (tracks['track'] == base_track)].iloc[0]

        # Description
        description = base_row.description or ""
        content += f"{quick_access}\n\n{{==\n\n{description}\n\n==}}\n\n"

        # Coordinators
        if base_row.coordinators:
            coordinators_md = "\n".join(f"- {c.strip()}" for c in base_row.coordinators.split(":") if c.strip())
            content += f":fontawesome-solid-user-group: **Track coordinator(s):**\n\n{coordinators_md}\n\n"

        # Webpage
        if base_row.webpage:
            content += f":fontawesome-solid-globe: **Track Web Page:** [`{base_row.webpage}`]({base_row.webpage})\n\n"

        content += "---\n\n"
        return content


    def overview_page_content(self, trec, tracks):
        """Generate the overview page of a TREC with all track overviews."""

        if trec == 'trec-covid':
            return self.overview_page_covid(trec, tracks)

        # Title
        content = f"# Text REtrieval Conference (TREC) {trec_year(trec)}\n\n"

        for track in tracks[tracks['trec'] == trec].track.unique():
            row = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].iloc[0]

            # Quick access navigation
            quick_access_parts = [f"[`Overview`](./{track}/overview.md)"]
            if (trec, track) not in self.no_proceedings:
                quick_access_parts.append(f"[`Proceedings`](./{track}/proceedings.md)")
            if (trec, track) not in self.no_data:
                quick_access_parts.append(f"[`Data`](./{track}/data.md)")
            if (trec, track) not in self.no_summary:
                quick_access_parts.append(f"[`Results`](./{track}/results.md)")
            if (trec, track) not in self.no_runs:
                quick_access_parts.append(f"[`Runs`](./{track}/runs.md)")
            if (trec, track) not in self.no_participants:
                quick_access_parts.append(f"[`Participants`](./{track}/participants.md)")
            quick_access = " | ".join(quick_access_parts)

            # Track details
            fullname = row.fullname
            description = row.description or ""

            content += f"## {fullname}\n\n{quick_access}\n\n{{==\n\n{description}\n\n==}}\n\n"

            # Coordinators
            if row.coordinators:
                coordinators_md = "\n".join(f"- {c.strip()}" for c in row.coordinators.split(":") if c.strip())
                content += f":fontawesome-solid-user-group: **Track coordinator(s):**\n\n{coordinators_md}\n\n"

            # Web page
            if row.webpage:
                content += f":fontawesome-solid-globe: **Track Web Page:** [`{row.webpage}`]({row.webpage})\n\n"

            content += "---\n\n"

        return content


    def data_page_content(self, trec, track, tracks, datasets):
        """Generate the content of a data page."""

        # Get metadata for the track and dataset
        track_row = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].iloc[0]
        dataset_row = datasets[(datasets['trec'] == trec) & (datasets['track'] == track)].iloc[0]

        track_fullname = track_row.fullname
        year = trec_year(trec)

        content = f"# Data - {track_fullname} {year}\n\n"

        # Add TREC webpage if available
        trec_webpage = dataset_row.trec_webpage
        if trec_webpage:
            content += f":fontawesome-solid-globe: **`trec.nist.gov`**: [`{trec_webpage}`]({trec_webpage})\n\n"

        content += "---\n\n"

        # Add links to primary resources
        task_content = []

        if dataset_row.corpus:
            task_content.append(f"- :material-database: **Corpus**: {convert(dataset_row.corpus)}\n")
        if dataset_row.topics:
            task_content.append(f"- :octicons-question-16: **Topics**: {convert(dataset_row.topics)}\n")
        if dataset_row.qrels:
            task_content.append(f"- :material-label: **Qrels**: {convert(dataset_row.qrels)}\n")
        if dataset_row.ir_datasets:
            task_content.append(f"- :material-database-outline: **ir_datasets**: {convert(dataset_row.ir_datasets)}\n")

        if task_content:
            content += ''.join(task_content) + "\n---\n\n"

        # Add "Other" resources if available
        if dataset_row.other:
            content += f"**Other:** {convert(dataset_row.other)}\n"

        return content


    def format_paper_section(self, pub, trec, runs, track=None):
        """Helper to format a paper section including metadata, links, and bibtex."""
        title = pub.title
        author = pub.author
        url = pub.url
        abstract = pub.abstract
        bibtex = pub.bibtex.strip().replace('\n', '\n\t')
        biburl = pub.biburl or ''

        section = f'#### {title}\n\n_{author}_\n\n'
        section += f'- :material-file-pdf-box: **Paper:** [{url}]({url})\n'

        if track and (trec, track) not in self.no_participants:
            section += f'- :fontawesome-solid-user-group: **Participant:** [{pub.pid}](./{track}/participants.md#{pub.pid.lower()})\n'

        if track:
            _runs = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['pid'] == pub.pid)]
            if len(_runs):
                run_links = [f"[{r.runid}](./{track}/runs.md#{r.runid.lower()})" for _, r in _runs.iterrows()]
                section += f'- :material-file-search: **Runs:** {" | ".join(run_links)}\n'

        if abstract:
            section += f'??? abstract "Abstract"\n\t\n\t{abstract}\n\t\n\n'

        section += f'??? quote "Bibtex [:material-link-variant:]({biburl})"\n\t```\n\t{bibtex}\n\t```\n\n'
        return section


    def proceedings_content(self, trec, publications, runs, tracks):
        """Generate the proceedings page of a TREC including all tracks."""

        # Header for the proceedings page
        content = f"# Proceedings {trec_year(trec)}\n\n"

        # Add general overview paper if it exists
        overview_pub = publications[(publications['track'] == 'overview') & (publications['trec'] == trec) & (publications['pid'] == 'overview')]
        if not overview_pub.empty:
            content += "## {}\n\n".format(overview_pub.iloc[0].title)
            content += self.format_paper_section(overview_pub.iloc[0], trec, runs)

        # Add track-specific papers
        for track in tracks[tracks['trec'] == trec].track.unique():
            track_pubs = publications[(publications['track'] == track) & (publications['trec'] == trec)]
            if track_pubs.empty:
                continue

            track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
            content += f"## {track_fullname}\n\n"

            # Track overview paper
            overview = track_pubs[track_pubs['pid'] == 'overview']
            if not overview.empty:
                content += self.format_paper_section(overview.iloc[0], trec, runs, track=track)

            # Participant papers
            for _, pub in track_pubs.iterrows():
                if pub.pid == 'overview':
                    continue
                content += self.format_paper_section(pub, trec, runs, track=track)

        return content


    def write_page(self, type, **args):
        """Generate browser pages of different types."""

        page_config = {
            'overview': ('overview.md', lambda a: self.overview_page_content(a['trec'], a['tracks'])),
            'proceedings': ('proceedings.md', lambda a: self.proceedings_content(
                trec=a['trec'], publications=a['publications'], runs=a['runs'], tracks=a['tracks'])),
            'publications': ('proceedings.md', lambda a: self.proceedings_page_content(
                trec=a['trec'], track=a['track'], publications=a['publications'], runs=a['runs'], tracks=a['tracks'])),
            'results': ('results.md', lambda a: self.results_page_content(
                a['trec'], a['track'], a['tracks'], a['runs'], a['results'], a['publications'])),
            'runs': ('runs.md', lambda a: self.runs_page_content(
                a['trec'], a['track'], a['publications'], a['runs'], a['tracks'])),
            'participants': ('participants.md', lambda a: self.participants_page_content(
                a['trec'], a['track'], a['participants'], a['runs'], a['tracks'])),
            'track_overview': ('overview.md', lambda a: self.track_overview_page_content(
                a['trec'], a['track'], a['tracks'])),
            'data': ('data.md', lambda a: self.data_page_content(
                a['trec'], a['track'], a['tracks'], a['datasets']))
        }

        if type not in page_config:
            raise ValueError(f"Unknown page type: {type}")

        file_name, content_func = page_config[type]
        page_content = content_func(args)

        # Determine the write path based on whether it's global (overview/proceedings) or track-specific
        if type in ['overview', 'proceedings']:
            output_path = os.path.join(args['build_path'], args['trec'])
        else:
            output_path = os.path.join(args['build_path'], args['trec'], args['track'])

        os.makedirs(output_path, exist_ok=True)
        with open(os.path.join(output_path, file_name), 'w') as f_out:
            f_out.write(page_content)


    def filter_by_trec(self, df, trec):
        return df[df['trec'] == trec]


    def build(self, trec, build_path, overwrite=False):

        runs = self.filter_by_trec(self.runs, trec)
        participants = self.filter_by_trec(self.participants, trec)
        publications = self.filter_by_trec(self.publications, trec)
        datasets = self.filter_by_trec(self.datasets, trec)
        tracks = self.filter_by_trec(self.tracks, trec)
        results = self.filter_by_trec(self.results, trec)
        
        # Mapping from page type to the sets that block their creation for a given (trec, track)
        skip_conditions = {
            'publications': self.no_proceedings,
            'runs': self.no_runs,
            'results': self.no_summary,
            'participants': self.no_participants,
            'data': self.no_data,
        }

        trec_path = os.path.join('.', 'browser', 'src', 'docs', trec)
        os.makedirs(trec_path, exist_ok=True)

        # Always write overview page
        self.write_page(trec=trec, tracks=tracks, type='overview', build_path=build_path)

        # Write proceedings if allowed
        if trec not in ['trec-covid', 'trec32']:
            self.write_page(trec=trec, tracks=tracks, publications=publications, runs=runs, type='proceedings', build_path=build_path)

        tracks_for_trec = tracks[tracks['trec'] == trec].track.unique()
        for track in tracks_for_trec:
            trec_track = (trec, track)
            for page_type in ['track_overview', 'publications', 'runs', 'results', 'participants', 'data']:
                # Skip page if condition matches
                if page_type in skip_conditions and trec_track in skip_conditions[page_type]:
                    continue
                self.write_page(
                    type=page_type,
                    trec=trec,
                    track=track,
                    tracks=tracks,
                    participants=participants,
                    runs=runs,
                    results=results,
                    publications=publications,
                    datasets=datasets,
                    build_path=build_path
                )


    def build_all(self, build_path, overwrite=False):

        trecs = []
        for file_path in self.base_path.glob('trec*'):
            trecs.append(file_path.name)

        for trec in tqdm(trecs):
            self.build(trec=trec, build_path=build_path, overwrite=overwrite)
    