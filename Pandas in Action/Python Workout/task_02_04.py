def my_sum(*args):
    res = 0
    for i in args:
        try:
            res += int(i)
        except:
            continue
    return res

print(my_sum(1, 'a', 2, 3, 4, 'a', 5, 6, 7, 'aaa'))
