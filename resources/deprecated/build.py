#!/usr/bin/env python
# coding: utf-8

# #### Setup

# In[1]:


## uncomment to install packages
# %pip install pyyaml==6.0.1 docutils==0.20.1 sqlalchemy==2.0.22 pandas==2.1.1 tqdm==4.66.2


# #### Imports

# In[2]:


import os
import re 
import json
import pandas as pd
from tqdm import tqdm
import yaml
from sqlalchemy import create_engine
from docutils.nodes import make_id


# #### Load data

# In[3]:


sqlite_filepath = '../trec.sqlite'
engine = create_engine(f"sqlite:///{sqlite_filepath}")
runs = pd.read_sql_table('runs', engine) 
participants = pd.read_sql_table('participants', engine) 
publications = pd.read_sql_table('publications', engine) 
tracks = pd.read_sql_table('tracks', engine) 
datasets = pd.read_sql_table('datasets', engine) 
results = pd.read_sql_table('results', engine) 


# #### Missing metadata

# In[4]:


# list with (trec, track) tuples
_trec_track = []
for row in tracks.iterrows():
    _trec_track.append((row[1].trec, row[1].track))

no_input = []
no_summary = []
no_appendix = []
no_proceedings = []
no_runs = []
no_participants = []
no_data = []

# no parsing is implemented, but summary files are available online
no_parsing = [ 
    ('trec32', 'crisis'),
    ('trec31', 'crisis'),
    ('trec31', 'fair'),
    ('trec30', 'fair'),
    ('trec29', 'fair'),
    ('trec28', 'fair'),
    ('trec27', 'incident'),
    ('trec26', 'rts'),
    ('trec25', 'realtime'),
    ('trec24', 'domain'),
    ('trec24', 'tempsumm'),
    ('trec21', 'crowd'),
    ('trec19', 'session'),
    ('trec17', 'relfdbk'),
    ('trec17', 'million-query'),
    ('trec16', 'qa'),
    ('trec15', 'qa'),
    ('trec14', 'qa'),
    ('trec13', 'qa'),
    ('trec12', 'qa'),
    ('trec11', 'qa'),
    ('trec10', 'qa'),
    ('trec9', 'qa'),
    ('trec8', 'qa'),
    ('trec7', 'filtering'),
    ('trec4', 'filtering'),
]

# no data
nd = datasets[datasets['corpus'].isna() & 
              datasets['topics'].isna() & 
              datasets['qrels'].isna() & 
              datasets['ir_datasets'].isna() & 
              datasets['trec_webpage'].isna() & 
              datasets['other'].isna()]
for row in nd.iterrows():
    no_data.append((row[1].trec, row[1].track))

# no runs, no participants, no inputs, no summaries, no appendices, no publications
for t in _trec_track:
    r = runs[(runs['trec'] == t[0]) & (runs['track'] == t[1])]
    if not len(r):
        no_runs.append(t)
        no_participants.append(t)
    if len(r[r['input_url'].isna()]) == len(r):
        no_input.append(t)
    if len(r[r['summary_url'].isna()]) == len(r):
        if (t[0], t[1]) not in [
            # these tracks have results in the database
            ('trec-covid', 'round5'),
            ('trec-covid', 'round4'),
            ('trec-covid', 'round3'),
            ('trec-covid', 'round2'),
            ('trec-covid', 'round1'),
            ('trec19', 'chemical'),
            ('trec11', 'xlingual'),
            ('trec5', 'dbmerge'),
            ('trec32', 'crisis'),
        ]:
            no_summary.append(t)
    if len(r[r['appendix_url'].isna()]) == len(r):
        no_appendix.append(t)

    p = publications[(publications['trec'] == t[0]) & (publications['track'] == t[1])]
    if not len(p):
        no_proceedings.append(t)

# add summaries for that no parsing is implemented
no_summary = no_summary + no_parsing


# #### Helper functions

# In[5]:


def is_json(json_data):
    """Check if a string is interpretable as JSON."""
    
    if json_data:
        try:
            json.loads(json_data)
        except ValueError:
            return False
        return True
    else:
        return False
    

def convert(json_data, bold=False, single_key=None):
    """Convert a (JSON-formatted) string to a markdown reference."""

    if is_json(json_data):
        content = []
        d = json.loads(json_data)
        for k, v in d.items():
            if bold:
                ref = ''.join(['[**`', k, '`**](', v, ')'])
            else:
                ref = ''.join(['[`', k, '`](', v, ')'])
            content.append(ref)
        
        return ' | '.join(content)
    
    key = single_key if single_key else json_data

    if bold:
        ref = ''.join(['[**`', key, '`**](', json_data, ')'])
    else:
        ref = ''.join(['[`', key, '`](', json_data, ')'])
    
    return ref


def trec_year(trec_name):
    """Get the year of a TREC iteration."""

    if trec_name == 'trec-covid':
        return 2020
    iteration = re.findall(r'\d+', trec_name)
    return 1991 + int(iteration[0])


