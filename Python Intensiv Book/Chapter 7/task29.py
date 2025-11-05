def sum_numbers():
    seq = input("Введите элементы: ")
    return sum(int(i) for i in seq.split() if i.isdigit())

# print(sum_numbers())

lines = [
    'xzzzzzzzzzz zzz zzzzzzzz',
    'abv',
    'iugjhj;l/kg',
    'ldkfjsldk'
]

def show_lines(lines):
    return [line for line in lines if len(line) > 20 and len(list(filter(lambda w: w.lower() in 'aeiou', line))) >= 1]

# print(show_lines(lines))

phone_numbers = [
    '123-444-1234',
    '123-567-9999',
    '123-777-5555'
]

def increment_codes(seq):
    return [phone for phone in seq if not phone.split('-')[1].startswith(tuple(str(i) for i in range(0, 6)))] + \
        ['-'.join((str(int(phone.split('-')[0]) + 1), phone.split('-')[1], phone.split('-')[2])) for phone in seq if phone.split('-')[1].startswith(tuple(str(i) for i in range(0, 6)))]

# print(increment_codes(phone_numbers))

people = [
    {'name': 'John1', 'age': 15},
    {'name': 'John2', 'age': 25},
    {'name': 'John3', 'age': 10},
    {'name': 'John4', 'age': 5},
    {'name': 'John5', 'age': 20},
]

def dicts_with_months(lst_dicts):
    return [{'name': d['name'], 'age': d['age'], 'age_in_months': d['age'] * 12} for d in lst_dicts if d['age'] <= 20]

print(dicts_with_months(people))
