import operator

PEOPLE = [
    {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
    {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'},
    {'first': 'Anton', 'last': 'Belikov', 'email': 'anvbelikov@yandex.ru'},
]

def alphabetize_names(lst):
    return sorted(lst, key=operator.itemgetter('last', 'first'))

print(PEOPLE)
print(alphabetize_names(PEOPLE))
