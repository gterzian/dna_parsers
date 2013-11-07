import argparse

from parsers import parse_file


#setting up the command line parser
parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('--files', type=str, metavar='Names', nargs='+', 
                       help='the name of the subtitle files, without comma separation but within single brackets')

file_name = parser.parse_args().files[0]
for seq in parse_file(file_name):
    print 'META INFO ==> %s' % seq['meta']
    print 'Sequence ==> %s ...' %  seq['seq']
