import collections

def file_tail(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines[-1]

# print(file_tail("text.txt"))

def sum_numeric_words(file_path):
    res = 0
    with open(file_path, "r") as f:
        for line in f:
            for word in line.strip().split():
                if word.startswith("-") and word[1:].isnumeric():
                    res += -int(word[1:])
                elif word.isnumeric():
                    res += int(word)
    return res

# print(sum_numeric_words("text2.txt"))

def get_sum_multiples(file_path):
    res = 0
    with open(file_path, 'r') as f:
        for line in f:
            words = line.strip().split('\t')
            if len(words) < 2:
                continue
            else:
                try:
                    first = float(words[0])
                    second = float(words[1])
                except:
                    continue
                res += first * second
    return res

# print(get_sum_multiples("text3.txt"))

def count_vowels(file_path):
    res = collections.Counter()
    with open(file_path, 'r') as f:
        for line in f:
            res += collections.Counter(''.join(filter(lambda x: x in 'aeiou', line.strip().lower())))
    for k, v in res.most_common():
        print(f'{k}  |  {v}')

count_vowels("text4.txt")
