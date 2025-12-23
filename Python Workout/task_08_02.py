def last_word(file_path):
    res = ''
    with open(file_path, 'r') as f:
        res = list(f)[-1].split()[-1]
    return res

print(last_word('test.txt'))
