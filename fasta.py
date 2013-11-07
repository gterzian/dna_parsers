from utils import sequence_data, read_lines    


def process_seq(gen, current_line):
    with sequence_data(meta=None, seq=list(), error=None) as d:
        d['meta'] = current_line[1:]
        next_line = next(gen)
        if next_line[0] == ">":
            process_seq(gen, next_line)
        else:
            d['seq'].append(next_line)
    yield d
  
def process_file(reader, filter):
    for line in reader:  
        if line[0] == ">":
            yield process_seq(reader, line)
           
def parse_fasta(file_name, exclude):
    reader = read_lines(file_name)
    sequences_processors = process_file(reader, exclude)
    for processor in sequences_processors:
        for seq in processor:
            yield seq