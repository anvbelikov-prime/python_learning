import copy

def pig_latin_v3(word):
    if word[0].lower() in 'aeiouy':
        if word[-1].isalnum():
            return word + 'way'
        else:
            return word[:-1] + 'way' + word[-1]
    else:
        if word[0].isupper():
            new_begining = word[1:].capitalize()
        else:
            new_begining = word[1:]
        if word[-1].isalnum():
            return new_begining + word[0].lower() + 'ay'
        else:
            return new_begining[:-1] + word[0].lower() + 'ay' + new_begining[-1]
        
def pl_sentence(sentence):
    return ' '.join([pig_latin_v3(word) for word in sentence.split(' ')])

# print(pl_sentence('This is a test, translation!'))

def generate_sentence_from_file():
    lst = []
    with open("text.txt", "r") as f:
        count = 0
        for line in f:
            if count == 10:
                break
            else:
                lst.append(line.split()[count])
                count += 1
    return ' '.join(lst)

# print(generate_sentence_from_file())

def transpose_lists(lst):
    new_lst = [l.split() for l in copy.copy(lst)]
    res = []
    for j in range(0, len(new_lst[0])):
        res.append([])
    for i in range(0, len(new_lst)):
        for j in range(0, len(new_lst[0])):
            res[j].append(new_lst[i][j])
    res = [' '.join(l) for l in res]
    return res

# print(transpose_lists(['a b c d', 'a b c d', 'a b c d']))

def another_transpose_lists(lst):
    print([' '.join(t) for t in (zip(*[l.split() for l in lst]))])

another_transpose_lists(['a b c d', 'a b c d', 'a b c d'])
