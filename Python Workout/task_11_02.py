def vowels_count(word):
    vowels = set('aeiou')
    res = 0
    for c in word:
        if c in vowels:
            res += 1
    return res

def vowels_sort(lst):
    return sorted(lst, key=vowels_count)

print(vowels_sort(['aaeeiiioo', 'bnd', 'abc', 'aaeefgh', 'hjk']))
