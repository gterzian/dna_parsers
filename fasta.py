from utils import read_lines, read_fasta_seqs
from itertools import imap, chain, ifilter
from string import split

ERRORS = dict(no_meta_info='No Meta Info Found', no_sequence='No Sequence Info Found')
EXCLUDE = ('#', '@', '*')

def process_lines(reader):
    for line in reader:  
        if ">" in line:
            yield True, line
        else:
            yield False, line
            
def filter_sequence(s):
    seq_str = ''.join(chain(s['seq']))
    s['seq'] = ifilter(lambda x: x not in EXCLUDE, seq_str)
    if not seq_str:
        s['errors'].append(ERRORS['no_sequence'])
    if not s['meta']:
        s['errors'].append(ERRORS['no_meta_info'])
    return s
    
create_seq_dict = lambda : dict(meta=None, seq=list(), errors=list())

def process_sequence(seq):
    lines = split(seq, '\n')
    data = create_seq_dict()
    data['meta'] = lines[0]
    data['seq'] = lines[1:]
    return data
    
def parse_fasta(file_name):
    seqs = read_fasta_seqs(file_name)
    seqs_data = imap(process_sequence, seqs)
    for clean_seq in imap(filter_sequence, seqs_data):
        yield clean_seq
           
    