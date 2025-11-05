def dict_union(*dicts):
    res = {}
    for d in dicts:
        for k in d:
            res[k] = d[k]
    return res

print(dict_union({'a':1, 'b':2, 'c':3}, {'a':2, 'd':5, 'e':7}, {'a':10, 'e':9, 'f':7, 'c': 3}))
