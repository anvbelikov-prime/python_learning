def alt_pig_latin(word):
    if word[0].isupper():
        if not word[-1].isalnum():
            if len(set(word.lower()) & set('aeiou')) > 1:
                return word[:-1] + 'way' + word[-1]
            else:
                return word[1:-1].capitalize() + word[0].lower() + 'ay' + word[-1]
        else:
            if len(set(word.lower()) & set('aeiou')) > 1:
                return word + 'way'
            else:
                return word[1:].capitalize() + word[0].lower() + 'ay'   
    else:
        if not word[-1].isalnum():
            if len(set(word.lower()) & set('aeiou')) > 1:
                return word[:-1] + 'way' + word[-1]
            else:
                return word[1:-1] + word[0] + 'ay' + word[-1]
        else:
            if len(set(word.lower()) & set('aeiou')) > 1:
                return word + 'way'
            else:
                return word[1:] + word[0] + 'ay'

print(alt_pig_latin('wine'))
print(alt_pig_latin('wind'))
print(alt_pig_latin('Wine'))
print(alt_pig_latin('Wind'))
print(alt_pig_latin('Wine;'))
print(alt_pig_latin('Wind:'))
