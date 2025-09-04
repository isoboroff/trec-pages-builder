#!/usr/bin/env python
# coding: utf-8

import re
import os
import json
import urllib
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from pylatexenc.latex2text import LatexNodes2Text
import bibtexparser

# entries in the 'track' column that do not correspond to actual tracks
no_tracks = [
    'application', 
    'proceedings', 
    'poster', 
    'notebook', 
    'xpm',
    'Xpm',
    'xfair', 
    'xcast', 
    'xdeep', 
    'xtask', 
    'xcontext', 
    'xmicroblog', 
    'xsession', 
    'xclinical', 
    'XHARD',
    'coordinators',
    'overviews',
]

no_tasks =  [
    'human?',
    'N/A',
    'reco',
    'NOTSPEC',
    'REPLACED',
    '50',
    '250',
    'fixed',
    'rolling',
    '10',
    '01',
    '11',
    'opt',
    'required2',
    '2',
]

no_type = [
    'automatic', 
    'auto', 
    'automatic-mi', 
    'relauto', 
    'manual', 
    'human-assisted',
    'base', 
    'simple', 
    'realistic', 
    'exploratory', 
    'pilot', 
    'final', 
    'interactive', 
    'active', 
    'online', 
    'feedback',
    'techassist', 
    'both', 
    'preference', 
    'clueweb12cs', 
    'clueweb12b13',
    'clueweb12full', 
    'SSOAR', 
    'CiteSeerX'
]

summary_prefixes = [
    'summary.trec_eval.', 
    'summary.trec-eval.', 
    'summary.sample-eval.', 
    'summary.QD.', 
    'summary.QE.', 
    'summary.QR.', 
    'summary.QS.', 
    'summary.ndeval.', # web
    'summary.risk-a0-nd.', # web
    'summary.risk-a1-nd.', # web
    'summary.risk-a5-nd.', # web
    'summary.risk-a10-nd.', # web
    'summary.risk-rm-a0-nd.', # web
    'summary.risk-terrier-a0-nd.', # web
    'summary.risk-rm-a5-nd.', # web
    'summary.risk-terrier-a5-nd.', # web
    'std-nd', # web 
    'summary.gdeval.', # web
    'summary.risk-a0-gd.', # web
    'summary.risk-a1-gd.', # web
    'summary.risk-a5-gd.', # web
    'summary.risk-a10-gd.', # web
    'summary.risk-rm-a0-gd.', # web
    'summary.risk-terrier-a0-gd.', # web
    'summary.risk-rm-a5-gd.', # web
    'summary.risk-terrier-a5-gd.', # web
    'std-gd', # web        
    'summary.allsubtopics.', # trec20/session
    'summary.lastquerysubtopics.', # trec20/session
    'summary.evidence-eval.', # trec29/pm
    'summary.small.', # trec19/chemical
    'summary.full.', # trec19/chemical
    'summary.eval.', # trec18/legal
    'summary.evalH.', # trec18/legal
    'summary.resid.', # trec17/legal
    'summary.residH.', # trec17/legal
    'summary.adhoc.', # trec17/legal
    'summary.adhocH.', # trec17/legal
    'summary.allrel.', # trec20/microblog
    'summary.highrel.', # trec20/microblog
    'summary.baseline.', # trec19/blog 
    'summary.topicrel.', # trec16/blog trec15/blog
    'summary.topicrel.', # trec16/blog trec15/blog
    'summary.positive.', # trec17/blog
    'summary.negative.', # trec17/blog
    'summary.feed.', # trec16/blog
    'summary.opinion.', # trec16/blog trec15/blog
    'summary.polarity.', # trec16/blog
    'summary.first.', # trec18/blog
    'summary.second.', # trec18/blog
    'summary.none.', # trec18/blog
    'summary.headline.', # trec18/blog
    'summary.tb-topics.', # trec16/million-query
    'summary.experts.', # trec16/enterprise
    'summary.document.', # trec16/enterprise
    'summary.doc-residual.', # trec16/enterprise
    'summary.doc-promotion.', # trec16/enterprise
    'summary.expert.', # trec17/enterprise
    'summary.eval.', # trec18/entity
    'summary-adhoc-', # trec23/microblog
    'summary-ttg-', # trec23/microblog
    'summary-a-', # trec24/microblog 
    'summary-b-', # trec24/microblog 
    'summary-', # trec25/task 
    'summary.', 
    'passages-eval.', 
    'treceval.', 
    'trec_eval.', 
]

summary_suffixes = [
    '.trec_eval', 
    '.ndcg', # trec31/deep
    '.lenient', # trec31/cast
    '.strict', # trec31/cast
    '.txt', # trec23/microblog
]

field_names_runs = [
    'runid', 
    'pid', 
    'email', 
    'track', 
    'type', 
    'fields', 
    'task', 
    'date', 
    'of_1', 
    'of_2', 
    'of_3', 
    'judge', 
    'merge', 
    'of_4', 
    'of_5', 
    'description', 
    'md5', 
    'notes'
] 

field_names_participants = [
    'pid', 
    'organization', 
    'email', 
    'name',
    'address', 
    'phone', 
    'fax', 
    'track-interest',
    'date', 
    'ad-form', 
    'tipster-form', 
    'trec-form-disk4', 
    'trec-form-disk5', 
    'notes'
]

field_names_covid = [
    'runid', 
    'pid', 
    'email', 
    'task', 
    'date', 
    'type', 
    'num',
    'judge',  
    'of_4', 
    'of_5', 
    'description', 
    'md5',
    'notes'
] 

run_types = [
    'automatic', 
    'auto', 
    'automatic-mi', 
    'relauto', 
    'manual', 
    'human-assisted',
    'base', 
    'simple', 
    'realistic', 
    'exploratory', 
    'pilot', 
    'final', 
    'interactive', 
    'active', 
    'online', 
    'feedback',
    'techassist', 
    'both', 
    'preference', 
    'clueweb12cs', 
    'clueweb12b13',
    'clueweb12full', 
    'SSOAR', 
    'CiteSeerX'
]

xligualalt_special_url = [
    'RaliHanE2EF', 
    'RaliHanF2EF', 
    'RaliWebE2EF', 
    'RaliWebF2EF', 
    'sleI2Ef1', 
    'sleI2Et1',
    'sleI2Etd1', 
    'tno8mx', 
    'TW8E2F', 
    'TW8F2E'
]

# measures that will be parsed from the summary files if available
trec_eval_measures = [
    'map', 
    'bpref', 
    'recip_rank',
    'P_10', 
    'P_100', 
    'P_1000', 
    'P10', 
    'P100', 
    'P1000', 
    'recall_10', 
    'recall_100', 
    'recall_1000',
    'ndcg_cut_10', 
    'ndcg_cut_100', 
    'ndcg_cut_1000', 
    'ndcg'
]

# sample eval measures that will be parsed from the summary files if available
sample_eval_measures = [
    'infAP',
    'infNDCG',
    'iP10',
    'iP100'
]

# older summaries with different formatting
old_summary = [
    ('trec14', 'robust'),
    ('trec14', 'qa'),
    ('trec14', 'HARD'),
    ('trec13', 'robust'),
    ('trec13', 'genomics'),
    ('trec12', 'robust'),
    ('trec12', 'qa'),
    ('trec12', 'hard'),
    ('trec12', 'genomics'),
    ('trec11', 'xlingual'),
    ('trec10', 'xlingual'),
    ('trec9', 'web'),
    ('trec9', 'sdr'),
    ('trec9', 'xlingual'),
    ('trec8', 'adhoc'),
    ('trec8', 'sdr'),
    ('trec8', 'web'),
    ('trec8', 'xlingual'),
    ('trec7', 'adhoc'),
    ('trec7', 'query'),
    ('trec7', 'sdr'),
    ('trec7', 'filtering'),
    ('trec7', 'xlingual'),
    ('trec6', 'adhoc'),
    ('trec6', 'routing'),
    ('trec6', 'chinese'),
    ('trec6', 'clir'),
    ('trec6', 'nlp'),
    ('trec5', 'adhoc'),
    ('trec5', 'routing'),
    ('trec5', 'Chinese'),
    ('trec5', 'dbmerge'),
    ('trec5', 'nlp'),
    ('trec5', 'Spanish'),
    ('trec4', 'adhoc'),
    ('trec4', 'routing'),
    ('trec4', 'confusion'),
    ('trec4', 'dbmerge'),
    ('trec4', 'spanish'),
    ('trec4', 'interactive'),
    ('trec3', 'adhoc'),
    ('trec3', 'routing'),
    ('trec2', 'adhoc'),
    ('trec2', 'routing')
]

# no datasets available
no_data = [
    ('trec33', 'avs'),
    ('trec33', 'vtt'),
    ('trec33', 'medvidqa'),
    ('trec27', 'centre'),
    ('trec26', 'open'),
    ('trec25', 'open'),
    ('trec25', 'recall'),
    ('trec24', 'recall'),
    ('trec22', 'crowd'),
    ('trec21', 'crowd'),
    ('trec20', 'crowd'),
    ('trec13', 'HARD'),
    ('trec11', 'video'),
    ('trec11', 'xlingual'),
    ('trec10', 'video'),
    ('trec10', 'xlingual'),
    ('trec9', 'query'),
    ('trec9', 'sdr'),
    ('trec9', 'xlingual'),
    ('trec8', 'girt'),
    ('trec8', 'xlingual'),
    ('trec7', 'query'),
    ('trec7', 'hp'),
    ('trec6', 'hp'),
    ('trec6', 'nlp'),
    ('trec6', 'vlc'),
    ('trec5', 'nlp'),
    ('trec5', 'filtering'),
    ('trec5', 'dbmerge')
]

# no summaries are available
no_summary = [ 
    ('trec33', 'actev'),
    ('trec33', 'avs'),
    ('trec33', 'biogen'),
    ('trec33', 'ccu'),
    ('trec33', 'medvidqa'),
    ('trec33', 'plaba'),
    ('trec33', 'rufeers'),
    ('trec32', 'crisis'),
    ('trec30', 'incident'),
    ('trec29', 'incident'),
    ('trec29', 'news'),
    ('trec28', 'car'),
    ('trec28', 'incident'),
    ('trec27', 'rts'),
    ('trec27', 'car'),
    ('trec27', 'centre'),
    ('trec27', 'incident'),
    ('trec26', 'qa'),
    ('trec26', 'domain'),
    ('trec26', 'open'),
    ('trec26', 'car'),
    ('trec25', 'open'),
    ('trec25', 'domain'),
    ('trec25', 'recall'),
    ('trec25', 'qa'),
    ('trec24', 'qa'),
    ('trec24', 'task'),
    ('trec24', 'recall'),
    ('trec23', 'kba'),
    ('trec23', 'context'),
    ('trec23', 'federated'),
    ('trec23', 'tempsumm'),
    ('trec22', 'kba'),
    ('trec22', 'context'),
    ('trec22', 'tempsumm'),
    ('trec22', 'federated'),
    ('trec22', 'crowd'),
    ('trec21', 'context'),
    ('trec21', 'kba'),
    ('trec20', 'legal'),
    ('trec20', 'crowd'),
    ('trec19', 'legal'),
    ('trec19', 'relfdbk'),
    ('trec13', 'HARD'),
    ('trec11', 'filtering'),
    ('trec11', 'interactive'),
    ('trec11', 'video'),
    ('trec10', 'filtering'),
    ('trec10', 'interactive'),
    ('trec10', 'video'),
    ('trec9', 'filtering'),
    ('trec9', 'query'),
    ('trec9', 'interactive'),
    ('trec8', 'filtering'),
    ('trec8', 'query'),
    ('trec8', 'girt'),
    ('trec8', 'interactive'),
    ('trec7', 'interactive'),
    ('trec6', 'filtering'),
    ('trec6', 'interactive'),
    ('trec6', 'sdr'),
    ('trec6', 'vlc'),
    ('trec5', 'vlc'),
    ('trec5', 'filtering'),
    ('trec5', 'confusion'),
    ('trec5', 'interactive'),
    ('trec4', 'filtering')
]

