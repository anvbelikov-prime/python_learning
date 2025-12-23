import collections
import operator

Movie = collections.namedtuple('Movie', ['name', 'duration', 'director'])

MOVIES = [
    Movie('First', 100, 'A'),
    Movie('First', 120, 'B'),
    Movie('AA', 90, 'B'),
    Movie('BB', 15, 'C'),
    Movie('CC', 45, 'C'),
    Movie('DD', 190, 'D'),
]

name_to_index = {'name': 0, 'duration': 1, 'director': 2}

def sort_movies(movies):
    dimensions = input('Введите по чему сортировать: ')
    idx_tup = tuple((name_to_index[n] for n in dimensions.strip().split(',')))
    lst = sorted(movies, key=operator.itemgetter(*idx_tup))
    return '\n'.join(str(i) for i in lst)

print(sort_movies(MOVIES))
