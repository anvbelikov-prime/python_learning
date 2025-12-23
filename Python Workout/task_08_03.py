def get_longest_word(file_path):
    res = ''
    length = 0
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                if len(word) > length:
                    res = word
                    length = len(word)
    return res

print(get_longest_word('test.txt'))
