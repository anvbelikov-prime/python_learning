def ubbi_dubbi(word):
    res = ''
    vowels = set('aeiou')
    for w in word:
        if w.lower() in vowels:
            res +=  ('Ub' + w.lower()) if w.isupper() else ('ub' + w)
        else:
            res += w
    return res

print(ubbi_dubbi('mIlk'))
print(ubbi_dubbi('soAp'))
print(ubbi_dubbi('Octopus'))
