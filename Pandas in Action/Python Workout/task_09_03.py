def get_largest_word(f):
    res = ''
    for line in f:
        for word in line.strip().split():
            if len(word) > len(res):
                res = word
    return res

with open('test.txt', 'r') as f:
    word = get_largest_word(f)

print(word)
