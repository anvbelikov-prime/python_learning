def my_sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(my_sum(1, 2, 3, 4, 5, 6, 7))
print(my_sum(*[1, 2, 3, 4, 5, 6, 7]))
print(sum([1, 2, 3, 4, 5, 6, 7]))
