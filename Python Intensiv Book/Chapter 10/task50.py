import os

def my_chain(*args):
    for arg in args:
        for e in arg:
            yield e

def my_chain_v2(*args):
    return (e for arg in args for e in arg)

# for e in my_chain('abc', [1, 2, 3], {'e': 1, 'f': 2, 'g': 3}, {4, 5, 6}):
#     print(e)

# print('-' * 50)

# for e in my_chain_v2('abc', [1, 2, 3], {'e': 1, 'f': 2, 'g': 3}, {4, 5, 6}):
#     print(e)

def my_zip(*args):
    for i in range(len(min(args, key=len))):
        yield tuple(arg[i] for arg in args)

# for t in my_zip([1, 2, 3], ['a', 'b', 'c'], range(0, 15)):
#     print(t)

def all_files_reader(path):
    return my_chain(*(open(os.path.join(dir_tuple[0], file), 'r') for dir_tuple in os.walk(path) for file in dir_tuple[2] if not file.startswith('.')))

# for line in all_files_reader('.'):
#     print(line.strip())

def my_range(start, end, step=1):
    idx = start
    while idx < end:
        yield idx
        idx += step

for i in my_range(0, 11, 2):
    print(i) 
