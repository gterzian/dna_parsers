from contextlib import contextmanager


@contextmanager
def sequence_data(**fields):
    data = dict(**fields)
    try:
        yield data
    except ValueError, e:
        data['error'] = e
             
def read_lines(file_name):
    with open(file_name, 'rt') as f: 
        for line in f:
            striped = line.decode('utf-8').strip()
            if striped:
                yield striped