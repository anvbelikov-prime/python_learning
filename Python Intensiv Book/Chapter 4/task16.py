def dictdiff(d1, d2):
    res = {}
    keys = d1.keys() | d2.keys()
    for key in keys:
        if d1.get(key, None) != d2.get(key, None):
            res[key] = [d1.get(key, None), d2.get(key, None)]
    return res

# print(dictdiff({}, {}))
# print(dictdiff({'a':1, 'b':2}, {'a':1, 'b':2}))
# print(dictdiff({'a':1, 'b':2}, {'a':1, 'b':3}))
# print(dictdiff({'a':1, 'b':2}, {'a':1, 'c':3}))
# print(dictdiff({'a':1, 'b':2, 'c':3}, {'a':1, 'b':3, 'd':5}))

def dict_update(*args):
    res = {}
    for d in args:
        for key in d:
            res[key] = d[key]
    return res

# print(dict_update({'a':1, 'b':2}, {'a':2, 'c':3}))

def dict_create(*args):
    res = {}
    if len(args) % 2:
        return {}
    else:
        for i in range(0, len(args) - 1, 2):
            lst = args[i:i+2]
            res[lst[0]] = lst[1]
    return res

# print(dict_create(1, 2, 3))
# print(dict_create('a', 1, 'b', 2))
# print(dict_create('a', 1, 'b', 2, 'c', 3))
# print(dict_create('a', 1, 'b', 2, 3, 3))

def threshold(k,v):
    return abs(v) < 10

def even(k,v):
    return v % 2

def positive(k, v):
    return v > 0

def dict_partition(d, f):
    d1 = {}
    d2 = {}
    for k,v in d.items():
        if f(k,v):
            d1[k] = v
        else:
            d2[k] = v
    return d1, d2

print(dict_partition({'a':-1, 'b':-9, 'c':5, 'd':15, 'e':9, 'f':4, 'g':12}, threshold))
print(dict_partition({'a':-1, 'b':-9, 'c':5, 'd':15, 'e':9, 'f':4, 'g':12}, even))
print(dict_partition({'a':-1, 'b':-9, 'c':5, 'd':15, 'e':9, 'f':4, 'g':12}, positive))
