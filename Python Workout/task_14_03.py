import datetime

family = {
    'Bob': datetime.date(2025, 5, 3),
    'Martha': datetime.date(1976, 10, 4),
    'John': datetime.date(1988, 3, 8),
}

def parse_date(s):
    return datetime.date.fromisoformat(s)

def get_diff_in_days(d1, d2):
    return (d2 - d1).days

def how_old():
    name = input('Enter name: ')
    if name in family:
        iso_date = input('Enter date (iso_format): ')
        print(f'{name} is {get_diff_in_days(family[name], parse_date(iso_date))} days old on {iso_date}!')
    else:
        print('No such person!')

how_old()
