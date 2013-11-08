from utils import read_lines  
from itertools import imap, chain, ifilter
from collections import namedtuple


ERRORS = dict(no_meta_info='No Meta Info Found')
EXCLUDE = ['#', '@', '*']

def process_file(reader):
    for line in reader:  
        if ">" in line:
            yield True, line
        else:
            yield False, line
            
def process_seq(s):
    s['seq'] = ifilter(lambda x: x not in EXCLUDE, ''.join(chain(s['seq'])))
    return s
           
def parse_fasta(file_name):
    reader = read_lines(file_name)
    seqs = list()
    for new_seq, line in process_file(reader):
        if new_seq:
            d = dict(meta=None, seq=list(), errors=list())
            d['meta'] = line[1:]
            seqs.append(d)         
        else:
            try:      
                seqs[-1]['seq'].append(line.strip())
            except IndexError:
                d = dict(meta=None, seq=list(), errors=list())
                d['errors'].append(ERRORS['no_meta_info'])
                seqs.append(d)
                seqs[-1]['seq'].append(line.strip())
    for s in imap(process_seq, seqs):
        yield s
    