# summaries are available but no parsing is implemented
no_summary_parsing = [ 
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

# no appendix files available
no_appendix = [
    ('trec29', 'incident'),
    ('trec27', 'car'),
    ('trec27', 'news'),
    ('trec27', 'centre'),
    ('trec26', 'car'),
    ('trec24', 'tempsumm'),
    ('trec25', 'recall'),
    ('trec24', 'recall'),
    ('trec20', 'crowd'),
    ('trec19', 'session'),
    ('trec19', 'entity'),
    ('trec19', 'relfdbk'),
    ('trec18', 'entity'),
    ('trec17', 'enterprise'),
    ('trec11', 'interactive'),
    ('trec10', 'interactive'),
    ('trec8', 'query'),
    ('trec7', 'interactive'),
    ('trec4', 'filtering'),
]

# no input files available
no_input = [
    ('trec33', 'avs'),
    ('trec33', 'actev'),
    ('trec33', 'ccu'),
    ('trec33', 'rufeers'),
    ('trec30', 'incident'),
    ('trec29', 'incident'),
    ('trec29', 'news'),
    ('trec28', 'incident'),
    ('trec28', 'car'),
    ('trec27', 'rts'),
    ('trec27', 'car'),
    ('trec27', 'centre'),
    ('trec26', 'qa'),
    ('trec26', 'car'),
    ('trec26', 'open'),
    ('trec25', 'open'),
    ('trec25', 'recall'),
    ('trec24', 'recall'),
    ('trec22', 'crowd'),
    ('trec20', 'legal'),
    ('trec20', 'crowd'),
    ('trec19', 'chemical'),
    ('trec19', 'relfdbk'),
    ('trec19', 'legal'),
    ('trec17', 'million-query'), # URL exists but not online https://trec.nist.gov/results/trec17/08million.query.input.html
    ('trec17', 'legal'),  # URL exists but not online https://trec.nist.gov/results/trec17/08legal.adhoc.input.html
    ('trec17', 'relfdbk'),  # URL exists but not online https://trec.nist.gov/results/trec17/08relfdbk.input.html
    ('trec14', 'spam'), # runids do not match with names of the inputs  
    ('trec13', 'HARD'),  
    ('trec11', 'video'), # dead URL  
    ('trec11', 'xlingual'),   
    ('trec11', 'interactive'),   
    ('trec11', 'video'),   
    ('trec10', 'interactive'),   
    ('trec10', 'video'),   
    ('trec9', 'query'),   
    ('trec9', 'interactive'),   
    ('trec8', 'interactive'),   
    ('trec7', 'interactive'),  # *.docs and *.search exist
    ('trec6', 'filtering'),  
    ('trec6', 'interactive'),  # *.docs and *.search exist
    ('trec5', 'interactive'),
    ('trec4', 'filtering'),
]

# no proceedings available
no_proceedings = [
    ('trec-covid', 'round5'),
    ('trec-covid', 'round4'),
    ('trec-covid', 'round3'),
    ('trec-covid', 'round2'),
    ('trec-covid', 'round1'),
    ('trec4', 'filtering'),
    ('trec1', 'adhoc'),
    ('trec1', 'routing'),
]

# no runs page in the browser
no_runs = [
    ('trec6', 'vlc'),
    ('trec4', 'filtering'),
    ('trec1', 'adhoc'),
    ('trec1', 'routing'),
]

# no participants page in the browser
no_participants = [
    ('trec6', 'vlc'),
    ('trec4', 'filtering'),
    ('trec1', 'adhoc'),
    ('trec1', 'routing'),
]


results_url = 'https://trec.nist.gov/results'


def trec_year(trec_name):
    if trec_name == 'trec-covid':
        return 2020
    iteration = re.findall(r'\d+', trec_name)
    return 1991 + int(iteration[0])


def parse_line(fields, _type='runs'):
    for i in range(len(fields)):
        # some entries in runs_table files have more than the typical 18 fields (trec24 to trec29)
        if _type == 'runs' and i < len(field_names_runs):
            yield field_names_runs[i], fields[i] 
        if _type == 'participants':
            yield field_names_participants[i], fields[i] 
        if _type in ['covid-runs', 'covid-participants']:
            yield field_names_covid[i], fields[i] 


def metadata_line(fields, _type='runs'):
    return dict(parse_line(fields, _type=_type))


def     table_list(f_path, _type='runs'):
    data = []
    with open(f_path, encoding='utf8', errors='ignore') as f_in:
        lines = f_in.readlines()
        for line in lines:
            if line[0] == '#':
                continue
            else:
                fields = line.split(':')
                if any(d in fields[0] for d in ['DROPOUT', 'dropout', 'DROP-OUT']):
                    continue 
                if _type == 'participants':
                    fields = fields[:14] 
                line = metadata_line(fields, _type=_type)
                if line.get('task') == 'registration':
                    continue
                if line.get('track') not in no_tracks:
                    data.append(line) 
    return data


def rename_track_identifier(item):
    if item['trec'] == 'trec28':
        if item['track'] == 'converse':
            item['track'] = 'cast'
    if item['trec'] == 'trec12':
        if item['track'] == 'genome':
            item['track'] = 'genomics'
    if item['trec'] == 'trec6':
        if item['track'] == 'high-prec':
            item['track'] = 'hp'
    return item 


def adjust_task_field(item):
    if item['trec'] == 'trec7' and item['track'] == 'xlingual':
        item['task'] = item['md5']
    if item['trec'] in ['trec25', 'trec24'] and item['track'] == 'recall':
        item_task  = item['type'] 
        item_type = item['task']
        item['task'] = item_task
        item['type'] = item_type
    if item['trec'] in ['trec23', 'trec22'] and item['track'] == 'session':
        item_task = item['of_3']
        item_task = item_task.split('-')[0]
        item['task'] = item_task
    return item


def parse_description(item):
    if item['trec'] == 'trec32':
        if item['track'] == 'tot':
            desc = '\n'.join([item['description'], item['of_1']])
            item['description'] = desc.strip()
        if item['track'] == 'product':
            item['description'] = item['of_4']
    if item['trec'] in ['trec32', 'trec31', 'trec30'] and item['track'] == 'trials':
        if len(item['description']) == 0:
            item['description'] = item['of_4']
    if item['trec'] in ['trec29', 'trec28'] and item['track'] == 'pm':
        if len(item['description']) == 0:
            item['description'] = item['of_4']
    if item['trec'] == 'trec12':
        item['description'] = item['of_5']
    if item['trec'] == 'trec11' and item['track'] != 'filtering':
        item['description'] = item['of_5']
    if item['trec'] == 'trec10':
        item['description'] = item['of_4']
    if item['year'] < 1998:
        item['description'] = None
    if item.get('description'): 
        item['description'] = urllib.parse.unquote(item['description'])
        item['description'] = re.sub(r'[^\x00-\x7F]+','', item['description'])
        item['description'] = item['description'].replace('](', '] (') # otherwise, we have problems with the markdown syntax
    return item


def check_md5(item):
    md5 = item.get('md5')
    md5_regex = r'([a-fA-F\d]{32})'
    if md5:
        if len(re.findall(md5_regex, md5)) != 1:
            item['md5'] = None
    return item


def add_implementation_and_hardware(item):
    if item['trec'] == 'trec32':
        if item['track'] == 'atomic':
            part_one = urllib.parse.unquote(item['of_2'])
            part_two = urllib.parse.unquote(item['of_3'])
            part_three = urllib.parse.unquote(item['of_4'])
            if part_one != part_two != part_three:
                item['hardware'] = '\n'.join([
                    '_(Indexing)_ {}'.format(part_one), 
                    '_(Training)_ {}'.format(part_two), 
                    '_(Ranking)_ {}'.format(part_three), 
                    ])
        if item['track'] in ['neuclir', 'ikat']:
            item['hardware'] = urllib.parse.unquote(item['merge'])
            if item['hardware'] in ['Did not compute, sorry', 'Did not track', 'unk', 'unknown']:
                item['hardware'] = None
        if item['track'] in ['trials', 'product']:
            item['hardware'] = urllib.parse.unquote(item['of_3'])
            if item['hardware'] in ['N/A', 'NA.']:
                item['hardware'] = None
    return item

## TREC 33 TO HERE

def make_input(item):
    # common input
    input = '.'.join(['input', item['runid'], 'gz'])
    
    # TREC-30 input
    if item['trec'] == 'trec30':
        if item['track'] == 'podcast':
            if item['task'] == 'summarization':
                input = '.'.join(['input', item['runid'], 'tgz'])

    # TREC-29 input            
    if item['trec'] == 'trec29':
        if item['track'] == 'fair':
            input = '.'.join(['input', item['runid'], 'gz'])
        if item['track'] == 'podcast':
            if item['task'] == 'summarization':
                input = '.'.join(['input', item['runid'], 'tgz'])
    
    # TREC-26 input
    if item['trec'] == 'trec26':
        if item['track'] in ['rts', 'task', 'domain']:
            input = '.'.join([item['runid'], 'gz'])
    
    # TREC-25 input
    if item['trec'] == 'trec25':
        if item['track'] in ['task', 'domain', 'realtime', 'qa']:
            input = '.'.join([item['runid'], 'gz'])
        if item['track'] == 'qa':
            input = '.'.join([item['runid'], 'txt'])
    
    # TREC-24 input
    if item['trec'] == 'trec24':
        if item['track'] in ['microblog', 'task', 'domain']:
            input = '.'.join([item['runid'], 'gz'])
    
    # TREC-23 input
    if item['trec'] == 'trec23':
        if item['track'] in ['context', 'microblog', 'federated', 'tempsumm']:
            input = '.'.join([item['runid'], 'gz'])
        if item['track'] == 'kba':
            input = '.'.join([item['pid'], 'tar', 'gz'])
        if item['track'] == 'session':
            _input = '.'.join([item['runid'], 'gz'])
            input = '-'.join(['input', _input])
    
    # TREC-22 input
    if item['trec'] == 'trec22':
        if item['track'] in ['context', 'federated']:
            input = '.'.join([item['runid'], 'gz'])
        if item['track'] == 'kba':
            input = '.'.join([item['pid'], 'tar'])
        if item['track'] == 'session':
            _input = '.'.join([item['runid'], 'gz'])
            input = '-'.join(['input', _input])
    
    # TREC-21 input
    if item['trec'] == 'trec21': 
        if item['track'] == 'context':
            input = '.'.join([item['runid'], 'xml', 'gz'])
    
    # TREC-19 input
    if item['trec'] == 'trec19': 
        if item['track'] == 'web':
            if item['task'] == 'spam':
                input = '.'.join([item['runid'], 'bz2'])
    
    return input


def make_input_url(item, input):
    # common input_url
    input_url = '/'.join([results_url, item['trec'], item['track'], input])

    # TREC-COVID
    if item['trec'] == 'trec-covid':
        if item['track'] in ['round4', 'round5']:
            input = '.'.join([item['runid'], 'gz'])
            input_url = '/'.join(['https://ir.nist.gov/trec-covid/archive', item['track'], input])
        else:
            input_url = '/'.join(['https://ir.nist.gov/trec-covid/archive', item['track'], item['runid']])

    # TREC-28 input_url 
    if item['trec'] == 'trec28':
        if item['track'] == 'decisions':
            input_url = '/'.join([results_url, item['trec'], 'decision', input])

    # TREC-24 input_url         
    if item['trec'] == 'trec24':
        if item['track'] == 'qa':
            if item['runid'] == 'system7':
                input_url = 'https://trec.nist.gov/results/trec24/qa/ADAPT.DCU-system7'
            if item['runid'] == 'CMUOAQA':
                input_url = 'https://trec.nist.gov/results/trec24/qa/CMUOAQA-CarnegieMellonUniversityOAQAteam'
            if item['runid'] == 'dfkiqa':
                input_url = 'https://trec.nist.gov/results/trec24/qa/DFKI-dfkiqa'
            if item['runid'] == 'ecnucs':
                input_url = 'https://trec.nist.gov/results/trec24/qa/EastChinaNormalUniversity-ecnucs'            
            if item['runid'] == 'ECNU_ICA_2':
                input_url = 'https://trec.nist.gov/results/trec24/qa/ECNU-ECNU_ICA_2'
            if item['runid'] == 'Out-of-mEmory':
                input_url = 'https://trec.nist.gov/results/trec24/qa/emory-Out-of-mEmory'
            if item['runid'] == 'HIT_SCIR_QA_Grp':
                input_url = 'https://trec.nist.gov/results/trec24/qa/harbininstituteoftechnology-HIT_SCIR_QA_Grp'
            if item['runid'] == 'NUDTMDP1':
                input_url = 'https://trec.nist.gov/results/trec24/qa/MassiveDataProcessingLab-NUDTMDP1'
            if item['runid'] == 'NUDTMDP2':
                input_url = 'https://trec.nist.gov/results/trec24/qa/MassiveDataProcessingLab-NUDTMDP2'
            if item['runid'] == 'NUDTMDP3':
                input_url = 'https://trec.nist.gov/results/trec24/qa/MassiveDataProcessingLab-NUDTMDP3'
            if item['runid'] == 'QU1':
                input_url = 'https://trec.nist.gov/results/trec24/qa/QatarUniversity-QU1'
            if item['runid'] == 'system2':
                input_url = 'https://trec.nist.gov/results/trec24/qa/RMIT-system2'
            if item['runid'] == 'RMIT1':
                input_url = 'https://trec.nist.gov/results/trec24/qa/RMIT-RMIT1'
            if item['runid'] == 'RMIT2':
                input_url = 'https://trec.nist.gov/results/trec24/qa/RMIT-RMIT2'
            if item['runid'] == 'RMIT3':
                input_url = 'https://trec.nist.gov/results/trec24/qa/RMIT-RMIT3'
            if item['runid'] == 'SantaClaraUniversity':
                input_url = 'https://trec.nist.gov/results/trec24/qa/SCU-SantaClaraUniversity'
            if item['runid'] == 'CLIP1':
                input_url = 'https://trec.nist.gov/results/trec24/qa/UniversityofMaryland-CLIP1'
            if item['runid'] == 'CLIP2':
                input_url = 'https://trec.nist.gov/results/trec24/qa/UniversityofMaryland-CLIP2'
            if item['runid'] == 'CLIP3':
                input_url = 'https://trec.nist.gov/results/trec24/qa/UniversityofMaryland-CLIP3'
            if item['runid'] == 'system4':
                input_url = 'https://trec.nist.gov/results/trec24/qa/uwaterlooclarke-system4'
            if item['runid'] == 'Exp1':
                input_url = 'https://trec.nist.gov/results/trec24/qa/Yahoo-Exp1'

    # TREC-20 input_url         
    if item['trec'] == 'trec20':
        if item['track'] == 'entity':
            if item['task'] != 'ref':
                input_url = None    
    
    # TREC-16 input_url 
    if item['trec'] == 'trec16':
        if item['track'] == 'spam':
            if item['task'] == 'filter':
                input_url = None

    # TREC-15 input_url 
    if item['trec'] == 'trec15':
        if item['track'] == 'spam':
            if item['task'] == 'filter':
                input_url = None
        if item['track'] == 'blog':
            if item['task'] == 'open_task':
                input_url = None    
    
    # TREC-12 input_url 
    if item['trec'] == 'trec12':
        if item['track'] in ['genomics', 'hard', 'qa', 'novelty', 'qa', 'web']:
            input = '.'.join(['input', item['runid']])
        input_url = '/'.join([results_url, item['trec'], item['track'], 'inputs', input])
    
    # TREC-11 input_url 
    if item['trec'] == 'trec11':
        if item['track'] in ['filtering', 'novelty', 'qa', 'web']:
            input_url = '/'.join([results_url, item['trec'], item['track'], 'inputs', input])
    
    # TREC-10 input_url 
    if item['trec'] == 'trec10':
        if item['track'] in ['xlingual']:
            input_url = '/'.join([results_url, item['trec'], 'xling_inputs', input])
    
    # TREC-8 input_url 
    if item['trec'] == 'trec8':
        url_part = '.'.join([item['trec'], 'results', 'input'])
        if item['track'] == 'adhoc':
            input_url = '/'.join([results_url, item['trec'], url_part, item['track'], input])
        else:
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], input])
        if item['track'] == 'query':
            input_url = 'https://trec.nist.gov/results/trec8/trec8.results.input/tracks/query/query_runs.tar.gz'
        if item['track'] == 'web':
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', 'smweb', input])
    
    # TREC-7 input_url 
    if item['trec'] == 'trec7':
        url_part = '.'.join([item['trec'], 'results', 'input'])
        if item['track'] == 'adhoc':
            input_url = '/'.join([results_url, item['trec'], url_part, item['track'], input])
        else:
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], input])
        if item['track'] == 'hp':
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', 'high_prec', input])
        if item['runid'] in xligualalt_special_url:
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', 'xligualalt', input])
        if item['track'] == 'xlingual':
            if item['task'].strip() == 'EF':
                input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], 'ef', input])
            if item['task'].strip() == 'EFGI':
                input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], 'efgi', input])
            else: 
                input_url = None
    
    # TREC-6 input_url 
    if item['trec'] == 'trec6':
        url_part = '.'.join([item['trec'], 'results', 'input'])
        if item['track'] in ['adhoc', 'routing']:
            category = 'Category' + item['task'].upper()
            input_url = '/'.join([results_url, item['trec'], url_part, item['track'], category, input])
        else:
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], input])
        if item['track'] == 'clir':
            target_lang = item['task'].split('-')[1].replace('(Trans)', '').lower()
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], target_lang, input])
        if item['track'] == 'hp':
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', 'high_prec', input])
    
    # TREC-5 input_url 
    if item['trec'] == 'trec5':
        url_part = '.'.join([item['trec'], 'results', 'input'])
        if item['track'] in ['adhoc', 'routing']:
            category = 'Category' + item['task'].upper()
            input_url = '/'.join([results_url, item['trec'], url_part, item['track'], category, input])
        else:
            input_url = '/'.join([results_url, item['trec'], url_part, 'tracks', item['track'], input])
    
    # TREC-4 input_url 
    if item['trec'] == 'trec4':
        input = '.'.join(['input', item['runid'], 'Z'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.input'])
            category = ''.join(['Category', item['task']])
            input_url = '/'.join([results_url, item['trec'], _p, item['track'], category, input])
        if item['track'] in ['confusion', 'dbmerge']:
            _p = ''.join([item['trec'], '.results.input'])
            input_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], input])
        if item['track'] in ['interactive']:
            input = '.'.join(['input', item['runid']])
            _p = ''.join([item['trec'], '.results.input'])
            input_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], 'TASK1', input])
        if item['track'] in ['spanish']:
            _p = ''.join([item['trec'], '.results.input'])
            input_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], item['task'], input])
    
    # TREC-3 input_url 
    # TREC-2 input_url 
    if item['trec'] in ['trec3', 'trec2']:
        input = '.'.join(['input', item['runid'], 'gz'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.input'])
            input_url = '/'.join([results_url, item['trec'], _p, item['track'], input])
    
    return input_url


def make_summary(item):
    # common summary
    summary = '.'.join(['summary', item['runid']])

    # TREC-32 summaries
    if item['trec'] == 'trec32':
        if item['track'] == 'atomic':
            summary = f'summary.{item["runid"]}.eval'
        if item['track'] == 'deep':
            summary = f'treceval.{item["runid"]}.eval'
        if item['track'] == 'ikat':
            summary = {
                'Summary (doc ranking)': f'summary.{item["runid"]}.doc-eval',
                'Summary (PTKB ranking)': f'summary.{item["runid"]}.ptkb-eval'
            }
        if item['track'] == 'neuclir':
            summary = f'summary.{item["runid"]}.eval'
        if item['track'] == 'product':
            summary = f'{item["runid"]}.eval'
        if item['track'] == 'tot':
            summary = f'treceval.{item["runid"]}.eval'
        if item['track'] == 'trials':
            summary = {
                'Summary (trec_eval)': f'{item["runid"]}.treceval',
                'Summary (nDCG)': f'{item["runid"]}.ndcg-eval'
            }

    # TREC-31 summary
    if item['trec'] == 'trec31':
        if item['track'] == 'deep':
            if item['task'] == 'docs':
                summary = '.'.join(['summary', item['runid']])
            if item['task'] == 'passages':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', item['runid'], 'trec_eval']),
                    'Summary (ndcg)': '.'.join(['summary', item['runid'], 'ndcg'])
                }
        if item['track'] == 'neuclir':
            summary = '.'.join(['summary', item['runid'], 'trec_eval'])
        if item['track'] == 'cast':              
            summary = {
                'Summary (strict)': '.'.join(['summary', item['runid'], 'strict']),
                'Summary (lenient)': '.'.join(['summary', item['runid'], 'lenient'])
            }
        if item['track'] == 'fair':                         
            if item['task'] == 'coordinators': 
                summary = '.'.join(['summary', item['runid'], 'coord', 'tsv'])
            if item['task'] == 'editors': 
                summary = '.'.join(['summary', item['runid'], 'editors', 'tsv'])
        if item['track'] == 'crisis':                       
            summary = {
                'Summary (auto)': '.'.join(['summary', item['runid'], 'auto', 'csv']),
                'Summary (manual)': '.'.join(['summary', item['runid'], 'manual', 'tar', 'gz'])
            }

    # TREC-30 summary
    if item['trec'] == 'trec30':
        if item['track'] == 'incident':
            summary = '.'.join(['summary', item['runid'], 'html'])
        if item['track'] == 'deep':
            if item['task'] == 'passages':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                    'Summary (passages-eval)': '.'.join(['summary', 'passages-eval', item['runid']])
                }
            else:
                summary = '.'.join(['summary', 'treceval', item['runid']])
        if item['track'] == 'podcast':
            summary = '.'.join(['summary', 'QD', item['runid']])
            summary = {
                'Summary (QD)': '.'.join(['summary', 'QD', item['runid']]),
                'Summary (QE)': '.'.join(['summary', 'QE', item['runid']]),
                'Summary (QR)': '.'.join(['summary', 'QR', item['runid']]),
                'Summary (QS)': '.'.join(['summary', 'QS', item['runid']])
            }

    # TREC-29 summary
    if item['trec'] == 'trec29':
        if item['track'] == 'deep':
            if item['task'] == 'passages':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                    'Summary (passages-eval)': '.'.join(['summary', 'passages-eval', item['runid']])
                }
            else:
                summary = '.'.join(['summary', 'treceval', item['runid']])
        if item['track'] == 'misinfo':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'cast':   
            summary = '.'.join(['summary', 'treceval', item['runid']])
        if item['track'] == 'pm':   
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']]),
                'Summary (evidence-eval)': '.'.join(['summary', 'evidence-eval', item['runid']])
            }
        if item['track'] == 'podcast': 
            if item['task'] == 'summarization':
                summary = {
                    'Summary (manual)': '.'.join(['summary', 'manual', item['runid']]),
                    'Summary (rouge)': '.'.join(['summary', 'rouge', item['runid'], 'tgz'])
                }
            else:
                summary = '.'.join(['summary', 'treceval', item['runid']]) # treceval, manual, rouge 
    
    # TREC-28 summary
    if item['trec'] == 'trec28':
        if item['track'] == 'deep':
            if item['task'] == 'passages':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                    'Summary (passages-eval)': '.'.join(['summary', 'passages-eval', item['runid']])
                }
            else:
                summary = '.'.join(['summary', 'treceval', item['runid']]) # treceval, passages-eval
        if item['track'] == 'pm':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] in ['cast', 'converse']:
            summary = '.'.join(['summary', 'treceval', item['runid']])
            item['track'] = 'cast'
        if item['track'] == 'fair':
            summary = {
                'Summary (level)': '.'.join(['summary', 'level', item['runid']]),
                'Summary (hindex)': '.'.join(['summary', 'hindex', item['runid']])
            }
        if item['track'] == 'incident':
            summary = '.'.join(['summary', item['runid'], 'results', 'overall', 'txt']) # overall, perevent, pertopic
            summary = {
                'Summary (overall)': '.'.join(['summary', item['runid'], 'results', 'overall', 'txt']),
                'Summary (perevent)': '.'.join(['summary', item['runid'], 'results', 'perevent', 'txt']),
                'Summary (pertopic)': '.'.join(['summary', item['runid'], 'results', 'pertopic', 'txt'])
            }

    # TREC-27 summary
    if item['trec'] == 'trec27':
        if item['track'] == 'pm':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] == 'core':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'car':
            summary = 'http://trec-car.cs.unh.edu/results/'
    
    if item['trec'] == 'trec26':
        if item['track'] == 'core':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'pm':
            if item['task'] == 'abstracts':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                    'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
                }
            if item['task'] == 'trials':
                summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'rts':
            if item['task'] == 'a':
                summary = {
                    'Summary (Batch)': ''.join(['summary-batchA-', item['runid'], '.txt']),
                    'Summary (Mobile)': ''.join(['summary-mobileA-', item['runid'], '.txt'])
                }
            if item['task'] == 'b':
                summary = ''.join(['summary-batchB-', item['runid'], '.txt'])
        if item['track'] == 'task':
            summary = ''.join(['summary-', item['runid'], '.txt'])
    
    # TREC-25 summary
    if item['trec'] == 'trec25':
        if item['track'] == 'clinical':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] == 'context':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] in ['rts', 'realtime']:
            if item['task'] == 'a':
                summary = {
                    'Summary (Batch)': ''.join(['summary-batchA-', item['runid'], '.txt']),
                    'Summary (Mobile)': ''.join(['summary-mobileA-', item['runid'], '.txt'])
                }
            if item['task'] == 'b':
                summary = ''.join(['summary-batchB-', item['runid'], '.txt'])
        if item['track'] == 'task':
            summary = ''.join(['summary-', item['runid'], '.txt'])

    # TREC-24 summary
    if item['trec'] == 'trec24':
        if item['track'] == 'clinical':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] == 'context':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'microblog':
            summary = ''.join(['summary-', item['task'], '-', item['runid'], '.txt'])
        if item['track'] == 'tempsumm':
            summary = '.'.join([item['pid'], 'all', 'tsv'])
        if item['track'] == 'task':
            summary = ''.join(['summary-', item['runid'], '.txt'])
        if item['track'] == 'domain':
            summary = ''.join(['summary-', item['task'], '-', item['runid'], '.txt'])

    # TREC-23 summary
    if item['trec'] == 'trec23':
        if item['track'] == 'clinical':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] == 'microblog':
            summary = ''.join(['summary-', item['task'], '-', item['runid'], '.txt'])
        if item['track'] == 'web':
            if item['task'] == 'adhoc':
                summary = {
                    'Summary (std-gd)': '.'.join(['summary', 'std-gd', item['runid']]),
                    'Summary (std-nd)': '.'.join(['summary', 'std-nd', item['runid']])
                } 
            if item['task'] == 'risk':
                summary = {
                    'Summary (std-gd)': '.'.join(['summary', 'std-gd', item['runid']]),
                    'Summary (std-nd)': '.'.join(['summary', 'std-nd', item['runid']]),
                    'Summary (risk-rm-a0-gd)': '.'.join(['summary', 'risk-rm-a0-gd', item['runid']]),
                    'Summary (risk-rm-a0-nd)': '.'.join(['summary', 'risk-rm-a0-nd', item['runid']]),
                    'Summary (risk-rm-a5-gd)': '.'.join(['summary', 'risk-rm-a5-gd', item['runid']]),
                    'Summary (risk-rm-a5-nd)': '.'.join(['summary', 'risk-rm-a5-nd', item['runid']]),
                    'Summary (risk-terrier-a0-gd)': '.'.join(['summary', 'risk-terrier-a0-gd', item['runid']]),
                    'Summary (risk-terrier-a0-nd)': '.'.join(['summary', 'risk-terrier-a0-nd', item['runid']]),
                    'Summary (risk-terrier-a5-gd)': '.'.join(['summary', 'risk-terrier-a5-gd', item['runid']]),
                    'Summary (risk-terrier-a5-nd)': '.'.join(['summary', 'risk-terrier-a5-nd', item['runid']])
                } 
        if item['track'] == 'tempsumm':
            summary = '.'.join([item['runid'], 'tsv'])     
        if item['track'] == 'session':
            _runid ='.'.join(item['runid'].split('.')[:-1])
            summary = ''.join(['summary-', _runid, '.txt'])                   

    # TREC-22 summary
    if item['trec'] == 'trec22':
        if item['track'] == 'web':
            summary = {
                    'Summary (std-gd)': '.'.join(['summary', 'std-gd', item['runid']]),
                    'Summary (std-nd)': '.'.join(['summary', 'std-nd', item['runid']]),
                    'Summary (risk-risk-a0-gd)': '.'.join(['summary', 'risk-a0-gd', item['runid']]),
                    'Summary (risk-risk-a0-nd)': '.'.join(['summary', 'risk-a0-nd', item['runid']]),
                    'Summary (risk-risk-a1-gd)': '.'.join(['summary', 'risk-a1-gd', item['runid']]),
                    'Summary (risk-risk-a1-nd)': '.'.join(['summary', 'risk-a1-nd', item['runid']]),
                    'Summary (risk-risk-a5-nd)': '.'.join(['summary', 'risk-a5-nd', item['runid']]),
                    'Summary (risk-risk-a5-nd)': '.'.join(['summary', 'risk-a5-nd', item['runid']]),
                    'Summary (risk-risk-a10-gd)': '.'.join(['summary', 'risk-a10-gd', item['runid']]),
                    'Summary (risk-risk-a10-nd)': '.'.join(['summary', 'risk-a10-nd', item['runid']]),
                } 
        if item['track'] == 'federated':
            summary = '.'.join([item['runid'], 'pdf'])
        if item['track'] == 'session':
            summary = ''.join(['summary-', '.'.join(item['runid'].split('.')[:-1]), '.txt']) 

    # TREC-21 summary
    if item['trec'] == 'trec21':
        if item['track'] == 'microblog':
            if item['task'] == 'adhoc':
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'treceval', item['runid']]),
                    'Summary (roc)': '.'.join(['summary', 'roc', item['runid']])
                }  
            if item['task'] == 'filtering':
                summary = '.'.join(['summary', 'filtereval', item['runid']]) 
        if item['track'] == 'web':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (ndeval)': '.'.join(['summary', 'ndeval', item['runid']]),
                'Summary (gdeval)': '.'.join(['summary', 'gdeval', item['runid']])
            }  
        if item['track'] == 'medical':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (sample-eval)': '.'.join(['summary', 'sample-eval', item['runid']])
            }
        if item['track'] == 'session':
            summary = '.'.join(['summary', item['runid'].split('.')[0]]) 

    # TREC-20 summary
    if item['trec'] == 'trec20':
        if item['track'] == 'microblog':
            summary = {
                'Summary (highrel)': '.'.join(['summary', 'highrel', item['runid']]),
                'Summary (allrel)': '.'.join(['summary', 'allrel', item['runid']])
            } 
        if item['track'] == 'web':
            summary = {
                'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                'Summary (ndeval)': '.'.join(['summary', 'ndeval', item['runid']]),
                'Summary (gdeval)': '.'.join(['summary', 'gdeval', item['runid']])
            }  
        if item['track'] == 'medical':
            summary = '.'.join(['summary', 'trec_eval', item['runid']])
        if item['track'] == 'session':
            _runid = '.'.join(item['runid'].split('.')[:-1])
            summary = {
                'Summary (allsubtopics)': '.'.join(['summary', 'allsubtopics', _runid]),
                'Summary (lastquerysubtopics)': '.'.join(['summary', 'lastquerysubtopics', _runid])
            }

    # TREC-19 summary
    if item['trec'] == 'trec19':
        if item['track'] == 'blog':
            if item['task'] == 'feed':
                summary = {
                    'Summary (first)': '.'.join(['summary', 'first', item['runid'], 'gz']),
                    'Summary (second)': '.'.join(['summary', 'second', item['runid'], 'gz'])
                }
            if item['task'] == 'blfeed':
                summary = {
                    'Summary (baseline)': '.'.join(['summary', 'baseline', item['runid'], 'gz']),
                    'Summary (first)': '.'.join(['summary', 'first', item['runid'], 'gz']),
                    'Summary (second)': '.'.join(['summary', 'second', item['runid'], 'gz'])
                }
            if item['task'] == 'topstories':
                summary = {
                    'Summary (business)': '.'.join(['summary', 'business', item['runid'], 'gz']),
                    'Summary (scitech)': '.'.join(['summary', 'fiscitechrst', item['runid'], 'gz']),
                    'Summary (sport)': '.'.join(['summary', 'sport', item['runid'], 'gz']),
                    'Summary (us)': '.'.join(['summary', 'us', item['runid'], 'gz']),
                    'Summary (world)': '.'.join(['summary', 'world', item['runid'], 'gz'])
                }
            if item['task'] == 'newsblogpost':
                summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'web':
            if item['task'] in ['adhoc', 'diversity']:
                summary = {
                    'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
                    'Summary (ndeval)': '.'.join(['summary', 'ndeval', item['runid']]),
                    'Summary (gdeval)': '.'.join(['summary', 'gdeval', item['runid']])
                }  
            if item['task'] == 'spam':
                summary = '.'.join(['summary', 'spam', item['runid'], 'gz'])
        if item['track'] == 'session': 
            summary = '.'.join(['summary', item['pid'], 'tgz']) 
        if item['track'] == 'entity':
            summary = '.'.join(['summary', item['runid'], 'gz']) 

    # TREC-18 summary
    if item['trec'] == 'trec18':
        if item['track'] == 'relfdbk':    
            summary = '.'.join(['summary', 'eval', item['runid'], 'gz'])
        if item['track'] == 'chemical':   
            if item['task'] == 'techsurv':
                summary = '.'.join(['summary', 'eval', item['runid'], 'gz'])
            if item['task'] == 'priorart':
                summary = {
                    'Summary (full)': '.'.join(['summary', 'full', item['runid'], 'gz']),
                    'Summary (small)': '.'.join(['summary', 'small', item['runid'], 'gz'])
                }  
            if item['task'] == 'priorart_sm':
                summary = '.'.join(['summary', 'small', item['runid'], 'gz'])
        if item['track'] == 'legal':  
            if item['task'] == 'batch':
                summary = {
                    'Summary (eval)': '.'.join(['summary', 'eval', item['runid'], 'gz']),
                    'Summary (evalH)': '.'.join(['summary', 'evalH', item['runid'], 'gz'])
                }  
        if item['track'] == 'web':
            if item['task'] == 'adhoc':
                summary = '.'.join(['summary', 'adhoc', item['pid'], 'tgz'])
            if item['task'] == 'diversity':    
                summary = '.'.join(['summary', 'diversity', item['runid'], 'gz'])
        if item['track'] == 'million-query':
            summary = '.'.join(['summary', item['pid'], 'tgz'])
        if item['track'] == 'blog':
            if item['task'] == 'topstories':
                summary = {
                    'Summary (headline)': '.'.join(['summary', 'headline', item['runid'], 'gz']),
                    'Summary (blogpost)': '.'.join(['summary', 'blogpost', item['runid'], 'gz'])
                }  
            if item['task'] == 'feed':
                summary = {
                    'Summary (none)': '.'.join(['summary', 'none', item['runid'], 'gz']),
                    'Summary (first)': '.'.join(['summary', 'first', item['runid'], 'gz']),
                    'Summary (second)': '.'.join(['summary', 'second', item['runid'], 'gz'])
                }  
        if item['track'] == 'entity':
            summary = '.'.join(['summary', 'eval', item['runid'], 'gz'])

    # TREC-17 summary
    if item['trec'] == 'trec17':
        if item['track'] == 'blog':
            if item['task'] in ['baseline', 'opinion']:
                summary = {
                    'Summary (opinion)': '.'.join(['summary', 'opinion', item['runid'], 'gz']),
                    'Summary (topicrel)': '.'.join(['summary', 'topicrel', item['runid'], 'gz'])
                }  
            if item['task'] == 'polarity':
                summary = {
                    'Summary (negative)': '.'.join(['summary', 'negative', item['runid'], 'gz']),
                    'Summary (positive)': '.'.join(['summary', 'positive', item['runid'], 'gz'])
                }  
        if item['track'] == 'feed':
            summary = '.'.join(['summary', 'feed', item['runid'], 'gz'])
        if item['track'] == 'million-query':
            summary = {
                'Summary (mtc)': '.'.join(['summary', 'mtc', item['runid'], 'gz']),
                'Summary (statAP)': '.'.join(['summary', 'statAP', item['runid'], 'gz'])
            }  
        if item['track'] == 'enterprise':
            if item['task'] == 'document':
                summary = '.'.join(['summary', 'document', item['runid'], 'gz'])
            if item['task'] == 'expert':
                summary = '.'.join(['summary', 'expert', item['runid'], 'gz'])
        if item['track'] == 'legal':
            if item['task'] == 'adhoc':
                summary = {
                    'Summary (adhoc)': '.'.join(['summary', 'adhoc', item['runid'], 'gz']),
                    'Summary (adhocH)': '.'.join(['summary', 'adhocH', item['runid'], 'gz'])
                } 
            if item['task'] == 'feedback':
                summary = {
                    'Summary (resid)': '.'.join(['summary', 'resid', item['runid'], 'gz']),
                    'Summary (residH)': '.'.join(['summary', 'residH', item['runid'], 'gz'])
                } 
        if item['track'] == 'relfdbk':
            summary = {
                'Summary (mtc)': '.'.join(['summary', 'mtc', item['runid'], 'gz']),
                'Summary (statAP)': '.'.join(['summary', 'statAP', item['runid'], 'gz']),
                'Summary (top10)': '.'.join(['summary', 'top10', item['runid'], 'gz'])
            }  

    # TREC-16 summary
    if item['trec'] == 'trec16':
        if item['track'] == 'blog':
            if item['task'] in ['opinion', 'baseline']:
                summary = {
                    'Summary (topicrel)': '.'.join(['summary', 'topicrel', item['runid'], 'gz']),
                    'Summary (opinion)': '.'.join(['summary', 'opinion', item['runid'], 'gz'])
                } 
            if item['task'] == 'feed':
                summary = '.'.join(['summary', 'feed', item['runid'], 'gz'])
            if item['task'] == 'polarity':
                summary = '.'.join(['summary', 'polarity', item['runid'], 'gz'])
        if item['track'] == 'enterprise':
            if item['task'] == 'document':
                summary = {
                    'Summary (document)': '.'.join(['summary', 'document', item['runid'], 'gz']),
                    'Summary (doc-promotion)': '.'.join(['summary', 'doc-promotion', item['runid'], 'gz']),
                    'Summary (doc-residual)': '.'.join(['summary', 'doc-residual', item['runid'], 'gz'])
                } 
            if item['task'] == 'expert':
                summary = '.'.join(['summary', 'experts', item['runid'], 'gz'])
        if item['track'] == 'qa':
            if item['task'] in ['main', 'ciqa_baseline', 'ciqa_final']:
                summary = '.'.join(['summary', item['runid'], 'tar', 'gz'])
        if item['track'] == 'spam':
            summary = '.'.join([item['pid'], 'tgz'])
        if item['track'] in ['genomics', 'legal']:
            summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'million-query':
            summary = {
                'Summary (tb-topics)': '.'.join(['summary', 'tb-topics', item['runid'], 'gz']),
                'Summary (statMAP)': '.'.join(['summary', 'statMAP', item['runid'], 'gz'])
            } 

    # TREC-15 summary
    if item['trec'] == 'trec15':
        if item['track'] == 'terabyte':
            summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'spam':
            summary = '.'.join([item['pid'], 'tgz'])
        if item['track'] == 'enterprise':
            if item['task'] == 'discussion':
                summary = {
                    'Summary (rel_nonrel)': '.'.join(['summary', 'rel_nonrel', item['runid']]),
                    'Summary (rel_procon)': '.'.join(['summary', 'rel_procon', item['runid']])
                } 
            if item['task'] == 'expert':
                summary = {
                    'Summary (experts)': '.'.join(['summary', 'experts', item['runid']]),
                    'Summary (supported)': '.'.join(['summary', 'supported', item['runid']])
                } 
        if item['track'] == 'blog':
            if item['task'] == 'opinion':
                summary = {
                    'Summary (topicrel)': '.'.join(['summary', 'topicrel', item['runid'], 'gz']),
                    'Summary (opinion)': '.'.join(['summary', 'opinion', item['runid'], 'gz'])
                } 
        if item['track'] == 'qa':
            summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'legal':
            summary = {
                'Summary (trec-eval)': '.'.join(['summary', 'trec-eval', item['runid']]),
                'Summary (prec-at-B)': '.'.join(['summary', 'prec-at-B', item['runid']])
            } 

    # TREC-14 summary
    if item['trec'] == 'trec14':
        if item['track'] in ['enterprise', 'genomics', 'HARD', 'terabyte']:
            summary = '.'.join(['summary', item['runid'], 'gz'])
            if item['task'] == 'clarification':
                summary = '.'.join([item['runid'], 'responses', 'tgz'])
        if item['track'] == 'qa':
            if item['task'] == 'main':
                summary = '.'.join(['docrank', 'summary', item['runid'], 'gz'])
            if item['task'] == 'relationship':
                summary = '.'.join(['rel', 'summary', item['runid'], 'gz'])
        if item['track'] == 'robust':
            summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'spam':
            if item['pid'] == 'ibm.segal':
                summary = 'summary.621SPAM.tgz'
            if item['pid'] == 'cas-ict.wang':
                summary = 'summary.ICTSPAM.tgz'
            if item['pid'] == 'uparis-sud.aze':
                summary = 'summary.azeSPAM.tgz'
            if item['pid'] == 'merl.yerazunis':
                summary = 'summary.crmSPAM.tgz'
            if item['pid'] == 'dalhousieu.keselj':
                summary = 'summary.dalSPAM.tgz'
            if item['pid'] == 'jozef-stefan-inst.bratko':
                summary = 'summary.ijsSPAM.tgz'
            if item['pid'] == 'indianau.yang':
                summary = 'summary.indSPAM.tgz'
            if item['pid'] == 'beijingu.guo':
                summary = 'summary.kidSPAM.tgz'
            if item['pid'] == 'breyer.laird':
                summary = 'summary.lbSPAM.tgz'
            if item['pid'] == 'puc-rs.terra':
                summary = 'summary.pucSPAM.tgz'
            if item['pid'] == 'masseyu.meyer':
                summary = 'summary.tamSPAM.tgz'
            if item['pid'] == 'yorku.huang':
                summary = 'summary.yorSPAM.tgz'

    # TREC-13 summary
    if item['trec'] == 'trec13':
        if item['track'] in ['genomics', 'novelty', 'terabyte', 'qa', 'robust', 'web']:
            summary = '.'.join(['summary', item['runid'], 'gz'])

    # TREC-12 summary        
    if item['trec'] == 'trec12':
        if item['track'] in ['genomics', 'HARD', 'hard', 'novelty', 'qa', 'robust', 'web']:                       
            summary = '.'.join(['summary', item['runid']])
            summary = '/'.join(['summaries', summary])

    # TREC-11 summary
    if item['trec'] == 'trec11':
        if item['track'] in ['web', 'qa', 'novelty']:                       
            summary = '.'.join(['summary', item['runid'], 'gz'])
            summary = '/'.join(['summaries', summary])

    # TREC-10 summary
    if item['trec'] == 'trec10':
        if item['track'] in ['qa', 'xlingual', 'web']:
            summary = '.'.join(['summary', item['runid'], 'gz'])

    # TREC-9 summary
    if item['trec'] == 'trec9':
        if item['track'] in ['qa', 'xlingual', 'web', 'sdr']:
            summary = '.'.join(['summary', item['runid'], 'gz'])
    
    return summary


