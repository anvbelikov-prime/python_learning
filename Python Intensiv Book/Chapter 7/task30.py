import operator

def flatten_list(lst):
    return [ll for l in lst for ll in l]

# print(flatten_list([[1, 2], [3, 4]]))

def safe_int(s):
    try:
        return int(s)
    except:
        return 0

def flatten_odd_ints(lst):
    return [safe_int(ll) for l in lst for ll in l if safe_int(ll) % 2]

# print(flatten_odd_ints([[1, 2], [3, 4], ['a', '3', 'a3', '3b', 333, '333', '!']]))

family = {
    'A': ['B', 'C', 'D'],
    'E': ['F', 'G']
}

def get_grandchildren(family_dict):
    return [gc for _, lst in family_dict.items() for gc in lst]

# print(get_grandchildren(family))

family_v2 = {
    'A': [{'name':'B', 'age':24}, {'name':'C', 'age':18}, {'name':'D', 'age':10}],
    'E': [{'name':'F', 'age':12}, {'name':'G', 'age':7}]
}

def get_sorted_grandchildren(family_dict):
    return list(map(operator.itemgetter('name'), sorted([gc for _, lst in family_dict.items() for gc in lst], key=operator.itemgetter('age'))))

print(get_sorted_grandchildren(family_v2))
