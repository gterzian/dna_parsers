from utils import read_lines  
from itertools import imap, chain, ifilter


ERRORS = dict(no_meta_info='No Meta Info Found')
EXCLUDE = ('#', '@', '*')

def process_file(reader):
    for line in reader:  
        if ">" in line:
            yield True, line
        else:
            yield False, line
            
def process_seq(s):
    s['seq'] = ifilter(lambda x: x not in EXCLUDE, ''.join(chain(s['seq'])))
    return s
    
 
create_seq_dict = lambda : dict(meta=None, seq=list(), errors=list())
           
def parse_fasta(file_name):
    reader = read_lines(file_name)
    seqs = list()
    for new_seq, line in process_file(reader):
        if new_seq:
            seq = create_seq_dict()
            seq['meta'] = line[1:]
            seqs.append(seq)          
        else:
            try:      
                seqs[-1]['seq'].append(line)
            except IndexError:
                seq = create_seq_dict()
                seq['errors'].append(ERRORS['no_meta_info'])#note, this only catches a lack of meta for the first seq in the file  
                seq['seq'].append(line)
                seqs.append(seq)
    for s in imap(process_seq, seqs):
        yield s
    