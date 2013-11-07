from fasta import parse_fasta

'''note: use a data structure as context for the parsing code, allowing you to add some details as you come across them in the parsing and allowing for 
graceful exception handling. Either use a class with context management capabilities, or use a context manager function that would yield a named tuple and return
it with all info after parsing'''


exclude = ('A', 'G') 


def parse_file(file_name):
    name, ext = file_name.split('.')
    if ext == 'fasta':
        data = parse_fasta(file_name, exclude)
        return data
    else:
        raise(IOError("sorry no support for %s files yet" % ext))


                                        

