from itertools import imap, chain, ifilter

ERRORS = dict(no_meta_info='No Meta Info Found', 
                  no_sequence='No Sequence Info Found', 
                  meta_contains_dna='The Meta Info Seems to Include DNA')
EXCLUDE = ('#', '@', '*')
DNA = ('G', 'C', 'A', 'T')

def read_fasta_seqs(file_name):
    with open(file_name, 'rt') as f: 
        seqs = f.read().split('>')
        for sequence in seqs:
            yield sequence

def filter_sequence(s):
    seq_str = ''.join(chain(s['seq']))
    s['seq'] = ifilter(lambda x: x not in EXCLUDE, seq_str)
    if not seq_str:
        s['errors'].append(ERRORS['no_sequence'])
    if not s['meta']:
        s['errors'].append(ERRORS['no_meta_info'])
    if [i for i in s['meta'] if i in DNA]:
        s['errors'].append(ERRORS['meta_contains_dna'])
    return s

def process_sequence(seq):
    lines =  seq.split('\n')
    if len(lines) == 1:
        lines = seq.split('\r')
    data = dict(meta=None, seq=list(), errors=list())
    data['meta'] = lines[0]
    data['seq'] = lines[1:]
    return data
    
def parse_fasta(file_name):
    seqs = read_fasta_seqs(file_name)
    seq_data = imap(process_sequence, seqs)
    for clean_seq in imap(filter_sequence, seq_data):
        yield clean_seq
           
    