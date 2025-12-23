def my_sum(*args):
    res = args[0]
    for e in args[1:]:
        res += e
    return res

def mys_sum_bigger_than(lim, *args):
    return my_sum(*list(filter(lambda x: x > lim, args)))

print(mys_sum_bigger_than(10, 5, 20, 30, 6))
