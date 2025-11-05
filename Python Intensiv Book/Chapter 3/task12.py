import collections

def most_repeated_letter(word):
    _, num = collections.Counter(word).most_common(1)[0]
    return num

def most_repeated_vowel_letter(word):
    _, num = collections.Counter(filter(lambda i: i.lower() in 'eyuioa', word)).most_common(1)[0]
    return num

def most_repeated_word(seq):
    return max(seq, key=most_repeated_letter)

def most_repeated_word_v2(seq):
    return max(seq, key=most_repeated_vowel_letter)

print(most_repeated_word(['elementary', 'this', 'abba', 'exced', 'aeyuio']))
print(most_repeated_word_v2(['elementary', 'this', 'abbaa', 'exceed', 'aeyuio', 'thiiiis']))

def most_common_shells(file_name):
    shells = collections.defaultdict(list)
    with open(file_name, 'r') as f:
        for line in f:
            splitted_line = line.split(':')
            shells[splitted_line[-1].strip()].append(splitted_line[0].strip())
    for k, v in sorted(shells.items(), key=lambda i: len(i[1]), reverse=True):
        print(f'Shell "{k}" with users "{", ".join(v)}" ({len(v)} account(s))')

most_common_shells('passwd_example.txt')
