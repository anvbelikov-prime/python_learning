def ubbi_dubbi(word):
    res = ''
    vowels = set('aeiou')
    for w in word:
        if w.lower() in vowels:
            res += ('ub' + w)
        else:
            res += w
    return res

print(ubbi_dubbi('milk'))
print(ubbi_dubbi('soap'))
print(ubbi_dubbi('octopus'))