def track_map(tracks):
    """Get a dictionary with track acronyms as keys and their full names as values."""

    track_names = {}
    unique_trecs = tracks.trec.unique()
    for trec in unique_trecs:
        unique_tracks = tracks[tracks['trec']==trec]['track'].unique()
        _track_names = {}
        for track in unique_tracks:
            fullname = tracks[(tracks['trec']==trec) & (tracks['track']==track)].fullname.iloc[0]
            _track_names[track] = fullname
        track_names[trec] = _track_names

    return track_names


# #### Page generation functions

# In[6]:


def proceedings_page_content(trec, track, publications, runs, tracks):
    """Generate the proceedings page of a track."""
    
    pubs = publications[(publications['track'] == track) & (publications['trec'] == trec)]
    
    # Make the content block with the track's title.
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    content = ' '.join(['#', 'Proceedings', '-', track_fullname, str(trec_year(trec)), '\n\n'])
    
    # If an overview paper is available, add it.
    overview = pubs[pubs['pid'] == 'overview']
    if len(overview):
        overview_title = overview.iloc[0].title
        overview_author = overview.iloc[0].author
        overview_url = overview.iloc[0].url
        overview_bibtex = overview.iloc[0].bibtex.strip('\n\n\n\n').replace('\n', '\n\t')
        overview_biburl = str(overview.iloc[0].biburl or '')
        overview_abstract = overview.iloc[0].abstract
        content += '#### ' + overview_title + '\n\n'
        content += '_{}_\n\n'.format(overview_author)
        content += '- :material-file-pdf-box: **Paper:** [{0}]({0})\n'.format(overview_url)
        if overview_abstract:
            content += '??? abstract "Abstract"\n\t\n\t{}\n\t\n\n'.format(overview_abstract)
        content += '??? quote "Bibtex [:material-link-variant:]({}) "\n\t```\n\t{}\n\t```\n\n'.format(overview_biburl, overview_bibtex)

    # Add other papers.
    for pub in pubs.iterrows():

        # The overview paper is already added.
        if pub[1].pid == 'overview':
            continue

        # Add title and author to the content block.
        content += '#### {}\n\n_{}_\n\n'.format(pub[1].title, pub[1].author)

        # Add reference to participants page.
        if (trec, track) not in no_participants:
            content += '- :fontawesome-solid-user-group: **Participant:** [{}](./participants.md#{})\n'.format(pub[1].pid, pub[1].pid.lower())
        
        # Add URL of the paper.
        content += '- :material-file-pdf-box: **Paper:** [{0}]({0})\n'.format(pub[1].url)

        # Add runs references.
        runs_str_list = []
        _runs = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['pid'] == pub[1].pid)]
        if len(_runs):
            for _run in _runs.iterrows():
                runs_str_list.append('[{}](./runs.md#{})'.format(_run[1].runid, _run[1].runid.lower()))
            runs_str = ' | '.join(runs_str_list) 
            content += '- :material-file-search: **Runs:** {}\n\n'.format(runs_str)
        else: 
            content += '\n'

        # Add the abstract if available 
        abstract = pub[1].abstract
        if abstract:
            content += '??? abstract "Abstract"\n\t\n\t{}\n\t\n\n'.format(abstract)

        # Add the BibTeX info.
        bibtex = pub[1].bibtex.strip('\n\n\n\n').replace('\n', '\n\t')
        content += '??? quote "Bibtex [:material-link-variant:]({}) "\n\t```\n\t{}\n\t```\n\n'.format(pub[1].biburl, bibtex)

    return content


def results_page_content(trec, track, tracks, runs, results, publications):
    """Generate the results page of a track."""

    # Make the content block with track's title.
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    content = '---\nsearch:\n  exclude: true\n---\n\n' # Exclude the results page from the search index.
    content += ' '.join(['#', 'Results', '-', track_fullname, str(trec_year(trec)), '\n\n'])

    # Get the runs and summaries of the track.
    runids = runs[(runs['trec'] == trec) & (runs['track'] == track)].runid.unique()
    summaries = results[(results['trec'] == trec) & (results['track'] == track) & (results['measure'] == 'summary')]

    # The summaries of session track runs contain the results of multiple run files (RL1, RL2, RL3, RL4)     
    if track == 'session':
        _runids = [''.join(runid.split('.')[:-1]) for runid in runids]
        runids = set(_runids)
        
    for runid in runids:
        _summaries = summaries[summaries['runid'] == runid]
        if len(_summaries) < 1: 
            continue
        content += '#### {} \n'.format(runid)

        # Add quick access references
        run = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['runid'] == runid)]
        if track == 'session': # Session track requires a special run reference 
            run = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['runid'] == runid + '.RL1')]
        if len(run) > 0:
            run_url_id = run.iloc[0].runid.lower().replace('.', '')
            content += '[**`Metadata`**](./runs.md#{})'.format(run_url_id)
            participant_url_id = run.iloc[0].pid.lower().replace('.', '')
            content += ' | [**`Participants`**](./participants.md#{})'.format(participant_url_id)
            title = publications[(publications['trec'] == trec) & (publications['track'] == track) & (publications['pid'] == run.iloc[0].pid)]
            if len(title) > 0:
                _title = make_id(title.title.iloc[0])
                content += ' | [**`Proceedings`**](./proceedings.md#{})'.format(_title)
            input_url = run.iloc[0].input_url
            if input_url:
                content += ' '.join(['|', convert(input_url, bold=True, single_key='Input')])
            summary_url = run.iloc[0].summary_url
            if summary_url:
                content += ' '.join(['|', convert(summary_url, bold=True, single_key='Summary')])
            appendix_url = run.iloc[0].appendix_url
            if appendix_url:
                content += ' '.join(['|', convert(appendix_url, bold=True, single_key='Appendix')])
            content += '\n'

        # Add the (short version of the) summary.
        for summary in _summaries.iterrows():
            content += '??? example "summary ({})"\n\t```\n{}\n\t```\n'.format(summary[1].eval, summary[1].score)
        content += '---\n'

    return content


