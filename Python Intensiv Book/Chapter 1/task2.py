def my_sum(*args, start=0):
    res = start
    for i in args:
        res += i
    return res

def my_mean(*args):
    n = len(args)
    return my_sum(*args) / n

def my_min(*args):
    res = args[0]
    for i in args:
        if i < res:
            res = i
    return res

def my_max(*args):
    res = args[0]
    for i in args:
        if i > res:
            res = i
    return res

def words_stat(*args):
    lengths = []
    for w in args:
        lengths.append(len(w))
    return (my_min(*lengths), my_max(*lengths), my_mean(*lengths))

def safe_int_for_sum(obj):
    try:
        return int(obj)
    except:
        return 0

def my_sum_obj(*args, start=0):
    res = start
    for o in args:
        res += safe_int_for_sum(o)
    return res

print(my_sum_obj(1, 2, 3, [1, 2], 'a', 'a1b2c', -1, None))
