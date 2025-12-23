import collections

def dict_union(dicts):
    res = collections.defaultdict(list)
    for d in dicts:
        for k in d:
            res[k].append(d[k])
    for k in res:
        if len(res[k]) <= 1:
            res[k] = res[k][0]
    return res

print(dict_union([{'a':1, 'b': 2, 'c':3}, {'a':4, 'b':5, 'e':6}, {(1, 2):1, (3, 4): 2}, {'f':777}]))