def runs_page_content(trec, track, publications, runs, tracks):
    """Generate the runs page of a track."""

    _runs = runs[(runs['trec'] == trec) & (runs['track'] == track)]
    _runs = _runs.sort_values(by='runid', key=lambda col: col.str.lower())

    # Make content block with track's title and year.
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    content = ' '.join(['#', 'Runs', '-', track_fullname, str(trec_year(trec)), '\n\n'])

    for run in _runs.iterrows():  

        # Add reference to the participants browser page.
        participant_url_id = run[1].pid.lower().replace('.', '')
        if (trec, track) in no_summary:
            ref = '[**`Participants`**](./participants.md#{})'.format(participant_url_id)
        else:
            result_url_id = run[1].runid.lower().replace('.', '')
            if track == 'session':
                result_url_id = ''.join(run[1].runid.lower().split('.')[:-1])
            ref = '[**`Results`**](./results.md#{}) | [**`Participants`**](./participants.md#{})'.format(result_url_id, participant_url_id)

        # Add reference to the publications browser page.
        title = publications[(publications['trec'] == trec) & (publications['track'] == track) & (publications['pid'] == run[1].pid)]
        if len(title) > 0:
            _title = make_id(title.title.iloc[0])
            ref += ' | [**`Proceedings`**](./proceedings.md#{})'.format(_title)

        # Add reference to the input file hosted on the TREC servers.
        input_url = run[1].input_url
        if input_url:
            if len(input_url) > 0:
                ref = ' | '.join([ref, convert(input_url, bold=True, single_key='Input')])

        # Add reference to the summary file hosted on the TREC servers.
        summary_url = run[1].summary_url
        if summary_url:
            if len(summary_url) > 0:
                ref = ' | '.join([ref, convert(summary_url, bold=True, single_key='Summary')])

        # Add reference to the appendix file hosted on the TREC servers.
        appendix_url = run[1].appendix_url
        if appendix_url:
            if len(appendix_url) > 0:
                ref = ' | '.join([ref, convert(appendix_url, bold=True, single_key='Appendix')])

        # Add metadata card to the content.
        content += ''.join([
                        '#### ', str(run[1].runid), ' \n', ref, ' \n\n',
                        '- :material-rename: **Run ID:** ',  str(run[1].runid), ' \n',
                        '- :fontawesome-solid-user-group: **Participant:** ', run[1].pid, ' \n',
                        '- :material-format-text: **Track:** ', track_fullname, ' \n',
                        '- :material-calendar: **Year:** ', str(run[1].year), ' \n'
                ])
        
        if run[1].date:
            content += '- :material-upload: **Submission:** {} \n'.format(run[1].date)
        if run[1].type:
            content += '- :fontawesome-solid-user-gear: **Type:** {} \n'.format(run[1].type)
        if run[1].task:
            content += '- :material-text-search: **Task:** {} \n'.format(run[1].task)
        if run[1].md5:
            if len(run[1].md5) == 32:
                content += '- :material-fingerprint: **MD5:** `{}` \n'.format(str(run[1].md5).replace ('\n', ' '))
        if run[1].description:
            content += '- :material-text: **Run description:** {} \n'.format(str(run[1].description).replace ('\n', ' '))
        if run[1].other:
            repository = json.loads(run[1].other).get('repository')
            if repository:
                content += '- :material-code-tags: **Code:** [{0}]({0}) \n'.format(repository)
        content += '\n---\n'

    return content


