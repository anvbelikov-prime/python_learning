from collections import defaultdict

def safe_int(s):
    try:
        return int(s)
    except:
        return 0

def get_rainfall():
    cities = defaultdict(list)
    while True:
        city = input("Введите город: ")
        if city == '':
            break
        else:
            rain = safe_int(input("Введите кол-во осадков: "))
            cities[city].append(rain)
    for k, v in sorted(cities.items(), key=lambda i: sum(i[1]), reverse=True):
        print(f"{k}: всего {sum(v)} мм осадков, в среднем {sum(v)/len(v) if len(v) else ''}")

# get_rainfall()

def word_stats(file_path):
    stats = defaultdict(int)
    with open(file_path, 'r') as f:
        for line in f:
            for w in line.strip().split():
                stats[len(w)] += 1
    return stats

print(word_stats("text.txt"))
print(word_stats("text2.txt"))