def make_summary_url(item, summary):
    # common summary_url 
    if type(summary) == dict:
        for k, v in summary.items():
            summary[k] = '/'.join([results_url, item['trec'], item['track'], v])
        summary_url = json.dumps(summary)
    elif summary:
        summary_url = '/'.join([results_url, item['trec'], item['track'], summary])

    # TREC-28 summary_url
    if (item['trec'], item['track']) == ('trec28', 'decisions'):
        summary = {
            'Summary (trec_eval)': '.'.join(['summary', 'trec_eval', item['runid']]),
            'Summary (extended)': '.'.join(['summary', 'extended', item['runid']])
        }
        for summ_key, summ in summary.items():
            summary[summ_key] = '/'.join([results_url, item['trec'], 'decision', summ])
        summary_url = json.dumps(summary)

    # TREC-20 summary_url
    if (item['trec'], item['track'], item['task']) == ('trec20', 'entity', 'reflod'):
        summary_url = None 

    # TREC-19 summary_url
    if (item['trec'], item['track']) == ('trec19', 'chemical'):
        summary_url = None # no public summary files on the website

    # TREC-18 summary_url
    if (item['trec'], item['track'], item['task']) == ('trec18', 'legal', 'interactive'):
        summary_url = None
    
    # TREC-17 summary_url
    if (item['trec'], item['track'], item['task']) == ('trec17', 'legal', 'interactive'):
        summary_url = None
    
    # TREC-15 summary_url
    if (item['trec'], item['track'], item['task']) == ('trec15', 'blog', 'open_task'):
        summary_url = None

    # TREC-11 summary_url
    if (item['trec'], item['track']) == ('trec11', 'xlingual'):
        summary_url = None # no public summary files on the website

    # TREC-10 summary_url
    if (item['trec'], item['track']) == ('trec10', 'xlingual'):
        summary_url = '/'.join([results_url, item['trec'], 'xling_summaries', summary])

    # TREC-8 summary_url
    if item['trec'] == 'trec8':
        summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'adhoc':
            _p = ''.join([item['trec'], '.results.summary'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] in ['xlingual', 'filtering', 'qa', 'sdr']:
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] == 'web':
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, 'smweb', summary])

    # TREC-7 summary_url
    if item['trec'] == 'trec7':
        summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] == 'adhoc':
            _p = ''.join([item['trec'], '.results.summary'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] in ['query', 'sdr']:
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] == 'hp':
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, 'high_prec', summary])
        if item['track'] == 'xlingual':
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            task = item['task'].lower()
            summary_url = '/'.join([results_url, item['trec'], _p, 'xlingual', task, summary])
        if item['track'] == 'filtering':
            _results_url = 'https://trec.nist.gov/results/trec7/trec7.results.summary/tracks/filtering/'
            summary = '.'.join(['summary', item['runid'], 'gz'])
            if item['runid'] in ['AntRout1', 'AntRout2']:
                summary = 'summary.AntRout1.AntRout2.gz'
            if item['runid'] in ['CLARITafF1a', 'CLARITafF1b']:
                summary = 'summary.CLARITafF1a.CLARITafF1b.gz'
            if item['runid'] in ['CLARITafF3a', 'CLARITafF3b']:
                summary = 'summary.CLARITafF3a.CLARITafF3b.gz '
            if item['runid'] in ['IAHKaf11', 'IAHKaf12']:
                summary = 'summary.IAHKaf11.IAHKaf12.gz'
            if item['runid'] in ['IAHKaf31', 'IAHKaf32']:
                summary = 'summary.IAHKaf31.IAHKaf32.gz'
            if item['runid'] in ['Mer7AGbF1', 'Mer7ARbF1']:
                summary = 'summary.Mer7AGbF1.Mer7ARbF1.gz'
            if item['runid'] in ['Mer7AGbF3', 'Mer7ARbF3']:
                summary = 'summary.Mer7AGbF3.Mer7ARbF3.gz'
            if item['runid'] in ['att98fr4', 'att98fr5']:
                summary = 'summary.att98fr4.att98fr5.gz'
            if item['runid'] in ['nttd7rt1', 'nttd7rt2']:
                summary = 'summary.nttd7rt1.nttd7rt2.gz'
            if item['runid'] in ['ok7ff12', 'ok7ff13']:
                summary = 'summary.ok7ff12.ok7ff13.gz'
            if item['runid'] in ['ok7ff32', 'ok7ff33']:
                summary = 'summary.ok7ff32.ok7ff33.gz'
            if item['runid'] in ['pirc8R1', 'pirc8R2']:
                summary = 'summary.pirc8R1.pirc8R2.gz'
            if item['runid'] == 'MerBF1':
                summary = 'summary.Mer7BF1.gz'
            if item['runid'] == 'MerBF3':
                summary = 'summary.Mer7BF3.gz'
            if item['runid'] == 'att98ft1':
                summary = None
            if item['runid'] == 'MerAGbR':
                summary = None
            if item['runid'] == 'INQ512':
                summary = None
            if item['runid'] == 'nttd7rk':
                summary = None
            if summary:
                summary_url = ''.join([_results_url, summary])
            else:
                summary_url = None

    # TREC-6 summary_url
    if item['trec'] == 'trec6':
        summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.summary'])
            category = ''.join(['Category', item['task']])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], category, summary])
        if item['track'] in ['chinese', 'nlp']:
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] == 'clir':
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            _task = item['task'].split('-')[-1].lower()
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], _task, summary])
        if item['track'] == 'hp':
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, 'high_prec', summary])

    # TREC-5 summary_url
    if item['trec'] == 'trec5':
        summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.summary'])
            category = ''.join(['Category', item['task']])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], category, summary])
        if item['track'] in ['chinese', 'Chinese', 'spanish', 'Spanish', 'nlp']:
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] == 'vlc':
            summary = '.'.join(['summary', 'submit', 'Z'])
            _p = ''.join([item['trec'], '.results.summary/tracks'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])
        if item['track'] == 'dbmerge':
            summary_url = None # no public summaries on the website

    # TREC-4 summary_url
    if item['trec'] == 'trec4':
        summary = '.'.join(['summary', item['runid'], 'Z'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.summary'])
            category = ''.join(['Category', item['task']])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], category, summary])
        if item['track'] in ['confusion', 'dbmerge']:
            _p = ''.join([item['trec'], '.results.summary'])
            summary_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], summary])
        if item['track'] == 'interactive':
            summary = '.'.join(['summary', item['runid']])
            _p = ''.join([item['trec'], '.results.summary'])
            summary_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], 'TASK1', summary])
        if item['track'] == 'spanish':
            if item['task'] == 'topics_26_50':
                _p = ''.join([item['trec'], '.results.summary'])
                summary_url = '/'.join([results_url, item['trec'], _p, 'tracks', item['track'], 'topics_26_50', summary])
            else:
                summary_url = None
    
    # TREC-3 summary_url
    # TREC-2 summary_url
    if item['trec'] in ['trec3', 'trec2']:
        summary = '.'.join(['summary', item['runid'], 'gz'])
        if item['track'] in ['adhoc', 'routing']:
            _p = ''.join([item['trec'], '.results.summary'])
            summary_url = '/'.join([results_url, item['trec'], _p, item['track'], summary])

    return summary_url