def participants_page_content(trec, track, participants, runs, tracks):
    """Generate the participants page of a track."""

    _runs = runs[(runs['trec'] == trec)]
    pids = _runs.sort_values(by='pid', key=lambda col: col.str.lower()).pid.unique()

    # Make content block with track's title and year.
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    content = ' '.join(['#', 'Participants', '-', track_fullname, str(trec_year(trec)), '\n\n'])

    for pid in pids:
        _p_runs = []
        p_runs = runs[(runs['pid'] == pid) & (runs['trec'] == trec) & (runs['track'] == track)]
        if len(p_runs) > 0:

            # Get the name and organization of the individual who registered for the track
            try:
                organization = participants[(participants['trec'] == trec) & (participants['pid'] == pid)].organization.iloc[0]
                name = participants[(participants['trec'] == trec) & (participants['pid'] == pid)].name.iloc[0]
            except:
                organization = ''
                name = ''

            # Make references for all of the runs that belong to the participants.
            for p_run in p_runs.iterrows():
                run_url_id = p_run[1].runid.lower().replace('.', '')
                run_ref = '[{}](./runs.md#{})'.format(p_run[1].runid, run_url_id)
                _p_runs.append(run_ref)
            run_append = ' | '.join(_p_runs)

            # Add the metadata to the content block.
            content += '#### {}\n'.format(str(pid)) 
            if name: 
                content += ' - :fontawesome-solid-user-group: **Name:** {}\n'.format(name) 
            if organization:
                content += ' - :octicons-organization-16: **Organization:** {}\n'.format(organization) 
            if len(run_append) > 2:
                content += ' - :material-file-search: **Runs:** {}\n'.format(run_append)
            else:
                content += '\n'    

            content += '\n---\n'

    return content


def track_overview_page_content(trec, track, tracks):
    """Generate the content of a track overview page."""

    # Make the quick access with references to subpages of the browser.
    quick_access_parts = []
    if (trec, track) not in no_proceedings:
        quick_access_parts.append('[`Proceedings`](./proceedings.md)')
    if (trec, track) not in no_data:
        quick_access_parts.append('[`Data`](./data.md)')
    if (trec, track) not in no_summary:
        quick_access_parts.append('[`Results`](./results.md)')
    if (trec, track) not in no_runs:
        quick_access_parts.append('[`Runs`](./runs.md)')
    if (trec, track) not in no_participants:
        quick_access_parts.append('[`Participants`](./participants.md)')
    quick_access_str = ' | '.join(quick_access_parts)
    quick_access = quick_access_str

    # Make the header/title
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    heading = ' '.join(['#', 'Overview', '-', track_fullname, str(trec_year(trec))])

    # Get the description of the track.
    description = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].description.iloc[0]
    description = '' if not description else description # make empty string if none

    # Make the content block.
    content = ''.join([heading, '\n\n', quick_access, '\n\n', '{==\n\n', description, '\n\n==}\n\n'])

    # Add the track's coordinators to the content block.
    _coordinators = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].coordinators.iloc[0]
    if _coordinators:
        coordinators = ''
        for _coordinator in _coordinators.split(':'):
            coordinators += ' '.join(['-', _coordinator, '\n'])
        if len(coordinators) > 0:
            content += ':fontawesome-solid-user-group: **Track coordinator(s):**\n\n{}\n'.format(coordinators)

    # If the track has different tasks, list them.
    tasks = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].tasks.iloc[0]
    if tasks:
        if len(tasks):
            content += ':material-text-search: **Tasks:**\n\n' 
            _tasks = json.loads(tasks)
            for k, v in _tasks.items():
                content += '- `{}`: {} \n'.format(k, v)
            content += '\n'

    # If a webpage is available, add it to the content block.
    webpage = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].webpage.iloc[0]
    if webpage:
        if len(webpage):
            webpage_ref = '[`{0}`]({0})'.format(webpage)
            content += ':fontawesome-solid-globe: **Track Web Page:** {} \n\n---\n\n'.format(webpage_ref)
    else: 
        content += '\n\n---\n\n'

    return content


def overview_page_covid(trec, tracks):
    """Generate the overview page of a TREC-COVID"""

    # Make the title of the TREC-COVID's overview page.
    content = ' '.join(['#', 'TREC-COVID', str(trec_year(trec)), '\n\n'])

    # Make the quick access with references to subpages of the browser.
    quick_access = ''
    for track in tracks[tracks['trec'] == trec].track.unique():
        quick_access_parts = ['[`Overview`](./{0}/overview.md)']
        if (trec, track) not in no_proceedings:
            quick_access_parts.append('[`Proceedings`](./{0}/proceedings.md)')
        if (trec, track) not in no_data:
            quick_access_parts.append('[`Data`](./{0}/data.md)')
        if (trec, track) not in no_summary:
            quick_access_parts.append('[`Results`](./{0}/results.md)')
        if (trec, track) not in no_runs:
            quick_access_parts.append('[`Runs`](./{0}/runs.md)')
        if (trec, track) not in no_participants:
            quick_access_parts.append('[`Participants`](./{0}/participants.md)')
        round_name = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
        quick_access_str = ' | '.join(quick_access_parts)
        quick_access_round = '**' + round_name + ':** ' +  quick_access_str.format(track) + '\n\n'
        quick_access += quick_access_round

    # Add the description and coordinators of TREC-COVID.
    description = tracks[(tracks['trec'] == trec) & (tracks['track'] == 'round1')].description.iloc[0]
    content += ''.join([quick_access, '\n\n', '{==\n\n', description, '\n\n==}\n\n'])
    _coordinators = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].coordinators.iloc[0]
    if _coordinators:
        coordinators = ''
        for _coordinator in _coordinators.split(':'):
            coordinators += ' '.join(['-', _coordinator, '\n'])
        content += ''.join([':fontawesome-solid-user-group: **Track coordinator(s):**\n\n', coordinators, '\n\n'])

    # Add a reference to TREC-COVID's website.
    webpage = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].webpage.iloc[0]
    if webpage:
        webpage_ref = '[`{0}`]({0})'.format(webpage)
        content += ':fontawesome-solid-globe: **Track Web Page:** {} \n\n---\n\n'.format(webpage_ref)
    else: 
        content += '\n\n---\n\n'

    return content 


