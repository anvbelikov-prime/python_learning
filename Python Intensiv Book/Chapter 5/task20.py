from collections import defaultdict
import os

def word_count(file_path):
    chars_count = 0
    lines_count = 0
    words_count = 0
    unique_words = set()
    with open(file_path, 'r') as f:
        for line in f:
            lines_count += 1
            chars_count += len(line)
            for word in line.strip().split():
                words_count += 1
                unique_words.add(word)
    return (chars_count, words_count, lines_count, len(unique_words))


# print(word_count("wcfile.txt"))

def input_words_count():
    res = {}
    words_dict = defaultdict(int)
    file_path = input("Введите имя файла: ")
    raw_words = input("Введите слова через пробел: ")
    words = raw_words.strip().split()
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                words_dict[word] += 1
    for word in words:
        res[word] = words_dict.get(word, 0)
    return res

# print(input_words_count())

def file_list():
    res = {}
    items = os.listdir()
    for i in items:
        if os.path.isfile(i):
            res[i] = os.stat(i).st_size
    return res

# print(file_list())

def letters_count(path):
    res = defaultdict(int)
    items = os.listdir(path)
    for item in items:
        if os.path.isfile(path + '/' + item) and not item.startswith('.'):
            with open(path + '/' + item, 'r') as f:
                for line in f:
                    for c in line.strip():
                        if c.isalpha():
                            res[c.lower()] += 1
    return sorted(res.items(), key=lambda i: i[1], reverse=True)[:5]

print(letters_count('./test'))
