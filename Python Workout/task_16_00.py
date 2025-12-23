def dict_diff(d1, d2):
    res = {}
    keys = d1.keys() | d2.keys()
    for key in keys:
        if d1.get(key, None) != d2.get(key, None):
            res[key] = [d1.get(key, None), d2.get(key, None)]
    return res

print(dict_diff({'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a': 1, 'b': 2, 'c': 4, 'e': 5}))
