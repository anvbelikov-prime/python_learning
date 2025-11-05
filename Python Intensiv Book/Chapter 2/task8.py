def strsort(s):
    return ''.join(sorted(s))

# print(strsort('bca'))

def wordsort(s):
    return ', '.join(sorted(s.split()))

# print(wordsort('Tom Dick Harry'))

def last_word():
    with open("text.txt", "r") as f:
        return list(f)[-1].split()[-1]

# print(last_word())

def most_long_word():
    words = []
    lengths = []
    max_length = 0
    max_word = ''
    with open("text.txt", "r") as f:
        for line in f:
            for w in line.split():
                words.append(w)
                lengths.append(len(w))
    count = 0
    for w, l in zip(words, lengths):
        if count == 0:
            max_length = l
            max_word = w
        elif l > max_length:
            max_length = l
            max_word = w
        count += 1
    return max_word, max_length

print(most_long_word())
