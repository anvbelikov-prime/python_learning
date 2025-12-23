import collections

def file_stats():
    file_name, *words = input('Введите имя файла и слова: ').strip().split()
    with open(file_name, 'r') as f:
        full_stat = collections.Counter([word.lower() for line in f for word in line.strip().split()])
    user_stat = {}
    for word in words:
        if word in full_stat:
            user_stat[word] = full_stat[word]
        else:
            user_stat[word] = 0
    return user_stat

print(file_stats())
