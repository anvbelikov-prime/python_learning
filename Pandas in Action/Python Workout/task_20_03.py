import collections
import os

def letter_count(dir_path='.'):
    res = collections.Counter('')
    for file in [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]:
        with open(os.path.join(dir_path, file), 'r') as f:
            count = collections.Counter([c for line in f for c in line.strip() if c.isalpha()])
        res += count
    return res

print(letter_count())
print(letter_count().most_common(5))
