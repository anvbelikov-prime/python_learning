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
            
def pl_sentence(s):
    return ' '.join([pig_latin(word) for word in s.strip().split()])

print(pl_sentence('This is a test translation'))
