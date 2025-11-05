def my_sum(*args, start=0):
    res = start
    for i in args:
        res += i
    return res

print(my_sum(1, 2, 3, 4, 5, 6, 7, start=5))
print(my_sum(*[1, 2, 3, 4, 5, 6, 7], start=5))
print(sum([1, 2, 3, 4, 5, 6, 7], 5))