def make_appendix(item):
    # common appendix
    appendix = '.'.join([item['runid'], 'pdf'])

    if item['trec'] == 'trec33':
        appendix = f'{item["track"]}-appendix.html'

    # TREC-30 appendix
    if item['trec'] == 'trec30':
        if item['track'] == 'incident':
            appendix = '.'.join([item['runid'], 'html'])

    # TREC-27 appendix
    if item['trec'] == 'trec27':
        if item['track'] == 'incident':
            appendix = '.'.join([item['pid'], 'pdf'])

    # TREC-26 appendix
    if item['trec'] == 'trec26':
        if item['track'] == 'car':
            appendix = '.'.join(['car', 'pdf'])
        if item['track'] == 'domain':
            appendix = '.'.join(['domain', 'pdf'])
        if item['track'] == 'open':
            appendix = '.'.join(['trec-os-2017', 'pdf'])

    # TREC-25 appendix
    if item['trec'] == 'trec25':
        if item['track'] == 'recall':
            appendix = '.'.join(['recall', 'pdf'])
        if item['track'] == 'domain':
            appendix = '.'.join(['domain', 'pdf'])
        if item['track'] == 'domain':
            if item['pid'] == 'THKoeln-GESIS':
                appendix = '.'.join(['open-ssoar', 'pdf'])
            if item['pid'] == 'BJUT':
                appendix = '.'.join(['open-citeseer', 'pdf'])

    # TREC-24 appendix
    if item['trec'] == 'trec24':
        if item['track'] == 'recall':
            appendix = '.'.join(['recall', 'pdf'])
        if item['track'] == 'tempsumm':
            appendix = ''.join(['tempsumm-', item['task'], 'pdf'])

    # TREC-23 appendix
    if item['trec'] == 'trec23':
        if item['track'] =='session':
            runid = ''.join(item['runid'].split('.')[:-1])
            appendix = '.'.join([runid, 'pdf'])

    # TREC-22 appendix
    if item['trec'] == 'trec22':
        if item['track'] == 'crowd':
            appendix = '.'.join([item['runid'], 'result', 'pdf'])
        if item['track'] == 'tempsumm':
            appendix = 'TS13-{}-{}.pdf'.format(item['pid'], item['runid'])
        if item['track'] == 'session':
            runid = ''.join(item['runid'].split('.')[:-1])
            appendix = '.'.join([runid, 'pdf'])

    # TREC-21 appendix
    if item['trec'] == 'trec21':
        if item['track'] == 'crowd':
            appendix = '.'.join([item['runid'], 'result', 'pdf'])
        if item['track'] == 'session':
            runid = ''.join(item['runid'].split('.')[:-1])
            appendix = '.'.join([runid, 'pdf'])

    # TREC-20 appendix
    if item['trec'] == 'trec20':
        if item['track'] == 'medical':
            if item['type'] == 'automatic':
                appendix = '.'.join(['aut', item['runid'], 'pdf'])
            if item['type'] == 'manual':
                appendix = '.'.join(['man', item['runid'], 'pdf'])
        if item['track'] == 'session':
                runid = '.'.join(item['runid'].split('.')[:-1])
                appendix = '.'.join([runid, 'pdf'])
        if item['track'] == 'crowd':
            if item['task'] == 'task1':
                appendix = 'crowd-sourcing.assessment.pdf'
            if item['task'] == 'task2':
                appendix = 'crowd-sourcing.consensus.pdf'

    # TREC-18 appendix
    if item['trec'] == 'trec18':
        if item['track'] == 'relfdbk':
            appendix = '.'.join([item['pid'], 'pdf'])
        if item['track'] == 'million-query':
            appendix = '.'.join([item['runid'], 'main', 'pdf'])
        if item['track'] == 'web':
            if item['task'] == 'diversity':
                appendix = '.'.join([item['runid'], 'main', 'pdf'])

    return appendix


