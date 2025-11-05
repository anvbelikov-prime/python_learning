def my_sum(*args, start=0):
    print(args)
    print(start)
    res = start
    for i in args:
        res += i
    return res

print(my_sum(1, 2, 3, 4, start=10))