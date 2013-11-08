import argparse
import itertools

from parsers import parse_files


#setting up the command line parser
parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('--files', type=str, metavar='Name', nargs='+', 
                       help='the name of the DNA file')

file_names = parser.parse_args().files

for file_name, parser in parse_files(file_names):
    print 'RESULTS FROM %s ==>' % file_name
    for seq in itertools.islice(parser, 0, 3):
        print 'META INFO ==> %s' % seq['meta']
        print 'Sequence ==> %s(...)' % ''.join(itertools.islice(seq['seq'], 0, 5))
    print "FOUND %s more sequences in %s" % (len(list(parser)[3:]), file_name)
