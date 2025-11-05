import collections

def most_repeated_letter(word):
    return collections.Counter(word).most_common(1)[0][1]

def most_repeated_word(words):
    return max(words, key=most_repeated_letter)

print(most_repeated_word(['this', 'is', 'an', 'elementary', 'test', 'example']))