def overview_page_content(trec, tracks):
    """Generate the overview page of a TREC with all track overviews."""

    if trec == 'trec-covid':
        return overview_page_covid(trec, tracks)

    # Make the title of the TREC iteration's overview page.
    content = ' '.join(['#', 'Text REtrieval Conference (TREC)', str(trec_year(trec)), '\n\n'])

    for track in tracks[tracks['trec'] == trec].track.unique():
        
        # Make the quick access with references to subpages of the browser.
        quick_access_parts = ['[`Overview`](./{0}/overview.md)']
        if (trec, track) not in no_proceedings:
            quick_access_parts.append('[`Proceedings`](./{0}/proceedings.md)')
        if (trec, track) not in no_data:
            quick_access_parts.append('[`Data`](./{0}/data.md)')
        if (trec, track) not in no_summary:
            quick_access_parts.append('[`Results`](./{0}/results.md)')
        if (trec, track) not in no_runs:
            quick_access_parts.append('[`Runs`](./{0}/runs.md)')
        if (trec, track) not in no_participants:
            quick_access_parts.append('[`Participants`](./{0}/participants.md)')
        quick_access_str = ' | '.join(quick_access_parts)
        quick_access = quick_access_str.format(track)

        # Get the name, descriptions, and coordinators of a track.
        track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
        description = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].description.iloc[0]
        description = '' if not description else description 

        # Add track information to the content block.
        content += ''.join(['## ', track_fullname, '\n\n', quick_access, '\n\n', '{==\n\n', description, '\n\n==}\n\n'])

        # If the track has coordinators, add it to the content block.
        _coordinators = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].coordinators.iloc[0]
        if _coordinators:
            coordinators = ''
            for _coordinator in _coordinators.split(':'):
                coordinators += ' '.join(['-', _coordinator, '\n'])
            content += ''.join([':fontawesome-solid-user-group: **Track coordinator(s):**\n\n', coordinators, '\n\n'])

        # If the track has a webpage, add it to the content block.
        webpage = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].webpage.iloc[0]
        if webpage:
            webpage_ref = '[`{0}`]({0})'.format(webpage)
            content += ':fontawesome-solid-globe: **Track Web Page:** {} \n\n---\n\n'.format(webpage_ref)
        else: 
            content += '\n\n---\n\n'
            
    return content


def data_page_content(trec, track, tracks, datasets):
    """Generate the content of a data page."""

    # Make the title/header of the page.
    track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
    content = ' '.join(['#', 'Data', '-', track_fullname, str(trec_year(trec)), '\n\n'])

    # Add the TREC's website of the data if available.
    trec_webpage = datasets[(datasets['trec'] == trec) & (datasets['track'] == track)].trec_webpage.iloc[0]
    if trec_webpage:
        webpage = ':fontawesome-solid-globe: **`trec.nist.gov`**: [`{0}`]({0})'.format(trec_webpage)
    else:
        webpage = ''
    content += '{}\n\n---\n\n'.format(webpage)

    # Add links to the corpus, the topics, the qrels, and ir_datasets if available.
    tasks = datasets[(datasets['trec'] == trec) & (datasets['track'] == track)]
    task_content = []
    corpus = tasks.corpus.iloc[0]
    if corpus:
        task_content.append('- :material-database: **Corpus**: {}\n'.format(convert(corpus)))
    topics = tasks.topics.iloc[0]
    if topics:
        task_content.append('- :octicons-question-16: **Topics**: {}\n'.format(convert(topics)))
    qrels = tasks.qrels.iloc[0]
    if qrels:
        task_content.append('- :material-label: **Qrels**: {}\n'.format(convert(qrels))) 
    ir_datasets = tasks.ir_datasets.iloc[0]
    if ir_datasets:
        task_content.append('- :material-database-outline: **ir_datasets**: {}\n'.format(convert(ir_datasets)))
    task_content.append('\n\n---\n\n')
    content += ''.join(task_content)

    # Add links to other data resources if available.
    other = datasets[(datasets['trec'] == trec) & (datasets['track'] == track)].other.iloc[0]
    if other:
        content += '**Other:** {}\n'.format(convert(other))

    return content


