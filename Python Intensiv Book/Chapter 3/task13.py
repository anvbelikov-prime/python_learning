import collections
import operator

PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]

def format_sort_records(records):
    res = ''
    for record in records:
        res += f'{record[1]:10} {record[0]:10} {record[2]:5.2f}\n'
    return res

# print(format_sort_records(PEOPLE))

Person = collections.namedtuple('Person', ['first_name', 'last_name', 'duration'])

named_people = [
    Person(first_name='Donald', last_name='Trump', duration=7.85),
    Person(first_name='Vladimir', last_name='Putin', duration=3.626),
    Person(first_name='Jinping', last_name='Xi', duration=10.603),
    Person('Anthony', 'Edwards', 7.77)
]

def format_sort_records_v2(records):
    res = ''
    for record in records:
        res += f'{record.last_name:10} {record.first_name:10} {record.duration:5.2f}\n'
    return res

print(format_sort_records_v2(named_people))

films = [
    ('film_name1', 120.15, 'director_name3'),
    ('film_name2', 100.25, 'director_name7'),
    ('film_name3', 180.35, 'director_name5'),
    ('film_name4', 120.54, 'director_name1'),
    ('film_name5', 117.56, 'director_name3'),
    ('film_name6', 90.58,  'director_name5'),
    ('film_name7', 83.34,  'director_name2'),
]

def sort_films(films):
    field_names = {'name':0, 'duration':1, 'director':2}
    while True:
        input_keys = input('По каким полям сортировать: ')
        if input_keys == 'q':
            break
        else:
            keys_num = []
            keys = input_keys.split(',')
            for key in keys:
                keys_num.append(field_names[key])
            return sorted(films, key=operator.itemgetter(*keys_num))
        
# print(sort_films(films))
