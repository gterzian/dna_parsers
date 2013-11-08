from fasta import parse_fasta


def parse_file(file_name):
    name, ext = file_name.split('.')
    if ext == 'fasta':
        data = parse_fasta(file_name)
        return data
    else:
        raise(IOError("sorry no support for %s files yet" % ext))


def parse_files(file_names):
    for name in file_names:
        yield name, parse_file(name)                                        

