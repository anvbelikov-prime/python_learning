def pig_latin(word):
    if word[0].isupper():
        if not word[-1].isalnum():
            if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
                return word[:-1] + 'way' + word[-1]
            else:
                return word[1:-1].capitalize() + word[0].lower() + 'ay' + word[-1]
        else:
            if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
                return word + 'way'
            else:
                return word[1:].capitalize() + word[0].lower() + 'ay'   
    else:
        if not word[-1].isalnum():
            if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
                return word[:-1] + 'way' + word[-1]
            else:
                return word[1:-1] + word[0] + 'ay' + word[-1]
        else:
            if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
                return word + 'way'
            else:
                return word[1:] + word[0] + 'ay'
    
print(pig_latin('air,'))
print(pig_latin('eat.'))
print(pig_latin('python,'))
print(pig_latin('computer.'))
print('-' * 50)
print(pig_latin('Air,'))
print(pig_latin('Eat.'))
print(pig_latin('Python;'))
print(pig_latin('Computer:'))
