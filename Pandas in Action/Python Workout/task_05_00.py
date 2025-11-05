def pig_latin(word):
    if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'
    
print(pig_latin('air'))
print(pig_latin('eat'))
print(pig_latin('python'))
print(pig_latin('computer'))
