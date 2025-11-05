import collections

President = collections.namedtuple('President', ['first', 'last', 'duration'])

PEOPLE = [
    President('Donald', 'Trump', 7.85),
    President('Vladimir', 'Putin', 3.626),
    President('Jinping', 'Xi', 10.603),
]

def format_sort_records(lst):
    res = ''
    for r in lst:
        res += (f'{r.last:<10} {r.first:<10} {r.duration:5.2f}\n')
    return res

print(format_sort_records(PEOPLE))
