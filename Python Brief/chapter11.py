def my_func(*args, **kwargs):
    return args, kwargs

l = [1, 2, 3]
d = {'a':1, 'b':2, 'c':3}

print(my_func(*l, **d))

def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