def make_appendix_url(item, appendix):
    # common appendix_url
    appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/{1}/{2}'.format(item['trec'], item['track'], appendix)

    if item['trec'] == 'trec33':
        appendix_url = 'https://trec.nist.gov/pubs/trec33/appendices/{0}.html'.format(item['task'])

    # TREC-COVID
    if item['trec'] == 'trec-covid':
        appendix_url = 'https://ir.nist.gov/trec-covid/archive/{0}/{1}.pdf'.format(item['track'], item['runid'])

    # TREC-26 appendix_url
    if item['trec'] == 'trec26':
        if item['track'] == 'domain':
            appendix_url = 'https://trec.nist.gov/pubs/trec26/appendices/dynamic-domain-tables.pdf'
        if item['track'] == 'open':
            appendix_url = 'https://trec.nist.gov/pubs/trec26/appendices/trec-os-2017.pdf'
    
    # TREC-25 appendix_url
    if item['trec'] == 'trec25':
        if item['track'] == 'realtime':
            appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/rts/{1}'.format(item['trec'], appendix)
        if item['track'] == 'open':
            if item['type'] == 'CiteSeerX':
                appendix_url = 'https://trec.nist.gov/pubs/trec25/appendices/open-citeseer.pdf'
            if item['type'] == 'SSOAR':
                appendix_url = 'https://trec.nist.gov/pubs/trec25/appendices/open-ssoar.pdf'
        if item['track'] == 'domain':
            appendix_url = 'https://trec.nist.gov/pubs/trec25/appendices/dd-notebook-appendix.pdf'
    
    # TREC-20 appendix_url
    if item['trec'] == 'trec20':
        if item['track'] == 'entity':
            if item['task'] != 'ref':
                appendix_url = None
    
    # TREC-19 appendix_url
    if item['trec'] == 'trec19':
        if item['track'] == 'blog':
            if item['task'] == 'blfeed':
                appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/blfeed-blog.baseline/{0}.{1}.pdf'.format(item['pid'], item['task'])
            if item['task'] == 'feed':
                appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/feed-blog.faceted/{0}.{1}.pdf'.format(item['pid'], item['task'])
            else:
                appendix_url = None 
        if item['track'] == 'chemical':
            appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/chem/{0}.{1}.pdf'.format(item['pid'], item['task'])
            if item['task'] == 'techsurv' or item['pid'] == 'IowaS':
                appendix_url = None
        if item['track'] == 'legal':
            if item['task'] == 'learning':
                appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/legal-learning/{}.pdf'.format(item['runid'])
            else:
                appendix_url = None
        if item['track'] == 'web':
            if item['task'] in ['adhoc', 'diversity']:
                appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/web-adhoc-diversity/{}.adhoc.pdf'.format(item['pid'])
            if item['task'] == 'spam':
                appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/web-spam/{}-all.pdf'.format(item['runid'])
                if item['runid'] in ['1', '2']:
                    appendix_url = 'https://trec.nist.gov/pubs/trec19/appendices/web-spam/Budapest1-all.pdf'
    
    # TREC-18 appendix_url
    if item['trec'] == 'trec18':
        if item['track'] == 'chemical':
            if item['task'] == 'techsurv':
                appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/chem.tech-survey.pdf'
            if item['task'] == 'priorart':
                appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/chem.prior-art.pdf'
            if item['task'] == 'priorart_sm':
                appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/chem.prior-art.sm.pdf'
        if item['track'] == 'entity':
            appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/entity.pdf'
        if item['track'] == 'legal':
            appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/legal/app09scores.pdf'
        if item['track'] == 'million-query':
            appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/mq/{1}'.format(item['trec'], appendix)
        if item['track'] == 'web':
            if item['task'] == 'diversity':
                appendix_url = 'https://trec.nist.gov/pubs/trec18/appendices/web-diversity/appendix.pdf'
            if item['task'] == 'adhoc':
                appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/web-adhoc-{1}/{2}.adhoc.pdf'.format(item['trec'], item['of_1'].lower(), item['runid'])
        if item['track'] == 'blog':
            appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/blog-{1}/{2}.{3}.pdf'.format(item['trec'], item['task'], item['runid'], item['task'])
    
    # TREC-17 appendix_url
    if item['trec'] == 'trec17':
        if item['track'] == 'blog':
            if item['task'] in ['baseline', 'opinion']:
                appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/{1}/{2}.{3}.pdf'.format(item['trec'], item['track'], item['runid'], item['task'])
            if item['task'] == 'polarity':
                appendix_url = json.dumps({
                    'Appendix (Negative Polarity)': 'https://trec.nist.gov/pubs/{0}/appendices/{1}/{2}.negative.polarity.pdf'.format(item['trec'], item['track'], item['runid']),
                    'Appendix (Positive Polarity)': 'https://trec.nist.gov/pubs/{0}/appendices/{1}/{2}.positive.polarity.pdf'.format(item['trec'], item['track'], item['runid'])
                })
        if item['track'] == 'million-query':
            appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/million.query/{1}.main.pdf'.format(item['trec'], item['runid'])
        if item['track'] == 'enterprise':
            if item['task'] == 'document':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/enterprise.discussion.results.pdf'
            if item['task'] == 'expert':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/enterprise.expert.results.pdf'
        if item['track'] == 'enterprise': 
            if item['task'] == 'adhoc':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal/app08ah3.pdf'
            if item['task'] == 'feedback':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal/app08rf3.pdf'
            if item['task'] == 'interactive':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal.interactive.results.pdf'
        if item['track'] == 'relfdbk': 
            appendix_url = 'https://trec.nist.gov/pubs/{0}/appendices/relevance.feedback/{1}.main.pdf'.format(item['trec'], item['pid'])
        if item['track'] == 'legal':
            if item['task'] == 'adhoc':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal/app08ah3.pdf'
            if item['task'] == 'feedback':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal/app08rf3.pdf'
            if item['task'] == 'interactive':
                appendix_url = 'https://trec.nist.gov/pubs/trec17/appendices/legal.interactive.results.pdf'
    
    # TREC-16 appendix_url
    if item['trec'] == 'trec16':
        if item['track'] in ['blog', 'enterprise']:
            appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
            if item['task'] in ['feed', 'polarity']: # tasks of 'blog'
                appendix_url = None
        else:
            appendix_url = None
        if item['track'] == 'legal':
            if item['task'] in ['main', 'routing']:
                appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
            if item['task'] == 'interactive':
                appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/legal/interactive.pdf'
        if item['track'] in ['genomics']:
            appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/{0}/{1}.main.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'million-query':
            if item['task'] == 'official':
                    appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/million.query/{}.official.pdf'.format(item['runid'])
            else:
                appendix_url = None
        if item['track'] == 'qa':
            appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'spam':
            appendices = {
                'x3d': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}x3d.pdf',
                'x3f': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}x3f.pdf',
                'pd': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}pd.pdf',
                'pf': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}pf.pdf',
                'pp': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}pp.pdf',
                'p1000': 'https://trec.nist.gov/pubs/trec16/appendices/spam/{}p1000.pdf'
            }
            appendix_url = 'https://trec.nist.gov/pubs/trec16/appendices/spam.results.html'
            abbrv = None
            if item['pid'] == 'beijingu-posts-tele.weiran':
                abbrv = 'kid'
                kinds = ['x3d', 'x3f']
            if item['pid'] == 'mitsubhishi.yerazunis':
                abbrv = 'crm'
                kinds = ['x3d', 'x3f', 'pd', 'pf', 'pp']
            if item['pid'] == 'fudanu.niu':
                abbrv = 'fdw'
                kinds = appendices.keys()
            if item['pid'] == 'heilongjiang-it.qi':
                abbrv = 'hit'
                kinds = ['pd', 'pf', 'pp', 'p1000']
            if item['pid'] == 'indianau.yang':
                abbrv = 'iub'
                kinds = ['x3f', 'pd', 'pf', 'pp', 'p1000']
            if item['pid'] == 'iiit-hyderbad':
                abbrv = 'III'
                kinds = ['x3d', 'x3f', 'pf']
            if item['pid'] == 'jozef-stefan-inst.bratko':
                abbrv = 'ijs'
                kinds = appendices.keys()
            if item['pid'] == 'nationalu-defense-tech.liu':
                abbrv = 'ndt'
                kinds = appendices.keys()
            if item['pid'] == 'sjtu-cs-spam':
                abbrv = 'sjt'
                kinds = appendices.keys()
            if item['pid'] == 'schina.utech.weidong':
                abbrv = 'scu'
                kinds = ['x3f', 'pd', 'pf', 'pp', 'p1000']
            if item['pid'] == 'tufts.sculley':
                abbrv = 'tft'
                kinds = appendices.keys()
            if item['pid'] == 'uwaterloo.clarke':
                abbrv = 'wat'
                kinds = appendices.keys()
            if abbrv:
                out = {}
                for k in kinds:
                    out['Appendix ({})'.format(k)] = appendices[k].format(abbrv)
                appendix_url = json.dumps(out)
    
    # TREC-15 appendix_url
    if item['trec'] == 'trec15':
        if item['track'] == 'blog':
            if item['task'] == 'opinion':
                appendix_url = 'https://trec.nist.gov/pubs/trec15/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
        if item['track'] in ['enterprise',  'terabyte']:
            appendix_url = 'https://trec.nist.gov/pubs/trec15/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
        if item['track'] in ['genomics', 'legal']:
            appendix_url = 'https://trec.nist.gov/pubs/trec15/appendices/{0}/{1}.main.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'qa':
            appendix_url = 'https://trec.nist.gov/pubs/trec15/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'spam':
            appendix_url = 'https://trec.nist.gov/pubs/trec15/appendices/spam.results.html'
    
    # TREC-14 appendix_url
    if item['trec'] == 'trec14':
        if item['track'] in ['enterprise',  'terabyte']:
            appendix_url = 'https://trec.nist.gov/pubs/trec14/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
        if item['track'] == 'genomics':
            if item['task'] == 'adhoc':
                appendix_url = 'https://trec.nist.gov/pubs/trec14/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
            if item['task'] == 'categorization':
                appendix_url = 'https://trec.nist.gov/pubs/trec14/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['pid'], item['task'])
        if item['track'] in ['HARD', 'qa', 'robust']:
            appendix_url = 'https://trec.nist.gov/pubs/trec14/appendices/{0}/{1}.table.pdf'.format(item['track'].lower(), item['runid'])
        if item['track'] == 'spam':
            appendix_url = 'https://trec.nist.gov/pubs/trec14/appendices/spam.results.html'
            abbrv = None
            if item['pid'] == 'beijingu.guo':
                abbrv = 'kid'
            if item['pid'] == 'breyer.laird':
                abbrv = 'lb'
            if item['pid'] == 'cas-ict.wang':
                abbrv = 'ICT'
            if item['pid'] == 'dalhousieu.keselj':
                abbrv = 'dal'
            if item['pid'] == 'ibm.segal':
                abbrv = '621'
            if item['pid'] == 'indianau.yang':
                abbrv = 'ind'
            if item['pid'] == 'jozef-stefan-inst.bratko':
                abbrv = 'ijs'
            if item['pid'] == 'masseyu.meyer':
                abbrv = 'tam'
            if item['pid'] == 'merl.yerazunis':
                abbrv = 'crm'
            if item['pid'] == 'puc-rs.terra':
                abbrv = 'puc'
            if item['pid'] == 'uparis-sud.aze':
                abbrv = 'aze'         
            if item['pid'] == 'yorku.huang':
                abbrv = 'yor'  
            if abbrv:   
                appendix_url = json.dumps({
                    'Appendix (aggregate results)': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}agg.pdf'.format(abbrv),
                    'Appendix (public corpus [full])': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}full.pdf'.format(abbrv),
                    'Appendix (Mr. X Private corpus)': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}mrx.pdf'.format(abbrv),
                    'Appendix (S.B. Private corpus)': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}sb.pdf'.format(abbrv),
                    'Appendix (T.M. Private corpus)': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}tm.pdf'.format(abbrv),
                    'Appendix (public corpus [five subsets])': 'https://trec.nist.gov/pubs/trec14/appendices/spam/{}.pdf'.format(abbrv)
                })
    
    # TREC-13 appendix_url
    if item['trec'] == 'trec13':
        if item['track'] in ['novelty', 'qa', 'robust', 'hard', 'HARD']:
            appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'genomics':
            if item['task'] == 'adhoc':
                appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid'])
            else:
                appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/{0}/{1}.{2}.table.pdf'.format(item['track'], item['pid'], item['task'])
        if item['track'] == 'terabyte':
            appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/{0}/{1}.tb.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'web':
            if item['task'] == 'mixed':
                appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/{0}/{1}.mixed.pdf'.format(item['track'], item['pid'])
            else:
                appendix_url = 'https://trec.nist.gov/pubs/trec13/appendices/web/classification.pdf'
    
    # TREC-12 appendix_url
    if item['trec'] == 'trec12':
        if item['track'] == 'genomics':
            if item['task'] == 'primary':
                appendix_url = 'https://trec.nist.gov/pubs/trec12/appendices/genome/{}.table.pdf'.format(item['runid'])
            if item['task'] == 'secondary':
                appendix_url = 'https://trec.nist.gov/pubs/trec12/appendices/genome/{}.table2.pdf'.format(item['runid'])
        if item['track'] in ['hard', 'novelty', 'robust', 'web']:
            appendix_url = 'https://trec.nist.gov/pubs/trec12/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid'])
        if item['track'] == 'qa':
            appendix_url = 'https://trec.nist.gov/pubs/trec12/appendices/{0}/{1}.{2}.pdf'.format(item['track'], item['runid'], item['task'])
    
    # TREC-11 appendix_url
    if item['trec'] == 'trec11':
        if item['track'] == 'xlingual':
            appendix_url = 'https://trec.nist.gov/pubs/trec11/appendices/cross.language/{}.table.pdf'.format(item['runid'])
        if item['track'] == 'filtering':
            appendix_url = 'https://trec.nist.gov/pubs/trec11/appendices/filtering/{0}.{1}.pdf'.format(item['pid'], item['task'])
        if item['track'] in ['novelty', 'qa', 'web']:
            appendix_url = 'https://trec.nist.gov/pubs/trec11/appendices/{0}/{1}.table.pdf'.format(item['track'], item['runid']) 
        if item['track'] == 'video':
            appendix_url = 'https://trec.nist.gov/pubs/trec11/appendices/video.sb.html'
    
    # TREC-10 appendix_url
    if item['trec'] == 'trec10':
        if item['track'] in ['xlingual', 'filtering', 'qa', 'web']:
            appendix_url = 'https://trec.nist.gov/pubs/trec10/appendices/{0}/{1}.pdf'.format(item['track'], item['runid'])       
        if item['track'] == 'video':
            appendix_url = json.dumps({
                    'nb.backintro1': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.backintro1.pdf',
                    'nb.backintro2': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.backintro2.pdf',
                    'nb.gs.precision': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.gs.precision.pdf', 
                    'nb.ki.precision': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.ki.precision.pdf',
                    'nb.ki.recall': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.ki.recall.pdf',
                    'nb.sb.cutsgrad.insertcount': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.sb.cutsgrad.insertcount.pdf',
                    'nb.sb.cuts.precisionrecall': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.sb.cuts.precisionrecall.pdf',
                    'nb.sb.grad.precisionrecall': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.sb.grad.precisionrecall.pdf',
                    'nb.topics': 'https://trec.nist.gov/pubs/trec10/appendices/video/nb.topics.pdf'
                })   
    
    # TREC-9 appendix_url
    if item['trec'] == 'trec9':
        if item['track'] == 'xlingual':
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/xlingual/{}.pdf'.format(item['runid'])
        if item['track'] == 'filtering':
            if item['task'] == 'adaptive':
                appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/filtering/{}.adapt.pdf'.format(item['pid'])
            if item['task'] in ['batch', 'batch-adaptive']:
                appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/filtering/{}.batch.pdf'.format(item['pid'])
            if item['task'] == 'routing':
                appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/filtering/{}.rout.pdf'.format(item['pid'])
        if item['track'] == 'interactive':
            pid = item['pid']
            if pid == 'OHSU':
                pid = pid.lower()
            if pid == 'RMIT':
                pid = 'csiro.rmit'
            if pid == 'rutgers-belkin':
                pid = 'rutgers'
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/interactive/{}.results.pdf'.format(pid)
        if item['track'] == 'qa':
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/qa/{}.pdf'.format(item['runid'])
        if item['track'] == 'sdr':
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/sdr/{}.pdf'.format(item['runid'])
        if item['track'] == 'web':
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/web/{}.pdf'.format(item['runid'])
        if item['track'] == 'query':
            appendix_url = 'https://trec.nist.gov/pubs/trec9/appendices/A/query/pretty_print.pdf'  
    
    # TREC-8 appendix_url
    if item['trec'] == 'trec8':
        if item['track'] == 'adhoc':
            appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/adhoc_results/{}.table.pdf'.format(item['runid'])
        if item['track'] == 'girt':
            appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/xlingual_girt_results/{}.table.pdf'.format(item['runid'])
        if item['track'] == 'xlingual':
            if item['task'] == 'german':
                appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/xlingual_girt_results/{}.table.pdf'.format(item['runid'])
            if item['runid'] in xligualalt_special_url:
                appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/xlingual_alt_results/{}.table.pdf'.format(item['runid'])                   
            else:
                appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/xlingual_results/{}.table.pdf'.format(item['runid'])
        if item['track'] == 'filtering':
            if item['task'] == 'batch':
                appendix_url = json.dumps({
                    'Appendix (LF1 Measure)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/batch.LF1.pdf',
                    'Appendix (LF2 Measure)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/batch.LF2.pdf'
                })
            if item['task'] == 'adaptive':
                appendix_url = json.dumps({
                    'Appendix (LF1 Measure, Year 92-94)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF1.92-94.pdf',
                    'Appendix (LF1 Measure, Year 92)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF1.92.pdf',
                    'Appendix (LF1 Measure, Year 93)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF1.93.pdf',
                    'Appendix (LF1 Measure, Year 94)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF1.94.pdf',
                    'Appendix (LF2 Measure, Year 92-94)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF2.92-94.pdf',
                    'Appendix (LF2 Measure, Year 92)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF2.92.pdf',
                    'Appendix (LF2 Measure, Year 93)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF2.93.pdf',
                    'Appendix (LF2 Measure, Year 94)': 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/adapt.LF2.94.pdf'
                })
            if item['task'] == 'routing':
                appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/filtering_results/rout.pdf' 
        if item['track'] == 'interactive':
            appendix_url = json.dumps({
                    'Measures': 'https://trec.nist.gov/pubs/trec8/appendices/A/interactive_results/measures.pdf',
                    'Topic Instances': 'https://trec.nist.gov/pubs/trec8/appendices/A/interactive_results/topic-instances.pdf'
                }) 
        if item['track'] == 'qa':
            appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/qa_results/{}.pdf'.format(item['runid'])
        if item['track'] == 'sdr':
            appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/sdr_results/{}.table.pdf'.format(item['runid'])
        if item['track'] == 'web':
            appendix_url = 'https://trec.nist.gov/pubs/trec8/appendices/A/small_web_results/{}.table.pdf'.format(item['runid'])
    
    # TREC-7 appendix_url
    if item['trec'] == 'trec7':
        if item['track'] == 'adhoc':
            appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/adhoc_results/{}.table.pdf.gz'.format(item['runid'])
        if item['track'] == 'xlingual':
            appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/xlingual_results/{}.table.pdf.gz'.format(item['runid'])
        if item['track'] == 'hp':
            appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/hp_results/{}.table.pdf.gz'.format(item['runid'])
        if item['track'] == 'query':
            appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/query_results/query.pdf.gz'
        if item['track'] == 'sdr':
            appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/sdr_results/{}.table.pdf.gz'.format(item['runid'])
        if item['track'] == 'filtering':
            if item['runid'] in ['CLARITafF1a', 'CLARITafF1b', 'IAHKaf11', 'IAHKaf12', 'INQ510', 'Mer7AGbF1', 'Mer7ARbF1', 'ok7ff12', 'ok7ff13', 'pirc8FA1', 'sigmaTrec7F1', 'TNOAF102']:
                appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/filtering_results/adapt.F1.pdf.gz'
            if item['runid'] in ['CLARITafF3a',  'CLARITafF3b',  'IAHKaf31',  'IAHKaf32',  'INQ511',  'Mer7AGbF3',  'Mer7ARbF3',  'ok7ff32',  'ok7ff33',  'pirc8FA3',  'sigmaTrec7F3',  'TNOAF103']:
                appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/filtering_results/adapt.F3.pdf.gz'
            if item['runid'] in ['att98fb5', 'CLARITbfF1', 'IAHKbf11', 'MerBF1', 'nttd7bf1', 'pirc8FB1']:
                appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/filtering_results/batch.F1.pdf.gz'
            if item['runid'] in ['att98fb6', 'CLARITbfF3', 'IAHKbf32', 'MerBF3', 'nttd7bf3', 'pirc8FB3']:
                appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/filtering_results/batch.F3.pdf.gz'
            if item['runid'] in ['AntRout1', 'AntRout2', 'arc98cs', 'att98fr4', 'att98fr5', 'MerRou', 'nttd7rt1', 'nttd7rt2', 'pirc8R1', 'pirc8R2']:
                appendix_url = 'https://trec.nist.gov/pubs/trec7/appendices/A/filtering_results/rout.pdf.gz'
    
    # TREC-6 appendix_url
    if item['trec'] == 'trec6':
        if item['track'] == 'adhoc':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/adhoc.runs.pdf.gz'
        if item['track'] == 'routing':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/routing.runs.ps.gz'
        if item['track'] == 'chinese':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/chinese.runs.ps.gz'
        if item['track'] == 'clir':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/xlingual.runs.ps.gz'
        if item['track'] == 'filtering':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/papers/filter.track.figs.ps.gz'
        if item['track'] == 'hp':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/high-prec.runs.ps.gz'
        if item['track'] == 'interactive':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/t6iresults.ps.gz'
        if item['track'] == 'nlp':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/nlp.runs.ps.gz'
        if item['track'] == 'sdr':
            appendix_url = 'https://trec.nist.gov/pubs/trec6/appendices/A/sdr.runs.ps.gz'
    
    # TREC-5 appendix_url
    if item['trec'] == 'trec5':
        if item['track'] in ['adhoc', 'routing', 'Chinese', 'Spanish', 'dbmerge', 'nlp']:
            appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/{}.graphs.ps.gz'.format(item['track'].lower())
        if item['track'] == 'filtering':
            if item['pid'] == 'City':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/city96f.table.ps.gz'
            if item['pid'] == 'UMass':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/INR3.table.ps.gz'
            if item['pid'] == 'Intext':
                if item['type'] == 'automatic':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/INTXA.table.ps.gz'
                if item['type'] == 'manual':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/INTXM.table.ps.gz'
            if item['pid'] == 'UIUC':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/ispF.table.ps.gz'
            if item['pid'] == 'ITI-SG':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/iti96f.table.ps.gz'
            if item['pid'] == 'CUNY':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/pircs96f.table.ps.gz'
            if item['pid'] == 'Xerox':
                if item['runid'][7] == '1':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/xerox.f1.table.ps.gz'
                if item['runid'][7] == '2':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/xerox.f2.table.ps.gz'
                if item['runid'][7] == '3':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/xerox.f3.table.ps.gz'
        if item['track'] == 'interactive':
            if item['pid'] == 'City':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/notebook.page.city.ps.gz'
            if item['pid'] == 'RutgersB':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/notebook.page.rutgers.ps.gz'
        if item['track'] == 'confusion':
            if item['pid'] == 'ANU':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/anu5con.table.ps.gz'
            if item['pid'] == 'GMU':
                if item['runid'][-2] == '2':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/gmu962.table.ps.gz'
                else: 
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/gmu961.table.ps.gz'
            if item['pid'] == 'CLARITECH':
                if item['runid'][-1] == 'F':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/CLCONF.table.ps.gz'
                else: 
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/CLCON.table.ps.gz'
            if item['pid'] == 'RutgersK':
                appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/rutcf.table.ps.gz'
            if item['pid'] == 'ETH':
                if item['runid'][-1] == 'P':
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/ETHFR94P.table.ps.gz'
                else:
                    appendix_url = 'https://trec.nist.gov/pubs/trec5/appendices/A/ETHFR94N.table.ps.gz'
    
    # TREC-4 appendix_url
    if item['trec'] == 'trec4':
        if item['track'] == 'adhoc':
            appendix_url = 'https://trec.nist.gov/pubs/trec4/appendices/A/trec4.{}.list.graphs.ps.gz'.format(item['track'])
        if item['track'] == 'interactive':
            appendix_url = None
    
    # TREC-3 appendix_url
    if item['trec'] == 'trec3': 
        appendix_url = 'https://trec.nist.gov/pubs/trec3/appendices/A/{}.list.graphs.ps.gz'.format(item['track'])
    
    # TREC-2 appendix_url
    if item['trec'] == 'trec2': 
        appendix_url = 'https://trec.nist.gov/pubs/trec2/appendices/A.txt'
    
    return appendix_url


def add_input_url(item):
    if (item['trec'], item['track']) in no_input:
        input_url = None
    else:
        input = make_input(item) 
        input_url = make_input_url(item, input)
    item['input_url'] = input_url
    return item


def add_summary_url(item):
    if (item['trec'], item['track']) in no_summary:
        summary_url = None
    else:
        summary = make_summary(item)
        summary_url = make_summary_url(item, summary)
    item['summary_url'] = summary_url
    return item


def add_appendix_url(item):
    if (item['trec'], item['track']) in no_appendix:
        appendix_url = None
    else:
        appendix = make_appendix(item) 
        appendix_url = make_appendix_url(item, appendix) 
    item['appendix_url'] = appendix_url
    return item


def remove_task(item):
    if item['task'].strip() in no_tasks:
        item['task'] = None
    return item 


def remove_type(item):
    if item['type'].strip() not in no_type:
        item['type'] = None
    return item 


def pop_fields(item, _type):
    if _type == 'runs':
        item.pop('notes', None)
        item.pop('merge', None)
        item.pop('of_1', None)
        item.pop('of_2', None)
        item.pop('of_3', None)
        item.pop('of_4', None)
        item.pop('of_5', None)
        item.pop('email', None) 
    if _type == 'participants':
        item.pop('address', None)
        item.pop('phone', None)
        item.pop('fax', None)
        item.pop('track-interest', None)
        item.pop('date', None)
        item.pop('ad-form', None)
        item.pop('tipster-form', None)
        item.pop('trec-form-disk4', None)
        item.pop('trec-form-disk5', None)
        item.pop('notes', None)
        item.pop('email', None) 
    if _type == 'covid-runs':
        item.pop('email', None)
        item.pop('task', None)
        item.pop('num', None)
        item.pop('of_4', None)
        item.pop('of_5', None) 
        item.pop('notes', None)
    if _type == 'covid-participants':
        item.pop('runid', None)
        item.pop('type', None)
        item.pop('description', None)
        item.pop('md5', None)
        item.pop('date', None)
        item.pop('email', None)
        item.pop('task', None)
        item.pop('num', None)
        item.pop('judge', None)
        item.pop('of_4', None)
        item.pop('of_5', None) 
        item.pop('notes', None)


