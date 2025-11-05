def my_sum(*args):
    res = args[0]
    for e in args[1:]:
        res += e
    return res

print(my_sum([1, 2, 3], [4, 5, 6]))
print(my_sum('abc', 'def', 'ghi', 'jklmno'))
print(my_sum(1, 2, 3))
