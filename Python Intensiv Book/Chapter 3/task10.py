import copy

def my_sum(*args):
    res = copy.deepcopy(args[0])
    for a in args[1:]:
        res += copy.deepcopy(a)
    return res

# print(my_sum('a'))
# print(my_sum('abc', 'def'))
# print(my_sum([1, 2, 3], [4, 5, 6]))
# print(my_sum((1, 2, 3), (4, 5, 6)))
# print(my_sum(1, 2, 3))

def my_sum_bigger(threshold, *args):
    count = 0
    res = None
    for a in args:
        if a <= threshold:
            count += 1
        else:
            res = copy.deepcopy(a)
            break
    for a in args[count + 1:]:
        if a > threshold:
            res += a
    return res

# print(my_sum_bigger('a', 'b', 'bb', 'z', 'aa', 'zz'))

def safe_int(i):
    try:
        return int(i)
    except:
        return 0

def sum_numeric(*args):
    res = 0
    for a in args:
        res += safe_int(a)
    return res

# print(sum_numeric(10, 20, '30', 'abc', [1, 2, 3]))

def dict_union(dicts):
    if not dicts:
        return None
    res = {}
    keys = []
    for d in dicts:
        keys += d.keys()
    keys = set(keys)
    for key in keys:
        elements = []
        for d in dicts:
            if key in d.keys():
                elements.append(d[key])
        if len(elements) > 1:
            res[key] = elements
        else:
            res[key] = elements[0]
    return res

print(dict_union([{'a':1, 'b':2, 'c':3}, {'a':4, 'd':5}]))
