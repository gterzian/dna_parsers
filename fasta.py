from utils import read_lines  


def process_file(reader):
    for line in reader:  
        if line[0] == ">":
            yield True, line[1:]
        else:
            yield False, line
           
def parse_fasta(file_name):
    reader = read_lines(file_name)
    seqs = []
    for new_seq, line in process_file(reader):
        if new_seq:
            d = dict(meta=None, seq=list(),)
            d['meta'] = line
            seqs.append(d)         
        else:      
            seqs[-1]['seq'].append(line)
    for s in seqs:
        yield s
    