def adjust_email_field(item):
    if trec_year(item['trec']) < 2009 and trec_year(item['trec']) > 2005:
        if item.get('name') and item.get('email'):
            item['name'] = item['email']
            item['email'] = item['trec-form-disk4']
    if trec_year(item['trec']) < 2006:
        if item.get('name') and item.get('email'):
            item['name'] = ' '.join([item['name'], item['email']])
            item['email'] = item['trec-form-disk5']
    return item


def adjust_fields(item):
    if item['track'] == 'misinfo' and item['trec'] in ['trec31', 'trec30', 'trec29']:
        item['fields'] = item['of_2']
    if item['track'] == 'car':
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec27', 'core'):
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec26', 'core'):
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec25', 'recall'):
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec23', 'web'):
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec21', 'microblog'):
        item['fields'] = None        
    if (item['trec'], item['track']) == ('trec20', 'crowd'):
        item['fields'] = None
    if (item['trec'], item['track']) == ('trec9', 'filtering'):
        item['fields'] = None 
    if (item['trec'], item['track']) == ('trec5', 'confusion'):
        item['fields'] = None
    return item 


def add_other(item):
    if (item['trec'], item['track']) == ('trec32', 'atomic'):
        item['other'] = {
            'index_cost': item['of_2'],
            'training_cost': item['of_3'], 
            'query_cost': item['of_4']
        }

    if (item['trec'], item['track']) == ('trec32', 'ikat'):
        item['other'] = {
            'training_data': item['merge'],
            'meta_1': item['of_1'],
            'meta_2': item['of_2'],
            'meta_3': item['of_3'],
            'meta_4': item['of_4'],
            'meta_5': item['of_5']
        }

    if (item['trec'], item['track']) == ('trec32', 'tot'):
        item['other'] = {
            'external_resources': urllib.parse.unquote(item['of_1'])
        }

    if (item['trec'], item['track']) == ('trec32', 'crisis'):
        item['other'] = {
            'importance_score': urllib.parse.unquote(item['of_2']),
            'extractive_abstractive': urllib.parse.unquote(item['of_4']),
        }

    if (item['trec'], item['track']) == ('trec32', 'neuclir') or \
        (item['trec'], item['track']) == ('trec31', 'neuclir'):
        if len(item['of_3'].split('-')) > 1:
            baseline= item['of_3'].split('-')[1]
        else:
            baseline = 'no'      
        item['other'] = {
            'baseline': baseline,
            'rerank': item['of_3'].split('-')[0], 
            'query_form': item['of_2'],
            'doc_form': item['of_1']
        }
        if item['trec'] == 'trec32':
            item['other']['time'] = item['merge']

    if (item['trec'], item['track']) == ('trec32', 'trials') or \
        (item['trec'], item['track']) == ('trec31', 'trials') or \
            (item['trec'], item['track']) == ('trec30', 'trials'):
        item['other'] = {
            'external_resources': urllib.parse.unquote(item['of_3'])
        }

    if (item['trec'], item['track']) == ('trec32', 'deep') or \
        (item['trec'], item['track']) == ('trec31', 'deep'):
        item['other'] = {
            'subtask': item['of_1'].split('-')[0],
            'single_stage': item['of_1'].split('-')[1],
            'dense_retrieval': item['of_1'].split('-')[2],
            'baseline': item['of_4'].split('-')[2] ,
            'dnn_type': item['of_4'].split('-')[1],
            'training_type': item['merge'],
            'training_cost': urllib.parse.unquote(item['of_3']),
            'indexing_cost': urllib.parse.unquote(item['of_2']),
            'query_processing_cost': urllib.parse.unquote(item['of_5'])
        }


    if (item['trec'], item['track']) == ('trec31', 'crisis'):
        item['other'] = {
            'trec_is_labels': item['of_1'],
            'method_info': urllib.parse.unquote(item['of_2']),
            'streams': item['of_3'],
            'extractive_abstractive': item['of_4']
        }

    if (item['trec'], item['track']) == ('trec31', 'cast'):
        if item['task'] == 'primary':
            item['other'] = {
                'query_understanding_method': item['of_1'],
                'query_understanding_data': item['of_2'],
                'ranking_method': item['of_3'],
                'ranking_data': item['of_4'],
                'response_generation': item['of_5'].split('-')[1],
                'initiative': item['of_5'].split('-')[0],
                'external_resources': urllib.parse.unquote(item['merge'])
            }
        if item['task'] == 'mixed':
            item['other'] = {
                'selective_interaction_method': item['of_1'],
                'question_selection_method': item['of_2'],
                'question_selection_context': item['of_3'],
                'question_ranking_method': item['of_4'],
                'cast_mixed_data': item['of_5'],
                'external_resources': urllib.parse.unquote(item['merge'])
            }

    if (item['trec'], item['track']) == ('trec31', 'fair'):
        item['other'] = {
            'method_info': urllib.parse.unquote(item['of_2'])
        }

    if (item['trec'], item['track']) == ('trec30', 'deep'):
        item['other'] = {
            'subtask': item['of_1'].split('-')[0],
            'single_stage': item['of_1'].split('-')[1],
            'dense_retrieval': item['of_1'].split('-')[2],
            'dnn_type': item['of_4'].split('-')[1],
            'training_type': item['merge'],
            'training_cost': urllib.parse.unquote(item['of_3']),
            'indexing_cost': urllib.parse.unquote(item['of_2']),
            'query_processing_cost': urllib.parse.unquote(item['of_5'])
        }

    if (item['trec'], item['track']) == ('trec29', 'deep'):
        item['other'] = {
            'subtask': item['of_1'].split('-')[0],
            'dnn_type': item['of_2'],
            'training_type': item['of_3'],
            'training_cost': urllib.parse.unquote(item['merge']),
            'orcas': item['of_5']
        }

    if (item['trec'], item['track']) == ('trec28', 'deep'):
        item['other'] = {
            'subtask': item['of_1'].split('-')[0],
            'dnn_type': item['of_2'],
            'training_type': item['of_3'],
        }

    if (item['trec'], item['track']) == ('trec30', 'incident'):
            item['other'] = {
                'meta_1': item['of_2'],
                'meta_2': item['of_3'],
                'meta_3': item['of_4']
            }

    if (item['trec'], item['track']) == ('trec30', 'cast') or \
        (item['trec'], item['track']) == ('trec29', 'cast'):
        item['other'] = {
            'query_understanding_method': item['of_1'],
            'query_understanding_data': item['of_2'],
            'query_understanding_data_info': urllib.parse.unquote(item['merge']),
            'ranking_method': item['of_3'],
            'ranking_data': item['of_4'],
            'question_selection_context': item['of_5']  
        }

    if (item['trec'], item['track']) == ('trec30', 'podcast') or \
        (item['trec'], item['track']) == ('trec29', 'podcast') :
        if item['task'] == 'retrieval': 
            item['other'] = {
                'training_data': item['of_1'],
                'ranking_method': item['of_2'],
                'method_info': item['of_5']
            }
        if item['task'] == 'summarization': 
            item['other'] = {
                'training_data': item['of_1'],
                'summarization_method': item['of_3'],
                'summarization_model': item['of_4'],
                'method_info': item['of_5']
            }

    if (item['trec'], item['track']) == ('trec29', 'incident'):
        if item['type'] == 'auto':
            item['other'] = {
                'meta_1': item['of_2'],
                'meta_2': item['of_3']
            }

    if (item['trec'], item['track']) == ('trec29', 'pm') or \
        (item['trec'], item['track']) == ('trec28', 'pm'):
            item['other'] = {
                'external_resources': urllib.parse.unquote(item['of_3'])
            }

    if (item['trec'], item['track']) == ('trec28', 'cast'):
        item['other'] = {
            'query_understanding_method': item['of_1'],
            'ranking_method': item['of_2'], 
            'question_selection_context':  item['of_3'],
            'external_resources': urllib.parse.unquote(item['of_4'])
        }

    if (item['trec'], item['track']) == ('trec28', 'fair'):
        item['other'] = {
            'external_resources': urllib.parse.unquote(item['of_2'])
        }

    if (item['trec'], item['track']) == ('trec28', 'incident') or \
        (item['trec'], item['track']) == ('trec27', 'incident'):
            item['other'] = {
                'meta_1': item['of_2'],
                'meta_2': item['of_3']
            }

    if (item['trec'], item['track']) == ('trec27', 'core'):
        item['other'] = {
            'judged': item['fields']
        }

    if (item['trec'], item['track']) == ('trec26', 'core'):
        item['other'] = {
            'judged': item['fields'],
            'round': item['of_2'],
            'existing_judgments': item['of_4']
        }

    if (item['trec'], item['track']) == ('trec25', 'recall'):
            item['other'] = {
                'call_your_shot': urllib.parse.unquote(item['fields'])
            }

    if (item['trec'], item['track']) == ('trec25', 'context') or \
        (item['trec'], item['track']) == ('trec24', 'context') :
            item['other'] = {
                'external_resources': item['of_2']
            }

    if (item['trec'], item['track']) == ('trec23', 'context') or \
        (item['trec'], item['track']) == ('trec22', 'context') :
            item['other'] = {
                'main_data_source': item['type'],
                'secondary_data_source': item['of_1']
            }

    if (item['trec'], item['track']) == ('trec23', 'tempsumm') or \
        (item['trec'], item['track']) == ('trec22', 'tempsumm'):
        item['other'] = {
            'meta_1': item['of_1']
        }

    if (item['trec'], item['track']) == ('trec21', 'context'):
        item['other'] = {
            'evaluation_focus': item['type']
        }

    if (item['trec'], item['track']) == ('trec20', 'entity'):
        item['other'] = {
            'wiki_special_use': item['of_1'],
            'resources': item['of_2'],
            'used_other_resources': item['of_3'],
            'target_entity_field': item['of_4']
        }

    if (item['trec'], item['track']) == ('trec20', 'crowd'):
        item['other'] = {
            'resources': item['fields']
        }

    if (item['trec'], item['track']) == ('trec19', 'entity'):
        item['other'] = {
            'wiki_special_use': item['of_1'],
            'resources': item['of_2'],
            'used_other_resources': item['of_3']
        }

    if (item['trec'], item['track']) == ('trec18', 'entity'):
        item['other'] = {
            'wiki_special_use': item['of_1'],
            'resources': urllib.parse.unquote(item['of_2']),
            'used_other_resources': item['of_3']
        }

    if (item['trec'], item['track']) == ('trec18', 'million-query'):
        item['other'] = {
            'doc_fields': item['of_1'],
            'external_resources': item['of_2']
        }

    if (item['trec'], item['track']) == ('trec17', 'million-query'):
        item['other'] = {
            'doc_fields': item['of_1'],
            'external_resources': item['of_2']
        }

    if (item['trec'], item['track']) == ('trec17', 'relfdbk'):
        item['other'] = {
            'feedback_set': item['task']
        }

    if (item['trec'], item['track']) == ('trec17', 'enterprise'):
        item['other'] = {
            'external_resources': item['of_1']
        }

    if (item['trec'], item['track']) == ('trec16', 'million-query'):
        item['other'] = {
            'doc_fields': item['of_1'],
            'external_resources': item['of_2']
        }

    if (item['trec'], item['track']) == ('trec16', 'qa'):
        if item['task'] == 'ciqa_final':
            item['other'] = {
                'baseline': item['of_2'],
                'interaction_form': item['of_3']
            }
        if item['task'] == 'ciqa_urlfile':
            item['other'] = {
                'external_resources': item['of_5']
            }

    if (item['trec'], item['track']) == ('trec16', 'spam') or \
        (item['trec'], item['track']) == ('trec15', 'spam'):
            if item['task'] != 'run':
                item['other'] = {
                    'os': item['of_1'],
                    'system_requirements': item['of_2']
                }

    if (item['trec'], item['track']) == ('trec16', 'enterprise') or \
        (item['trec'], item['track']) == ('trec15', 'enterprise'):
        item['other'] = {
            'external_resources': item['of_1']
        }

    if (item['trec'], item['track']) == ('trec15', 'terabyte'):
        try:
            item['other'] = {
                'links_anchor_struct': item['of_4'],
                'time_index': item['of_2'].split('-')[0],
                'time_top20': item['of_2'].split('-')[1],
                'time_total': item['of_2'].split('-')[2],
                'time_total_cpu': item['of_2'].split('-')[3],
                'size': item['of_2'].split('-')[4],
                'num_cpu': item['of_1'].split('-')[1],
                'ram': item['of_1'].split('-')[2],
                'system_cost': item['of_1'].split('-')[4],
                'system_purchase': item['of_1'].split('-')[3],
                'os': item['of_1'].split('-')[5],
                'collection_percent': item['of_1'].split('-')[0]
            }  
        except:
            pass

    if (item['trec'], item['track']) == ('trec14', 'terabyte'):
        item['other'] = {
            'links_anchor_struct': item['of_4'],
            'time_index': item['of_2'].split('-')[0],
            'time_top20': item['of_2'].split('-')[1],
            'time_total': item['of_2'].split('-')[2],
            'size': item['of_5'],
            'num_cpu': item['of_3'].split('-')[0],
            'ram': item['of_3'].split('-')[1],
            'system_cost': item['description'].split('-')[1],
            'system_purchase': item['description'].split('-')[0],
            'collection_percent': item['of_1']
        }        

    if (item['trec'], item['track']) == ('trec14', 'spam'):
        if item['task'] != 'run':
            item['other'] = {
                'configuration_command': item['of_1'],
                'system_requirements': item['of_2']
            }

    if (item['trec'], item['track']) == ('trec13', 'terabyte'):
        item['other'] = {
            'links_anchor_struct': item['task'],
            'time_index': item['of_2'].split('-')[0],
            'time_top20': item['of_2'].split('-')[1],
            'ram': item['of_4'],
            'size': item['of_5'],
            'system_cost': item['description']
        }   

    if (item['trec'], item['track']) == ('trec13', 'robust'):
        item['other'] = {
            'optimized': item['of_1'],
            'optimized_measures': item['of_2'],
        }   

    if item['trec'] == 'trec13' and item['track'] == 'novelty':
        item['other'] = {
            'external_resources': item['of_1'],
            'term_expansion': item['of_2'].split('-')[0],
            'adaptive_threshold': item['of_2'].split('-')[1],
            'adaptive_term_model': item['of_2'].split('-')[2],
            'modeled_sentence_as': item['of_4'],
            'model_features': item['of_5']
        }

    if (item['trec'], item['track']) == ('trec12', 'robust'):
        item['other'] = {
            'optimized': item['of_1']
        }

    if item['trec'] == 'trec12' and item['track'] == 'novelty':
        item['other'] = {
            'external_resources': item['of_1']
        }

    if (item['trec'], item['track']) == ('trec11', 'xlingual'):
        item['other'] = {
            'stemming_resources': item['of_1'],
            'translation_resources': item['of_2'],
            'dictionary_resources': item['of_3'],
            'parallel_corpus_resources': item['of_4'],
        }

    if item['trec'] == 'trec11' and item['track'] == 'novelty':
        item['other'] = {
            'external_resources': item['of_3'],
            'external_resources_description': item['of_4']
        }

    if (item['trec'], item['track']) == ('trec9', 'sdr'):
        item['other'] = {
            'language_model': item['of_1'],
            'boundaries': item['of_2'],
            'non_lexical_other_info_used': item['of_3']
        }

    if (item['trec'], item['track']) == ('trec9', 'xlingual'):
        item['other'] = {
            'monolingual': item['of_5']
        }
           
    if (item['trec'], item['track']) == ('trec9', 'qa') or \
        (item['trec'], item['track']) == ('trec8', 'qa'):
        item['other'] = {
            'maximum_answer_length': item['task']
        }

    if (item['trec'], item['track']) == ('trec8', 'web'):
        item['other'] = {
            'information_used': item['task']
        }

    if (item['trec'], item['track']) == ('trec8', 'sdr'):
        item['other'] = {
            'language_model': item['task']
        }
        
    if (item['trec'], item['track']) == ('trec8', 'girt') or \
        (item['trec'], item['track']) == ('trec8', 'xlingual') :
        item['other'] = {
            'topic_language': item['task']
        }

    if item['track'] in ['rts', 'realtime']:
        if item['trec'] in ['trec27', 'trec26', 'trec25']:
            if item['task'] == 'b':
                item['other'] = {
                    'external_resources': item['of_2'],
                    'linked_documents': item['of_3']
                }

    if item['track'] == 'legal':
        if item['trec'] == 'trec20':
            item['other'] = {
                'external_resources' : item['fields'],
                'hours_configuring': item['of_1'].split('-')[0],
                'hours_searching': item['of_1'].split('-')[1],
                'hours_reviewing': item['of_1'].split('-')[2],
                'hours_analyzing': item['of_1'].split('-')[3],
                'other_resources' : item['of_3'],
                'ranking_method': item['of_4'],
                'probabilty': item['of_5'],
            }
        if item['trec'] == 'trec19':
            if item['task'] == 'learning':
                item['other'] = {
                    'external_resources' : item['fields'],
                    'other_resources' : item['of_3'],
                    'ranking_method': item['of_4'],
                    'probabilty': item['of_5'],
                }
        if item['trec'] == 'trec18':
            if item['task'] == 'batch':
                item['other'] = {
                    'doc_fields' : item['of_1'],
                    'used_boolean_ref_run' : item['of_2'],
                    'baseline': item['of_3'],
                    'doc_review': item['of_4'],
                    'baseline_name': item['of_5']
                }
        if item['trec'] == 'trec17':
            item['other'] = {
                'doc_fields' : item['of_1'],
                'used_boolean_ref_run' : item['of_2'],
                'baseline': item['of_3'],
                'doc_review': item['of_4'],
                'baseline_name': item['of_5']
            }
        if item['trec'] == 'trec16':
            item['other'] = {
                'doc_fields': item['of_1'],
                'reference_run': item['of_2']
            }
            if item['task'] == 'routing':
                item['other']['qrels_2006'] = item['of_3']
        if item['trec'] == 'trec15':
            item['other'] = {
                'doc_fields': item['of_1']
            }

    if item['track'] == 'decisions':
        item['other'] = {
            'meta_1': item['of_2']
        }

    if item['track'] == 'web':
        if item['trec'] in ['trec23', 'trec22', 'trec21', 'trec20', 'trec19', 'trec18']:
            item['other'] = {
                'external_resources': item['of_2'],
                'collection_category': item['of_1']
            }
        if item['trec'] in ['trec23', 'trec22']:
            item['other']['optimized_metric'] = item['of_3']

        if item['trec'] in ['trec13']:
            item['other'] = {
                'doc_struct': item['of_2'],
                'anchor_text': item['of_1'].split('-')[0],
                'link_struct':  item['of_1'].split('-')[1],
                'url_length': item['of_3'].split('-')[0],
                'url_features': item['of_3'].split('-')[1],
                'query_processing': item['of_4']
            }

        if item['trec'] in ['trec12', 'trec11', 'trec10']:
            item['other'] = {
                'doc_struct': item['of_1'],
                'anchor_text': item['of_2'],
                'link_struct': item['of_3']
            }

    if item['track'] == 'federated':
        item['other'] = {
            'external_resources': item['of_2'],
            'used_resources': item['of_1']
        }

    if item['track'] == 'kba':
        item['other'] = {
            'kba_corpus': item['of_1']
        }
        if item['trec'] == 'trec23':
            item['other']['method_info'] = urllib.parse.unquote(item['of_5'])
        
    if item['track'] == 'task':
        item['other'] = {
            'external_resources': item['type'],
            'collection_category': item['of_2']
        }

    if item['track'] == 'microblog':
        item['other'] = {
            'external_resources': item['of_2'],
            'linked_documents': item['of_3']    
        }
        if item['trec'] in ['trec21', 'trec20']:
            item['other']['crawl_indexed'] = item['of_1']
            item['other']['realtime_constraints'] = item['of_2']
        if item['trec'] in ['trec21']:
            item['other']['crawl_date'] = item['fields']
            item['other']['num_200_301_tweets'] = item['of_5']

    if item['track'] == 'filtering':
        if item['trec'] in ['trec11', 'trec10', 'trec9']:
            item['other'] = {
                'trec_data': item['of_1'],
                'reuters_data': item['of_2'],
                'other_data': item['of_3']
            }
            if item['task'] == 'batch' or item['trec'] in ['trec11', 'trec10', 'trec9']:
                item['other']['optimized_for'] = item['of_5']
            if item['trec'] == 'trec9':
                item['other']['topic_set'] = item['fields']

    if item['track'] == 'session':
        item['other'] = {
            'collection_category': item['of_1'] 
        }

    if item['track'] == 'blog':
        item['other'] = {
            'doc_fields': item['of_1']
        }
        if item['trec'] == 'trec19':
            item['other']['baseline'] = item['of_3']
        if item['trec'] == 'trec17':
            if item['task'] != 'baseline':
                item['other']['baseline'] = item['of_2']
        if item['trec'] == 'trec16':
            item['other']['external_resources'] = item['of_2']

    if item['track'] in ['hard', 'HARD']:
        if item['trec'] == 'trec14':
            item['other'] = {
                'training_trec_judge': item['of_1']
            }
        if item['trec'] in ['trec13', 'trec12']:
            item['other'] = {
                'baseline': item['of_1'],
                'metadata': item['of_2']
            }
        if item['trec'] == 'trec13':
            item['other']['cf'] = item['of_4']

    if item['track'] == 'news':
        item['other'] = {
            'external_resources': item['of_2'],
            'wikipedia': item['of_3']
        }

    if item['track'] == 'car':
        item['other'] = {
            'external_resources': item['of_2'],
            'ranking_method': item['of_3'],
            'run_features': item['fields']
        }

    if item['trec'] in ['trec24', 'trec25', 'trec26']:
        repository = urllib.parse.unquote(item['of_1'])
        if 'http' in repository:
            if item.get('other'):
                item['other']['repository'] = repository
            else:
                item['other'] = {'repository': repository}

    if item.get('other'):
        item['other'] = json.dumps(item['other'])
    return item 


