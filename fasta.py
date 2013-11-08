from utils import read_lines  
from itertools import imap, chain, ifilter


def process_file(reader):
    for line in reader:  
        if line[0] == ">":
            yield True, line[1:]
        else:
            yield False, line
            
def process_seq(s):
    exclude = ['#', '@', '*']
    s['seq'] = ifilter(lambda x: x not in exclude, ''.join(chain(s['seq'])))
    return s
           
def parse_fasta(file_name):
    reader = read_lines(file_name)
    seqs = []
    for new_seq, line in process_file(reader):
        if new_seq:
            d = dict(meta=None, seq=list(),)
            d['meta'] = line
            seqs.append(d)         
        else:      
            seqs[-1]['seq'].append(line.strip())
    for s in imap(process_seq, seqs):
        yield s
    