def proceedings_content(trec, tracks):
    """Generate the proceedings page of a TREC including all tracks."""
 
    # Make the title of the TREC iteration's proceedings page.
    content = ' '.join(['#', 'Proceedings', str(trec_year(trec)), '\n\n'])

    # Add overview paper of the entire conference if available.
    pubs = publications[(publications['track'] == 'overview') & (publications['trec'] == trec)]
    if len(pubs) > 0:
        overview = pubs[pubs['pid'] == 'overview']
        overview_title = overview.iloc[0].title
        overview_author = overview.iloc[0].author
        overview_url = overview.iloc[0].url
        overview_bibtex = overview.iloc[0].bibtex.strip('\n\n\n\n').replace('\n', '\n\t')
        overview_biburl = str(overview.iloc[0].biburl or '')
        overview_abstract = overview.iloc[0].abstract
        content += '## ' + overview_title + '\n\n'
        content += '_{}_\n\n'.format(overview_author)
        content += '- :material-file-pdf-box: **Paper:** [{0}]({0})\n'.format(overview_url)
        if overview_abstract:
            content += '??? abstract "Abstract"\n\t\n\t{}\n\t\n\n'.format(overview_abstract)
        content += '??? quote "Bibtex [:material-link-variant:]({})"\n\t```\n\t{}\n\t```\n\n'.format(overview_biburl, overview_bibtex)

    # Add the papers of individual tracks. (the following code is similar to that of proceedings_page_content())
    for track in tracks[tracks['trec'] == trec].track.unique():
        pubs = publications[(publications['track'] == track) & (publications['trec'] == trec)]
    
        # Make the content block with the track's title.
        track_fullname = tracks[(tracks['trec'] == trec) & (tracks['track'] == track)].fullname.iloc[0]
        content += ' '.join(['##', track_fullname, '\n\n'])
        
        # If an overview paper is available, add it.
        overview = pubs[pubs['pid'] == 'overview']
        if len(overview):
            overview_title = overview.iloc[0].title
            overview_author = overview.iloc[0].author
            overview_url = overview.iloc[0].url
            overview_bibtex = overview.iloc[0].bibtex.strip('\n\n\n\n').replace('\n', '\n\t')
            overview_biburl = str(overview.iloc[0].biburl or '')
            overview_abstract = overview.iloc[0].abstract
            content += '#### ' + overview_title + '\n\n'
            content += '_{}_\n\n'.format(overview_author)
            content += '- :material-file-pdf-box: **Paper:** [{0}]({0})\n'.format(overview_url)
            if overview_abstract:
                content += '??? abstract "Abstract"\n\t\n\t{}\n\t\n\n'.format(overview_abstract)
            content += '??? quote "Bibtex [:material-link-variant:]({}) "\n\t```\n\t{}\n\t```\n\n'.format(overview_biburl, overview_bibtex)

        # Add other papers.
        for pub in pubs.iterrows():

            # The overview paper is already added.
            if pub[1].pid == 'overview':
                continue

            # Add title and author to the content block.
            content += '#### {}\n\n_{}_\n\n'.format(pub[1].title, pub[1].author)

            # Add reference to participants page.
            if (trec, track) not in no_participants:
                content += '- :fontawesome-solid-user-group: **Participant:** [{}](./{}/participants.md#{})\n'.format(pub[1].pid, track, pub[1].pid.lower())
            
            # Add URL of the paper.
            content += '- :material-file-pdf-box: **Paper:** [{0}]({0})\n'.format(pub[1].url)

            # Add runs references.
            runs_str_list = []
            _runs = runs[(runs['trec'] == trec) & (runs['track'] == track) & (runs['pid'] == pub[1].pid)]
            if len(_runs):
                for _run in _runs.iterrows():
                    runs_str_list.append('[{}](./{}/runs.md#{})'.format(_run[1].runid, track, _run[1].runid.lower()))
                runs_str = ' | '.join(runs_str_list) 
                content += '- :material-file-search: **Runs:** {}\n\n'.format(runs_str)
            else: 
                content += '\n'

            # Add the abstract if available
            abstract = pub[1].abstract
            if abstract:
                content += '??? abstract "Abstract"\n\t\n\t{}\n\t\n\n'.format(abstract)
                
            # Add the BibTeX info.
            bibtex = pub[1].bibtex.strip('\n\n\n\n').replace('\n', '\n\t')
            content += '??? quote "Bibtex [:material-link-variant:]({}) "\n\t```\n\t{}\n\t```\n\n'.format(pub[1].biburl, bibtex)

    return content


