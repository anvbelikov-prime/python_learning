import os

d = {'a': 1, 'b': 2, 'c': 3}

def revert_dict(d):
    return {v: k for k, v in d.items()}

# print(revert_dict(d))

s = 'this is an easy test'

def create_word_dict(s):
    return {word: len([w for w in word if w.lower() in 'aeiou']) for word in s.split()}

# print(create_word_dict(s))

def create_files_dict(path):
    return {name: os.stat(os.path.join(path, name)).st_size for name in os.listdir(path) if os.path.isfile(os.path.join(path, name)) and not name.startswith('.')}

# print(create_files_dict('.'))

config = [
    'param1=value1',
    'param2=value2',
    'param3=value3',
]

def create_config_dict(config):
    return {line.strip()[:line.strip().index('=')]: line.strip()[line.strip().index('=') + 1:] for line in config }

def create_config_dict_v2(config):
    return {line.strip().split('=')[0]: line.strip().split('=')[1] for line in config}

print(create_config_dict_v2(config))
