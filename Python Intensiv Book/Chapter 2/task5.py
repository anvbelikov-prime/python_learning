def pig_latin(word):
    if word[0] in 'aeiouy':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

def pig_latin_v2(word):
    if word[0].lower() in 'aeiouy':
        return word + 'way'
    else:
        if word[0].isupper():
            new_begining = word[1:].capitalize()
        else:
            new_begining = word[1:]
        return new_begining + word[0].lower() + 'ay'

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

def get_num_different_vowels(word):
    return len(set([vowel for vowel in word if vowel.lower() in 'aeiouy']))

def pig_latin_v4(word):
    if get_num_different_vowels(word) > 1:
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

print(pig_latin_v4('Python!'))
print(pig_latin_v4('python!'))
print(pig_latin_v4('computer'))
print(pig_latin_v4('air'))
print(pig_latin_v4('Air!'))
print(pig_latin_v4('wind'))
print(pig_latin_v4('Wind!'))
print(pig_latin_v4('wine'))
