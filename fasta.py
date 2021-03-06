from itertools import imap

ERRORS = dict(no_meta_info='No Meta Info Found', 
                  no_sequence='No Sequence Info Found', 
                  meta_contains_dna='The Meta Info Seems to Include DNA: ')
EXCLUDE = ('#', '@', '*')
DNA = ('G', 'C', 'A', 'T')

def read_fasta_seqs(file_name):
    with open(file_name, 'rt') as f: 
        seqs = f.read().split('>')
        for sequence in seqs:
            yield sequence

def check_errors(s):
    if not s['seq']:
        s['errors'].append(ERRORS['no_sequence'])
    if not s['meta']:
        s['errors'].append(ERRORS['no_meta_info'])
    dna = [i for i in s['meta'] if i in DNA]
    if dna:
        s['errors'].append(''.join(ERRORS['meta_contains_dna']) + ''.join(dna))
    return s

def check_sequence(s):
    strange = [char for char in EXCLUDE for line in s['seq'] if char in line]            
    if strange:
        s['errors'].append('unknown characters found: %s' % ', '.join(strange))
    return s

def process_sequence(seq):
    lines =  seq.split('\n')
    if len(lines) == 1:
        lines = seq.split('\r')
    data = dict(meta=None, seq=list(), errors=list())
    data['meta'] = lines[0]
    data['seq'] = [l for l in lines[1:] if l]#remove empty lines
    return data
    
def parse_fasta(file_name):
    seqs = read_fasta_seqs(file_name)
    seq_data = imap(process_sequence, seqs)
    checked_data = imap(check_errors, seq_data)
    for seq in imap(check_sequence, checked_data):
        yield seq
           
    