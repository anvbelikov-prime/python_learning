import string

def gematria_create_letter_dict():
    return {w: i for i, w in enumerate(string.ascii_lowercase, 1)}

gematria_dict = gematria_create_letter_dict()

def gematria_for(word):
    return sum(gematria_dict[w.lower()] for w in word if w.lower() in gematria_dict)

def gematria_equal_words(file_path, word):
    with open(file_path, 'r') as f:
        gematria = gematria_for(word.strip())
        return [eq_word.strip() for eq_word in f if gematria_for(eq_word.strip()) == gematria]

# print(gematria_equal_words('words.txt', 'cat'))

cities = {'city1':75.2, 'city2': 100, 'city3': 50.5, 'city4': 25.56, 'city5': 0}

def create_celcius_dict(cities):
    return {k: round((v - 32) * 5 / 9, 1) for k, v in cities.items()}

# print(create_celcius_dict(cities))

books = [
    ('Aashg Aakfjs', 'Skdjhfjbsd', 100.5),
    ('Adglkbmdgl Bsigl', 'LOskfjgn', 55.67),
    ('OJhdkjfgb Kjhdjhfgb', 'IYTFadjhbf', 25.99)
]

def create_book_dict(books):
    return {book[1]: {'name': book[0].split()[0], 'surname': book[0].split()[1], 'price': book[2]} for book in books}

# print(create_book_dict(books))

currencies = {
    'a': 1,
    'b': 10,
    'c': 15.5,
    'd': 100.25,
    'e': 0.5,
}

def recalc_currencies(currencies):
    cur = input('Введите вашу валюту: ')
    if cur not in currencies:
        print('Такой валюты нет в словаре!')
        return
    return {k: v / currencies[cur] for k, v in currencies.items()}

# print(recalc_currencies(currencies))

def create_book_dict_v2(books, currencies):
    cur = input('Введите вашу валюту: ')
    if cur not in currencies:
        print('Такой валюты нет в словаре!')
        return
    return {book[1]: {'name': book[0].split()[0], 'surname': book[0].split()[1], 'price': book[2] * currencies[cur]} for book in books}

print(create_book_dict_v2(books, currencies))
