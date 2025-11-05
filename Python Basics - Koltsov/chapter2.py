import keyword
import builtins

print(keyword.kwlist)

print('-' * 50)

print(dir(builtins))

print('-' * 50)

d1 = {'a': 1, 'b': 2}
d2 = d1
d2['c'] = 3
print(d1) # d1 поменялся
print(d1 is d2) # True

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2) # True

d3 = {'a': 2}
d4 = {'a': 2}
print(d3 is d4) # False

s1 = '123'
s2 = '123'
print(s1 is s2) # True

a = 5

def func():
    a = 4
    print(a)

func()
print(a)

def my_func():
    global a
    a += 1

print(a)
my_func()
print(a)

def outer_func():
    a = 1
    def inner_func():
        nonlocal a
        a += 2
    inner_func()
    return a

print(outer_func())

l = [1, 2, 3]
a, *b = l
print(a)
print(b)

a, b, _ = l
print(a)
print(b)

print(type(a) == str)
print(type(a) == int)
print(type(3.75) == float)
print(type('123') == str)
print(type(d1) == dict)
print(type(l) == list)
print(type({1, 2, 3}) == set)
print(type((1, 2, 3)) == tuple)
print(type(True) == bool)

del a, b # delete variable

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print(a + b)
