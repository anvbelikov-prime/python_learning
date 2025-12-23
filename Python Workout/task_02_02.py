def my_avg(*args):
    res = 0
    for i in args:
        res += i
    return res / len(args)

print(my_avg(1, 2, 3, 4, 5, 6, 7))