def remove_description(item):
    if item['trec'] == 'trec14' and item['track'] == 'terabyte':
        item['description'] = None
    return item 


def read_tables(_type='runs'):
    tables = []
    for i in range(2, 34):
        trec = ''.join(['trec', str(i)])
        table_file = 'runs_table' if _type == 'runs' else 'participants_table'
        table_path = os.path.join('./trec', trec, 'reports', table_file)
        items = table_list(table_path, _type)
        for item in items:
            item['trec'] = trec
            item['year'] = trec_year(trec)
            if _type == 'runs':
                item = rename_track_identifier(item)
                item = adjust_task_field(item)
                item = parse_description(item)
                item = check_md5(item)
                item = add_input_url(item)
                item = add_summary_url(item)
                item = add_appendix_url(item)
                item = add_other(item)

                item = adjust_fields(item)
                item = remove_description(item)
                item = remove_task(item)
                item = remove_type(item)
                pop_fields(item, _type)
                # TREC-32 (temporary solution until resources are online)
                #if trec == 'trec32':
                #    item['input_url'] = None 
                #    item['summary_url'] = None 
                #    item['appendix_url'] = None 
            if _type == 'participants':   
                item = adjust_email_field(item)
                pop_fields(item, _type)
        tables += items
    # TREC-COVID
    _type = '-'.join(['covid', _type]) 
    for i in range(1,6):
        trec =  'trec-covid'
        table_path = './trec/trec-covid/round{}/reports/runs_table'.format(str(i))
        items = table_list(table_path, _type)
        for item in items:
            item['trec'] = 'trec-covid'
            item['year'] = trec_year(trec)
            if _type == 'covid-runs':
                item['track'] = 'round{}'.format(str(i))
                item['summary_url'] = None
                item = parse_description(item)
                item = check_md5(item)
                item = add_input_url(item) 
                item = add_appendix_url(item)
                pop_fields(item, _type)
            if _type == 'covid-participants':
                item['organization'] = None
                item['name'] = None
                pop_fields(item, _type)
        tables += items
    return tables  


def write_publications_json():
    library = bibtexparser.parse_file('bibtex/trec.bib')
    lib_dict = {entry.key: entry for entry in library.entries}
    with open('./json/abstracts.json') as f_in:
        publications = json.loads(f_in.read())
    with open('./json/publications.json', 'w') as f_out:
        for i in range(2, 34):
            trec = ''.join(['trec', str(i)])
            trec_pubs = publications.get(trec)
            for track, pubs in trec_pubs.items():
                for key, metadata in pubs.items():
                    try:
                        url = lib_dict[key]['url']
                        metadata['url'] = LatexNodes2Text().latex_to_text(url)
                        metadata['biburl'] = lib_dict[key]['biburl']
                    except KeyError:
                        pass
                    metadata['key'] = key
                    if metadata['pid'] == 'coordinators':
                        metadata['pid'] = 'overview'
                    title = lib_dict[key]['title']
                    title = LatexNodes2Text().latex_to_text(title)
                    title = title.replace(18*' ', ' ')
                    title = title.replace('\n', ' ')
                    metadata['title'] = title
                    author = lib_dict[key]['author']
                    author = author.replace('\n','')
                    author = author.replace(18*' ',' ')
                    author = LatexNodes2Text().latex_to_text(author)
                    author = author.replace(' and ', ', ')
                    metadata['author'] = author
                    bibtex = lib_dict[key]
                    bibtex = bibtexparser.Library(bibtex)
                    bibtex = bibtexparser.write_string(bibtex)
                    bibtex = bibtex.replace('\n' + 18*' ', ' ')
                    metadata['bibtex'] = bibtex
                    if 'doi' in lib_dict[key].fields_dict:
                        metadata['doi'] = lib_dict[key]['doi']
        f_out.write(json.dumps(publications, indent=4))


def runs_df():
    tables = read_tables()
    return pd.DataFrame(tables)


def participants_df():
    tables = read_tables(_type='participants')
    return pd.DataFrame(tables).drop_duplicates()


def publications_df():
    with open('./json/publications.json') as f_in:
        publications = json.loads(f_in.read())
    df_data = []
    for trec, tracks in publications.items():
        for track, pubs in tracks.items():
            for bibkey, fields in pubs.items():
                metadata = {'trec': trec, 'track': track}
                metadata.update(fields)
                df_data.append(metadata)
    return pd.DataFrame(df_data)


def tracks_df():
    with open('./json/tracks.json') as f_in:
        tracks = json.loads(f_in.read())
    df_data = []
    for trec, track in tracks.items():
        for track_id, fields in track.items():
            _fields = {'trec': trec, 'track': track_id}
            tasks = fields.get('tasks')
            if type(tasks) == dict:
                fields['tasks'] = json.dumps(tasks)
            _fields.update(fields)
            df_data.append(_fields)
    return pd.DataFrame(df_data)


def datasets_df():
    with open('./json/datasets.json') as f_in:
        datasets = json.loads(f_in.read())    
    df_datasets = []
    for trec, tracks in datasets.items():
        for track_name, track_info in tracks.items():
            for field, val in track_info.items():
                if type(val) is dict:
                    track_info[field] = json.dumps(val).encode('utf8')
                if not len(val): 
                    track_info[field] = None
            df_datasets.append(
                {
                    'trec': trec,
                    'track': track_name,
                    'corpus': track_info.get('corpus'),
                    'topics': track_info.get('topics'),
                    'qrels': track_info.get('qrels'),
                    'ir_datasets': track_info.get('ir_datasets'),
                    'trec_webpage': track_info.get('trec_webpage'),
                    'other': track_info.get('other')
                }    
            )
    return pd.DataFrame(df_datasets)


def eval_type(file, trec, track):
    eval = 'trec_eval' 

    if (trec, track) == ('trec31', 'cast'):
        if 'lenient' in file: 
            eval = 'lenient' 
        if 'strict' in file:
            eval = 'strict' 

    if (trec, track) == ('trec31', 'deep'):
        if 'ndcg' in file:
            eval = 'ndcg' 

    if (trec, track) == ('trec30', 'podcast'):
        if '.QD.' in file:
            eval = 'QD'
        if '.QE.' in file:
            eval = 'QE'
        if '.QR.' in file:
            eval = 'QR'
        if '.QS.' in file:
            eval = 'QS'

    if (trec, track) == ('trec30', 'deep'):
        if 'passages-eval' in file:
            eval = 'passages-eval' 

    if (trec, track) == ('trec29', 'deep'):
        if 'passages-eval' in file:
            eval = 'passages-eval' 

    if (trec, track) == ('trec28', 'deep'):
        if 'passages-eval' in file:
            eval = 'passages-eval' 

    if (trec, track) == ('trec23', 'web'):
        if 'risk-rm-a0-gd' in file: 
            eval = 'risk-rm-a0-gd'
        if 'risk-rm-a0-nd' in file: 
            eval = 'risk-rm-a0-nd'
        if 'risk-rm-a5-gd' in file: 
            eval = 'risk-rm-a5-gd'
        if 'risk-rm-a5-nd' in file: 
            eval = 'risk-rm-a5-nd'
        if 'risk-terrier-a0-gd' in file: 
            eval = 'risk-terrier-a0-gd'
        if 'risk-terrier-a0-nd' in file: 
            eval = 'risk-terrier-a0-nd'
        if 'risk-terrier-a5-gd' in file: 
            eval = 'risk-terrier-a5-gd'
        if 'risk-terrier-a5-nd' in file: 
            eval = 'risk-terrier-a5-nd'
        if 'std-gd' in file: 
            eval = 'std-gd'
        if 'std-nd' in file: 
            eval = 'std-nd'

    if (trec, track) == ('trec23', 'microblog'):
        if 'adhoc' in file: 
            eval = 'adhoc' 
        if 'ttg' in file:
            eval = 'ttg' 

    if (trec, track) == ('trec22', 'web'):
        if 'risk-a0-gd' in file: 
            eval = 'risk-a0-gd' 
        if 'risk-a0-nd' in file: 
            eval = 'risk-a0-nd' 
        if 'risk-a1-gd' in file: 
            eval = 'risk-a1-gd'
        if 'risk-a1-nd' in file: 
            eval = 'risk-a1-nd' 
        if 'risk-a5-gd' in file: 
            eval = 'risk-a5-gd' 
        if 'risk-a5-nd' in file: 
            eval = 'risk-a5-nd' 
        if 'risk-a10-gd' in file: 
            eval = 'risk-a10-gd' 
        if 'risk-a10-nd' in file: 
            eval = 'risk-a10-nd'
        if 'std-nd' in file: 
            eval = 'std-nd'
        if 'std-gd' in file: 
            eval = 'std-gd'

    if (trec, track) == ('trec20', 'session'):
        if 'allsubtopics' in file: 
            eval = 'allsubtopics' 
        if 'lastquerysubtopics' in file:
            eval = 'lastquerysubtopics' 

    if (trec, track) == ('trec20', 'microblog'):
        if 'allrel' in file: 
            eval = 'allrel' 
        if 'highrel' in file:
            eval = 'highrel' 

    if (trec, track) == ('trec19', 'blog'):
        if 'baseline' in file: 
            eval = 'baseline' 
        if 'first' in file:
            eval = 'first' 
        if 'second' in file:
            eval = 'second'   

    if (trec, track) == ('trec19', 'chemical'):
        if 'full' in file: 
            eval = 'full' 
        if 'small' in file:
            eval = 'small' 

    if (trec, track) == ('trec18', 'blog'):
        if 'headline' in file: 
            eval = 'headline' 
        if 'first' in file:
            eval = 'first' 
        if 'second' in file:
            eval = 'second'         
        if 'none' in file:
            eval = 'none' 

    if (trec, track) == ('trec18', 'legal'):
        if 'eval' in file: 
            eval = 'eval' 
        if 'evalH' in file:
            eval = 'evalH' 

    if (trec, track) == ('trec18', 'chemical'):
        if 'full' in file: 
            eval = 'full' 
        if 'small' in file:
            eval = 'small' 
        if 'eval' in file:
            eval = 'eval' 

    if (trec, track) == ('trec17', 'enterprise'):
        if 'document' in file: 
            eval = 'document' 
        if 'expert' in file:
            eval = 'expert' 

    if (trec, track) == ('trec17', 'blog'):
        if 'feed' in file: 
            eval = 'feed' 
        if 'opinion' in file:
            eval = 'opinion' 
        if 'positive' in file:
            eval = 'positive'    
        if 'negative' in file:
            eval = 'negative'         
        if 'topicrel' in file:
            eval = 'topicrel' 

    if (trec, track) == ('trec17', 'legal'):
        if 'adhoc' in file: 
            eval = 'adhoc' 
        if 'adhocH' in file:
            eval = 'adhocH' 
        if 'resid' in file:
            eval = 'resid'    
        if 'residH' in file:
            eval = 'residH'   

    if (trec, track) == ('trec16', 'blog'):
        if 'feed' in file: 
            eval = 'feed' 
        if 'opinion' in file:
            eval = 'opinion' 
        if 'polarity' in file:
            eval = 'polarity'         
        if 'topicrel' in file:
            eval = 'topicrel' 

    if (trec, track) == ('trec16', 'enterprise'):
        if 'doc-promotion' in file:
            eval = 'doc-promotion'
        if 'doc-residual' in file:
            eval = 'doc-residual'
        if 'document' in file:
            eval = 'document'
        if 'experts' in file:
            eval = 'experts'
    
    if (trec, track) == ('trec15', 'blog'):
        if 'opinion' in file:
            eval = 'opinion'        
        if 'topicrel' in file:
            eval = 'topicrel' 

    if (trec, track) in [
        ('trec29', 'pm'),
        ('trec28', 'pm'),
        ('trec27', 'pm'),
        ('trec26', 'pm'),
        ('trec25', 'clinical'),
        ('trec24', 'clinical'),
        ('trec23', 'clinical'),
        ('trec21', 'medical'),
    ]:
        if 'sample-eval' in file: 
            eval = 'sample-eval' 
        if 'evidence' in file: 
            eval = 'evidence-eval' 

    if (trec, track) in [
        ('trec21', 'web'),
        ('trec20', 'web'),
        ('trec19', 'web'),
    ]:
        if 'gdeval' in file: 
            eval = 'gdeval' 
        if 'ndeval' in file:
            eval = 'ndeval' 

    return eval


def track_measures(eval):
    if eval == 'sample-eval':
        return sample_eval_measures
    return trec_eval_measures


def strip_file_name(runid):
    runid = runid.split('/')[-1]
    affixes = summary_prefixes + summary_suffixes
    for affix in affixes:
        runid = runid.replace(affix, '')
    return runid


def parse_summary_misinfo(data_df, file, lines, trec, track):
    eval = eval_type(file, trec, track)
    runid = strip_file_name(file)
    summary = ''
    for line in lines:
        s = line.strip('\n').split('\t')
        if len(s) == 5:
            qrels = s[1]
            measure = s[2].strip().strip('\t')
            topic = s[3]
            score = s[4]
            _measures = ['P_10', 'ndcg', 'compatibility']
            if measure in _measures and topic == 'all':
                data_df.append(
                    {
                        'trec': trec,
                        'track': track,
                        'runid': runid,
                        'eval': eval,
                        'measure': ''.join([measure, ' (', qrels, ')']),
                        'topic': topic,
                        'score': score
                    }
                )
                summary += '\t' + line
    if len(summary) > 0:
        data_df.append(
                {
                    'trec': trec,
                    'track': track,
                    'runid': runid,
                    'eval': eval,
                    'measure': 'summary',
                    'topic': topic,
                    'score': summary
                }
            )
    return data_df


def parse_summary_session(data_df, file, lines, trec, track):
    runid = strip_file_name(file)
    if trec == 'trec20':
        et = eval_type(file, trec, track)
        for line in lines:
            s = line.split()
            if s[1].strip('\t') == 'all':
                summary = ''    
                eval_suffix = ''.join(['[', et, ']'])
                eval = ' '.join([s[0].strip('.'), eval_suffix])
                err = s[2]
                ndcg = s[6]
                map = s[8]
                evaluation_measures = [('err', 3, err), ('ndcg', 2, ndcg), ('map', 3,map)]
                for em in evaluation_measures:         
                    summary += ''.join(['\t', em[0], em[1]*'\t', 'all ', em[2], '\n'])
                    data_df.append(
                        {
                            'trec': trec,
                            'track': track,
                            'runid': runid,
                            'eval': eval,
                            'measure': em[0],
                            'topic': 'all',
                            'score': em[2]
                        }
                    )
                data_df.append(
                    {
                        'trec': trec,
                        'track': track,
                        'runid': runid,
                        'eval': eval,
                        'measure': 'summary',
                        'topic': 'all',
                        'score': summary
                    }
                )
        return data_df

    else:
        for line in lines:
            s = line.split()
            if s[0] == 'all':
                map_rl1 = s[1] # map
                map_rl2 = s[2] # map
                map_rl3 = s[3] # map
                err_rl1 = s[4] # err
                err_rl2 = s[5] # err
                err_rl3 = s[6] # err
                ndcg_rl1 = s[10] # ndcg
                ndcg_rl2 = s[11] # ndcg
                ndcg_rl3 = s[12] # ndcg
                p_at_k_rl1 = s[22] # P_k
                p_at_k_rl2 = s[23] # P_k
                p_at_k_rl3 = s[24] # P_k
                evals = ['RL1', 'RL2', 'RL3']

                if trec == 'trec21':
                    map_rl1 = s[1] # map
                    map_rl2 = s[2] # map
                    map_rl3 = s[3] # map
                    map_rl4 = s[4] # map
                    err_rl1 = s[5] # err
                    err_rl2 = s[6] # err
                    err_rl3 = s[7] # err
                    err_rl4 = s[8] # err
                    ndcg_rl1 = s[13] # ndcg
                    ndcg_rl2 = s[14] # ndcg
                    ndcg_rl3 = s[15] # ndcg
                    ndcg_rl4 = s[16] # ndcg
                    p_at_k_rl1 = s[29] # P_k
                    p_at_k_rl2 = s[30] # P_k
                    p_at_k_rl3 = s[31] # P_k
                    p_at_k_rl4 = s[32] # P_k
                    evals = ['RL1', 'RL2', 'RL3', 'RL4']

        for eval in evals:
            summary = ''
            if eval == 'RL1':
                evaluation_measures = [('map', 3, map_rl1), ('err', 3, err_rl1), ('ndcg', 2, ndcg_rl1), ('P_k', 3, p_at_k_rl1)]
            if eval == 'RL2':
                evaluation_measures = [('map', 3, map_rl2), ('err', 3, err_rl2), ('ndcg', 2, ndcg_rl2), ('P_k', 3, p_at_k_rl2)]
            if eval == 'RL3':
                evaluation_measures = [('map', 3, map_rl3), ('err', 3, err_rl3), ('ndcg', 2, ndcg_rl3), ('P_k', 3, p_at_k_rl3)]
            if eval == 'RL4':
                evaluation_measures = [('map', 3, map_rl4), ('err', 3, err_rl4), ('ndcg', 2, ndcg_rl4), ('P_k', 3, p_at_k_rl4)]
            for em in evaluation_measures:
                summary += ''.join(['\t', em[0], em[1]*'\t', 'all ', em[2], '\n'])
                data_df.append(
                    {
                        'trec': trec,
                        'track': track,
                        'runid': runid,
                        'eval': eval,
                        'measure': em[0],
                        'topic': 'all',
                        'score': em[2]
                    }
                )
            data_df.append(
                {
                    'trec': trec,
                    'track': track,
                    'runid': runid,
                    'eval': eval,
                    'measure': 'summary',
                    'topic': 'all',
                    'score': summary
                }
            )
        return data_df


