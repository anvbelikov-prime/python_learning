PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603),
]

def format_sort_records(lst):
    res = ''
    for r in lst:
        res += (f'{r[1]:<10} {r[0]:<10} {r[2]:5.2f}\n')
    return res

print(format_sort_records(PEOPLE))
