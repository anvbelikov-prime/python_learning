import collections

def get_rainfall():
    stats = collections.defaultdict(list)
    while True:
        city = input('Enter city: ').strip()
        if city:
            rainfall = float(input('Enter rainfall: '))
            stats[city].append(rainfall)
        else:
            break
    for k in stats:
        print(f'City: {k}, total rainfall: {sum(stats[k])}, average rainfall: {sum(stats[k]) / len(stats[k])}')

get_rainfall()
