import collections

def most_repeated_vowel_letter(word):
    vowels = set('aeiou')
    return collections.Counter(list(filter(lambda c: c in vowels, word))).most_common(1)[0][1]

def most_repeated_word(words):
    return max(words, key=most_repeated_vowel_letter)

print(most_repeated_word(['this', 'is', 'an', 'elementary', 'test', 'example', 'aaaaaaa']))