def get_evaluation_measures(trec, track, lines, file, file_path, measures, eval):

    if (trec, track) in old_summary or \
        track == 'web' and trec in ['trec10', 'trec11', 'trec12'] and len(lines) > 308:
        results_all_topics = []
        cnt = 0
        for line in lines:
            if 'Queryid (Num):       all' in line or \
                'Queryid (Num):       39topics' in line or \
                    'Queryid (Num):       43topics' in line or \
                        'Queryid (Num):       45topics' in line or \
                            'Queryid (Num):       50topics' in line:
                cnt = 31
            if cnt: 
                results_all_topics.append(line)
                cnt -= 1
        P_10 = results_all_topics[22].split(':')[1].strip()
        P_100 = results_all_topics[25].split(':')[1].strip()
        P_1000 = results_all_topics[28].split(':')[1].strip()
        Rprec = results_all_topics[30].split(':')[1].strip()
        map = results_all_topics[18].strip()
        return [
            ('P_10', 2, P_10),
            ('P_100', 2, P_100),
            ('P_1000', 2, P_1000),
            ('Rprec', 2, Rprec),
            ('map', 3, map)
        ]
    
    if track == 'web':
        if trec in ['trec10', 'trec11', 'trec12']:
            for line in lines:
                    if 'reciprocal rank' in line:
                        mrr = line.split(':')[-1].strip()
            return [('mrr', 3, mrr)]
        
        if trec != 'trec13' and eval != 'trec_eval': 
            if eval in [
                'gdeval', 
                'risk-a0-gd',
                'risk-a1-gd', 
                'risk-a5-gd', 
                'risk-a10-gd', 
                'risk-rm-a0-gd',
                'risk-terrier-a0-gd',
                'risk-rm-a5-gd',
                'risk-terrier-a5-gd',
                'std-gd',
                ]:
                df = pd.read_csv(file_path)
                ndcg = df[df.topic == 'amean']['ndcg@20'].iloc[0]
                err = df[df.topic == 'amean']['err@20'].iloc[0]
                return [
                    ('err', 3, str(err)), 
                    ('ndcg', 2, str(ndcg))
                    ]
            
            if eval in [
                'ndeval', 
                'risk-a0-nd', 
                'risk-a1-nd', 
                'risk-a5-nd', 
                'risk-a10-nd', 
                'risk-rm-a0-nd',
                'risk-terrier-a0-nd',
                'risk-rm-a5-nd',
                'risk-terrier-a5-nd',
                'std-nd', 
                ]:
                df = pd.read_csv(file_path)
                err_ia = df[df.topic == 'amean']['ERR-IA@10'].iloc[0]
                alpha_ndcg = df[df.topic == 'amean']['alpha-nDCG@10'].iloc[0]
                p_ia = df[df.topic == 'amean']['P-IA@10'].iloc[0]
                map_ia = df[df.topic == 'amean']['MAP-IA'].iloc[0]
                return [
                    ('ERR-IA@10', 2, str(err_ia)), 
                    ('alpha-nDCG@10', 1, str(alpha_ndcg)), 
                    ('P-IA@10', 3, str(p_ia)), 
                    ('MAP-IA', 3, str(map_ia))
                    ]
        
    if track == 'novelty' and trec in ['trec11', 'trec12', 'trec13']:
        if trec == 'trec11':
            precision_relevant = lines[56].strip().split(':')[1].strip()
            recall_relevant = lines[57].strip().split(':')[1].strip()
            f_score_relevant = lines[58].strip().split(':')[1].strip()

            precision_new = lines[170].strip().split(':')[1].strip()
            recall_new = lines[171].strip().split(':')[1].strip()
            f_score_new = lines[172].strip().split(':')[1].strip()

            return [
                ('Precision (relevant sentences)', 2, precision_relevant),
                ('Recall (relevant sentences)', 3, recall_relevant),
                ('F-score (relevant sentences)', 2, f_score_relevant),
                ('Precision (new sentences)', 3, precision_new),
                ('Recall (new sentences)', 4, recall_new),
                ('F-score (new sentences)', 4, f_score_new)
            ]

        if trec in ['trec12', 'trec13']:
            if len(lines) > 64:
                precision_relevant = lines[57].strip().split(':')[1].strip()
                recall_relevant = lines[58].strip().split(':')[1].strip()
                f_score_relevant = lines[59].strip().split(':')[1].strip()

                precision_new = lines[119].strip().split(':')[1].strip()
                recall_new = lines[120].strip().split(':')[1].strip()
                f_score_new = lines[121].strip().split(':')[1].strip()

                return [
                    ('Precision (relevant sentences)', 2, precision_relevant),
                    ('Recall (relevant sentences)', 3, recall_relevant),
                    ('F-score (relevant sentences)', 2, f_score_relevant),
                    ('Precision (new sentences)', 3, precision_new),
                    ('Recall (new sentences)', 4, recall_new),
                    ('F-score (new sentences)', 4, f_score_new)
                ]
            else:
                precision_new = lines[57].strip().split(':')[1].strip()
                recall_new = lines[58].strip().split(':')[1].strip()
                f_score_new = lines[59].strip().split(':')[1].strip()

                return [
                    ('Precision (new sentences)', 3, precision_new),
                    ('Recall (new sentences)', 4, recall_new),
                    ('F-score (new sentences)', 4, f_score_new)
                ]

    if track == 'enterprise' and trec == 'trec17':
        if eval != 'expert':
            for line in lines:
                s = line.split()
                if len(s) > 2:
                    if s[0] == 'infNDCG' and s[1] == 'all':
                        infNDCG =  s[2]
                    if s[0] == 'infAP' and s[1] == 'all':
                        infAP =  s[2]
            return [
                ('infNDCG', 2, infNDCG),
                ('infAP', 2, infAP)
            ]

    if track == 'task' and trec in ['trec25', 'trec26']:
        if trec == 'trec26':
            df = pd.read_csv(file_path)
            err_10 = str(df[df['topic'] == 'amean'].iloc[0]['ERR-IA@10'])
            ndcg_10 = str(df[df['topic'] == 'amean'].iloc[0]['alpha-nDCG@10'])
        if trec == 'trec25':
            for line in lines:
                s = line.split()
                if s[0].strip('\t') == 'ERR-IA@10' and s[1] == 'all':
                    err_10 = s[2]
                if s[0].strip('\t') == 'alpha-nDCG@10' and s[1] == 'all':
                    ndcg_10 = s[2]
        return [
            ('ERR-IA@10', 2, err_10),
            ('alpha-nDCG@10', 1, ndcg_10)
        ]

    if track == 'microblog' and trec in ['trec23', 'trec24']:
        if eval != 'adhoc':
            if trec == 'trec23':
                for line in lines:
                    s = line.split()
                    if s[1] == 'all':
                        unweighted_recall = s[2]
                        weighted_recall = s[3]
                        precision = s[4]

                return [
                    ('unweighted_recall', 2, unweighted_recall),
                    ('weighted_recall', 3, weighted_recall),
                    ('precision', 4, precision),
                ]
            if trec == 'trec24':
                for line in lines:
                    s = line.split()
                    if len(s) == 3:
                        if s[1].strip('\t') == 'all':
                            ndcg = s[2]
                            return [
                                ('nDCG', 2, ndcg),
                            ]
                    if len(s) == 4: 
                        if s[1].strip('\t') == 'all':
                            elg = s[2]
                            ncg = s[3]
                            return [
                                ('ELG', 2, elg),
                                ('nCG', 2, ncg),
                            ]

    if track == 'hp' and trec in ['trec6', 'trec7']:
        if trec == 'trec6':
            _all_str = 'Queryid (Num):	all'
        if trec == 'trec7':
            _all_str = 'Queryid (Num):       all'
        idx = 0
        for line in lines:
            if _all_str in line:
                break
            else:
                idx += 1
        P = lines[idx+5].split()[-1]
        RP = lines[idx+6].split()[-1]
        AP = lines[idx+7].split()[-1]
        if trec == 'trec6':
            return [
                ('Precision@10', 4, P),
                ('Relative Precision@10', 2, RP),
                ('Unranked Avg. Precision@10', 1, AP),
            ]        
        if trec == 'trec7':
            return [
                ('Precision@15', 4, P),
                ('Relative Precision@15', 2, RP),
                ('Unranked Avg. Precision@15', 1, AP),
            ]

    if track == 'genomics' and trec in ['trec14', 'trec15', 'trec16'] :
        if trec == 'trec14' and len(lines) < 13: # otherwise it's the summary of the categorization task
            _evaluation_measures = []
            for line in lines:
                s = line.split()
                if len(s) > 1:
                    if s[0] in ['Precision:', 'Recall:', 'F-score:']:
                        measure = s[0].strip(':')
                        score = s[1]
                        tabs = 2 
                        if measure == 'Precision':
                            tabs = 1
                        _evaluation_measures.append((measure, tabs, score))
            return _evaluation_measures
        
        if trec in ['trec16', 'trec15']:
            _evaluation_measures = []
            for line in lines:
                s = line.split()
                if s[2] == 'MAP':
                    measure = ' '.join([s[2], ''.join(['(', s[1], ')'])])
                    score = s[3]
                    _evaluation_measures.append((measure, 2, score))
            return _evaluation_measures

    _evaluation_measures = []
    for line in lines:
        s = line.strip('\n').split('\t')
        if eval == 'sample-eval':
            s = line.split()
        if len(s) > 1:
            measure = s[0].strip().strip('\t')
            topic = s[1]
            score = s[2]
            if measure == 'P10':
                measure = 'P_10'
            if measure == 'P100':
                measure = 'P_100'
            if measure == 'P1000':
                measure = 'P_1000'
            if measure in measures and topic == 'all':
                tabs = 3
                if measure == 'map':
                    tabs = 4
                elif measure in ['recip_rank', 'ndcg_cut_10', 'recall_10', 'recall_100', 'recall_1000']:
                    tabs = 2 
                elif measure in ['ndcg_cut_100', 'ndcg_cut_1000']:
                    tabs = 1 
                _evaluation_measures.append((measure, tabs, score))
    return _evaluation_measures


def parse_summary(data_df, file, lines, trec, track, file_path):
    if track == 'misinfo':
        return parse_summary_misinfo(data_df, file, lines, trec, track)
    if track == 'session':
        return parse_summary_session(data_df, file, lines, trec, track)
    eval = eval_type(file, trec, track)
    measures = track_measures(eval)
    runid = strip_file_name(file)
    summary = ''
    evaluation_measures = get_evaluation_measures(trec, track, lines, file, file_path, measures, eval)
    for em in evaluation_measures:
        summary += ''.join(['\t', em[0], em[1]*'\t', 'all\t', em[2], '\n'])
        data_df.append(
            {
                'trec': trec,
                'track': track,
                'runid': runid,
                'eval': eval,
                'measure': em[0],
                'topic': 'all',
                'score': em[2]
            }
        )
    if len(summary) > 0:
        data_df.append(
            {
                'trec': trec,
                'track': track,
                'runid': runid,
                'eval': eval,
                'measure': 'summary',
                'topic': 'all',
                'score': summary
            }
        )
    return data_df


def parse_summary_covid(data_df, trec, tracks):
    for track in tracks[tracks['trec'] == trec].track:
        if track == 'round1':
            bpref_df = pd.read_csv('./trec/trec-covid/{}/eval/means-bpref'.format(track), sep=' ', names=['runid', 'bpref'])
            map_df = pd.read_csv('./trec/trec-covid/{}/eval/means-map'.format(track), sep=' ', names=['runid', 'map'])
            ndcg_df = pd.read_csv('./trec/trec-covid/{}/eval/means-ndcg'.format(track), sep=' ', names=['runid', 'ndcg'])
            P5_df = pd.read_csv('./trec/trec-covid/{}/eval/means-P5'.format(track), sep=' ', names=['runid', 'P_5'])
            results = bpref_df
            for df in [map_df, ndcg_df, P5_df]:
                results = pd.merge(left=results, right=df, left_on='runid', right_on='runid')
        if track in ['round2', 'round3']:
            bpref_df = pd.read_csv('./trec/trec-covid/{}/eval/means-bpref'.format(track), sep=' ', names=['runid', 'bpref'])
            map_df = pd.read_csv('./trec/trec-covid/{}/eval/means-map'.format(track), sep=' ', names=['runid', 'map'])
            ndcg_df = pd.read_csv('./trec/trec-covid/{}/eval/means-ndcg'.format(track), sep=' ', names=['runid', 'ndcg'])
            P5_df = pd.read_csv('./trec/trec-covid/{}/eval/means-P5'.format(track), sep=' ', names=['runid', 'P_5'])
            rbp_p5_df = pd.read_csv('./trec/trec-covid/{}/eval/means-rbp_p5'.format(track), sep=' ', names=['runid', 'rbp_p5'])
            results = bpref_df
            for df in [map_df, ndcg_df, P5_df, rbp_p5_df]:
                results = pd.merge(left=results, right=df, left_on='runid', right_on='runid')
        if track in ['round4', 'round5']:
            bpref_df = pd.read_csv('./trec/trec-covid/{}/eval/mean-bpref'.format(track), sep=' ', names=['runid', 'bpref'])
            map_df = pd.read_csv('./trec/trec-covid/{}/eval/mean-map'.format(track), sep=' ', names=['runid', 'map'])
            ndcg_df = pd.read_csv('./trec/trec-covid/{}/eval/mean-ndcg20'.format(track), sep=' ', names=['runid', 'ndcg_20'])
            P5_df = pd.read_csv('./trec/trec-covid/{}/eval/mean-P20'.format(track), sep=' ', names=['runid', 'P_20'])
            rbp_p5_df = pd.read_csv('./trec/trec-covid/{}/eval/mean-rbp_p5'.format(track), sep=' ', names=['runid', 'rbp_p5'])
            results = bpref_df
            for df in [map_df, ndcg_df, P5_df, rbp_p5_df]:
                results = pd.merge(left=results, right=df, left_on='runid', right_on='runid')
        measures = list(results.columns[1:]) 
        for row in results.iterrows():
            summary = ''
            runid = row[1]['runid']
            for measure in measures:
                score = str(row[1][measure])
                tabs = 3 if measure in ['map', 'P_5'] else 2
                summary += ''.join(['\t', measure, tabs*'\t', 'all\t', score, '\n'])
                data_df.append(
                    {
                        'trec': trec,
                        'track': track,
                        'runid': runid,
                        'eval': 'trec_eval',
                        'measure': measure,
                        'topic': 'all',
                        'score': score
                    }
                )
            if len(summary) > 0:
                data_df.append(
                    {
                        'trec': trec,
                        'track': track,
                        'runid': runid,
                        'eval': 'trec_eval',
                        'measure': 'summary',
                        'topic': 'all',
                        'score': summary
                    }
                )
    return data_df


def results_df():
    data_df = []
    tracks = tracks_df()
    trecs = tracks.trec.unique()
    for trec in trecs:
        if trec == 'trec-covid': # "summary files" are different for TREC-COVID 
            data_df = parse_summary_covid(data_df, trec, tracks)
        _tracks = tracks[(tracks['trec'] == trec)].track.unique()
        for track in _tracks:
            if (trec, track) in no_summary + no_summary_parsing:
                continue
            summaries_path = os.path.join('trec', trec, track, 'summaries')
            if (trec, track) == ('trec28', 'cast'):
                summaries_path = os.path.join('trec', trec, 'converse', 'summaries')
            for root, dirs, files in os.walk(summaries_path):
                files.sort(key=str.lower)
                for file in files:
                    if file.endswith(('.tsv', '.csv', '.rbp', '.tar', '.gz', '.tgz', '.Z', '.pdf', '.eps', '.ps', '.DS_Store')):
                        continue
                    if 'trec_eval(2)' in file: # trec23/clinical
                        continue
                    if 'short' in file.split('.') or 'long' in file.split('.'):
                        continue
                    else:
                        try: 
                            file_path= os.path.join(root, file)
                            with open(file_path) as f_in:
                                lines = f_in.readlines()
                            data_df = parse_summary(data_df, file, lines, trec, track, file_path)
                        except Exception as e:
                            print(trec, track, file, e)
    return pd.DataFrame(data_df)


def add_tables(engine):
    table_names = ['tracks', 'runs', 'results', 'publications', 'participants', 'datasets']
    for tn in table_names:
        print(tn)
        if tn == 'runs':
            table = runs_df()
        if tn == 'participants':
            table = participants_df()
        if tn == 'publications':
            table = publications_df()
        if tn == 'tracks':
            table = tracks_df()
        if tn == 'datasets':
            table = datasets_df()    
        if tn == 'results':
            table = results_df()       
        table = table.replace(r'', np.nan, regex=True)
        table.to_sql(tn, engine, if_exists='replace')


def main():
    write_publications_json()
    sqlite_filepath = 'trec.sqlite'
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base = declarative_base()
    Base.metadata.drop_all(engine)
    add_tables(engine)


if __name__ == '__main__':
    main()
