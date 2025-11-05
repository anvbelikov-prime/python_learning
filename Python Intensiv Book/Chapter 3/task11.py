import operator

PEOPLE = [{'first': 'Reuven', 'last' :'Lerner', 'email':'reuven@lerner.co.il'},
          {'first': 'Donald', 'last':'Trump', 'email' :'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last' :'Putin', 'email' :'president@kremvax.ru'}]

def alphabetize_names(d):
    return sorted(d, key=operator.itemgetter("last", "first"))

def alphabetize_names_v2(d):
    return sorted(d, key=lambda i: (i["last"], i["first"]))

# print(alphabetize_names(PEOPLE))
# print(alphabetize_names_v2(PEOPLE))

def sorted_abs(seq):
    return sorted(seq, key=abs)

# print(sorted_abs([-5, -4, 0, 2, 4]))

def vowel_count(s):
    res = 0
    for c in s:
        if c in 'aeuioy':
            res += 1
    return res

def sorted_vowels(seq):
    return sorted(seq, key=vowel_count)

# print(sorted_vowels(['a', 'aep', 'oo', 'b', 'd', 'eel']))

def sorted_inner_list_sum(seq):
    # return sorted(seq, key=lambda i: sum(i))
    return sorted(seq, key=sum)

print(sorted_inner_list_sum([[1, 2, 3], [], [10]]))