def write_page(type, **args):
    """Generate browser pages of different types."""

    if type in ['overview', 'proceedings']:
        if type == 'overview':
            page_content = overview_page_content(args['trec'], args['tracks'])
            file_name = 'overview.md'
        if type == 'proceedings':
            page_content = proceedings_content(args['trec'], args['tracks'])
            file_name = 'proceedings.md'
        conf_path = os.path.join('.', 'src', 'docs', args['trec'])
        os.makedirs(conf_path, exist_ok=True)
        results_path = os.path.join(conf_path, file_name)
        with open(results_path, 'w') as f_out:  
            f_out.write(page_content) 
        return 
    
    if type == 'publications':
        page_content = proceedings_page_content(args['trec'], args['track'], args['publications'], args['runs'], args['tracks'])
        file_name = 'proceedings.md'
    if type == 'results':
        page_content = results_page_content(args['trec'], args['track'], args['tracks'], args['runs'], args['results'], args['publications'])
        file_name = 'results.md'
    if type == 'runs':
        page_content = runs_page_content(args['trec'], args['track'], args['publications'], args['runs'], args['tracks'])
        file_name = 'runs.md'
    if type == 'participants':
        page_content = participants_page_content(args['trec'], args['track'], args['participants'], args['runs'], args['tracks'])
        file_name = 'participants.md'
    if type == 'track_overview':
        page_content = track_overview_page_content(args['trec'], args['track'], args['tracks'])
        file_name = 'overview.md'
    if type == 'data':
        page_content = data_page_content(args['trec'], args['track'], args['tracks'], args['datasets'])
        file_name = 'data.md'
    
    track_path = os.path.join('.', 'src', 'docs', args['trec'], args['track'])
    os.makedirs(track_path, exist_ok=True)
    results_path = os.path.join(track_path, file_name)
    with open(results_path, 'w') as f_out:  
        f_out.write(page_content)   


# #### Write page contents

# In[ ]:


for trec in tqdm(runs.trec.unique()):
    trec_path = os.path.join('.', 'src', 'docs', trec)
    os.makedirs(trec_path, exist_ok=True)
    write_page(trec=trec, tracks=tracks, type='overview')
    if trec not in ['trec-covid']: # TREC-COVID does not have proceedings
        write_page(trec=trec, tracks=tracks, type='proceedings')
    _tracks = tracks[tracks['trec'] == trec].track.unique()
    for track in _tracks:
        for t in ['track_overview', 'publications', 'runs', 'results', 'participants', 'data']:
            if (trec, track) in no_proceedings and t == 'publications':
                continue
            elif (trec, track) in no_runs and t == 'runs':
                continue
            elif (trec, track) in no_summary and t == 'results':
                continue
            elif (trec, track) in no_participants and t == 'participants':
                continue
            elif (trec, track) in no_data and t == 'data':
                continue
            else:
                write_page(type=t, trec=trec, track=track, tracks=tracks, participants=participants, 
                           runs=runs, results=results, publications=publications, datasets=datasets)  


# #### Write ./browser/src/docs/index.md

# In[ ]:


content = '<center>\n\n<h1>Text REtrieval Conference (TREC)</h1>\n\n<img src="./assets/logo.png" alt="logo" width="50%"/>\n\n[`Proceedings`](./proceedings.md) __|__ [`Data`](./data.md) __|__ [`trec.nist.gov`](https://trec.nist.gov/)\n\n<img src="./assets/tracks.png" alt="tracks"/>\n\n</center>\n\n'

track_overview = {}
for row in tracks.iterrows():
    fullname = row[1].fullname
    trec = row[1].trec
    track = row[1].track
    trec_and_year = '{} ({})'.format('-'.join([trec[:4].upper(), trec[4:]]),  str(trec_year(trec)))
    overview_path = os.path.join('.', trec, track, 'overview.md')
    if trec == 'trec-covid':
        continue # the overview page won't feature overviews of every single round
    if trec == 'trec1':
        overview_path = os.path.join('.', trec, 'overview.md')
    ref = '[`{}`]({})'.format(trec_and_year, overview_path)
    if track_overview.get(fullname):
        track_overview[fullname].append(ref)
    else:
        track_overview[fullname] = [ref]

track_overview = {key: value for key, value in sorted(track_overview.items())}
# sort dict by keys alphabetically regardless of capitalization
track_overview = dict(sorted(track_overview.items(), key=lambda x: x[0].lower()))

for track, iterations in track_overview.items():
    _trecs = ' | '.join(iterations)
    content += '#### {}\n{}\n'.format(track, _trecs)

with open('./src/docs/index.md', 'w') as f_out:
    f_out.write(content)


# #### Write ./browser/src/docs/data.md

# In[ ]:


intro = ''
content = '# Data\n\n:fontawesome-solid-globe: **`trec.nist.gov`:** [`https://trec.nist.gov/data.html`](https://trec.nist.gov/data.html)\n\n'

