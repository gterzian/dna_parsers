import argparse
from itertools import islice

from parsers import parse_files


#setting up the command line parser
arg_parser = argparse.ArgumentParser(description='Process some files.')
arg_parser.add_argument('--files', type=str, metavar='Name', nargs='+', 
                       help='the name of the DNA file')

file_names = arg_parser.parse_args().files

for file_name, parser in parse_files(file_names):
    print 
    print 'FIRST 3 RESULTS FROM %s ==>' % file_name
    print
    for seq in parser:
        print 'META INFO ==> %s' % seq['meta']
        print 'Sequence ==> %s(...)' % ''.join(seq['seq'])
        if seq['errors']:
            print 'PARSING ERRORS ==> %s' % ', '.join(seq['errors'])
        print
    print "FOUND %s more sequences in %s" % (len(list(parser)[3:]), file_name)
