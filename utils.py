from string import strip, split


def read_lines(file_name):
    with open(file_name, 'rt') as f: 
        for line in f:
            striped = line.decode('utf-8').strip()
            if striped:
                yield striped
                