track_overview = {}
for row in tracks.iterrows():
    fullname = row[1].fullname
    trec = row[1].trec
    track = row[1].track
    trec_and_year = '{} ({})'.format('-'.join([trec[:4].upper(), trec[4:]]),  str(trec_year(trec)))
    overview_path = os.path.join('.', trec, track, 'data.md')
    if trec == 'trec-covid':
        continue
    if trec == 'trec1':
        overview_path = os.path.join('.', trec, 'overview.md')
    ref = '[`{}`]({})'.format(trec_and_year, overview_path)
    if (trec, track) not in no_data:
        if track_overview.get(fullname):
            track_overview[fullname].append(ref)
        else:
            track_overview[fullname] = [ref]
    track_overview['TREC-COVID'] = [
        '[`Round 1`](trec-covid/round1/data.md)',
        '[`Round 2`](trec-covid/round2/data.md)',
        '[`Round 3`](trec-covid/round3/data.md)',
        '[`Round 4`](trec-covid/round4/data.md)',
        '[`Round 5`](trec-covid/round5/data.md)'
        ]

track_overview = {key: value for key, value in sorted(track_overview.items())}

for track, iterations in track_overview.items():
    _trecs = ' | '.join(iterations)
    content += '#### {}\n{}\n'.format(track, _trecs)

with open('./src/docs/data.md', 'w') as f_out:
    f_out.write(content)


# #### Write ./browser/src/mkdocs.yml file

# In[ ]:


tm = track_map(tracks)
trecs = list(runs['trec'].unique())
trecs.reverse()
_trecs = []

for trec in trecs:
    _tracks = []
    for key, full_name in tm.get(trec).items():
        track_menu = [{'Overview': os.path.join(trec, key, 'overview.md')}]
        if (trec, key) not in no_data:
            track_menu.append({'Data': os.path.join(trec, key, 'data.md')})
        if (trec, key) not in no_participants:
            track_menu.append({'Participants': os.path.join(trec, key, 'participants.md')})
        if (trec, key) not in no_runs:
            track_menu.append({'Runs': os.path.join(trec, key, 'runs.md')})
        if (trec, key) not in no_summary:
            track_menu.append({'Results': os.path.join(trec, key, 'results.md')})
        if (trec, key) not in no_proceedings:
            track_menu.append({'Proceedings': os.path.join(trec, key, 'proceedings.md')})
        _tracks.append({full_name: track_menu})
    trec_key = '{} ({})'.format('-'.join([trec[:4].upper(), trec[4:]]), str(trec_year(trec)))
    if trec == 'trec-covid':
        trec_key = trec.upper()
    if trec not in ['trec-covid']:
        _trecs.append({trec_key: [{'Overview': os.path.join(trec, 'overview.md')},
                                  {'Proceedings': os.path.join(trec, 'proceedings.md')}] + _tracks})
    else:
        _trecs.append({trec_key: [{'Overview': os.path.join(trec, 'overview.md')}] + _tracks})

# TREC-1 has only an overview
_trecs.append({'TREC-1 (1992)': [{'Overview': 'trec1/overview.md'}]})

nav = [{'Home': 'index.md'}] + _trecs  

content = {'site_name': 'TREC Browser',
            'site_url': 'https://pages.nist.gov/trec-browser',
            'theme': {'name': 'material',
                     'logo': 'assets/search.svg',
                     'icon': {'repo': 'fontawesome/brands/git-alt'},
                     'palette': [{'scheme': 'default',
                                  'primary': 'light blue',
                                  'accent': 'light blue',
                                  'toggle': {'icon': 'material/toggle-switch',
                                             'name': 'Switch to dark mode'}},
                                 {'scheme': 'slate',
                                  'primary': 'light blue',
                                  'accent': 'light blue',
                                  'toggle': {'icon': 'material/toggle-switch-off-outline',
                                             'name': 'Switch to light mode'}}],
                     'features': ['content.code.copy', 'navigation.instant']},
            'repo_url': 'https://github.com/usnistgov/trec-browser',
            'repo_name': 'usnistgov/trec-browser',
            'markdown_extensions': [
                'def_list',
                'attr_list',
                'admonition',
                'pymdownx.details',
                'pymdownx.superfences',
                {'pymdownx.emoji': {
                    'emoji_index': '!!python/name:material.extensions.emoji.twemoji',
                    'emoji_generator': '!!python/name:material.extensions.emoji.to_svg'
                }},
                'pymdownx.critic',
                'pymdownx.caret',
                'pymdownx.keys',
                'pymdownx.mark',
                'pymdownx.tilde',
                {'toc': {'permalink': 'true'}}
                ],
            'extra_css': [
                'https://pages.nist.gov/nist-header-footer/css/nist-combined.css'
            ],
            'extra_javascript': [
                'https://code.jquery.com/jquery-3.6.2.min.js',
                'https://pages.nist.gov/nist-header-footer/js/nist-header-footer.js'
            ],
            'nav': nav,
            'not_in_nav': '\n/proceedings.md\n/data.md'                               
          }

with open('./src/mkdocs.yml', 'w') as f_out:
    output = yaml.dump(content, sort_keys=False)
    output = output.replace("'","")
    f_out.write(output)

