import keyword
print(keyword.kwlist)

import builtins
print(dir(builtins))

print('-' * 50)

s = 'abc'

print(type(s))
print(isinstance(s, str))
print(isinstance(s, bytes))
print(isinstance(s, float))

print('-' * 50)

lst = [1, 2, 3]

i = iter(lst)
print(i.__next__())
print(next(i))
print(next(i))
# print(next(i))  # Будет ошибка StopIteration

print('-' * 50)

a = 1
b = 1
print(a is b)
b = 2
print(a is b)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
a = b = [7, 8, 9]
print(a is b)
print(a is not b)

print('-' * 50)

a = b = [1, 2, 3]
a[1] = 7
print(b[1]) # 7

a = [1, 2, 3]
b = a.copy()
a[1] = 7
print(b[1])

import copy
a = [1, 2, 3]
b = copy.deepcopy(a)
a[1] = 7
print(b[1])

print('-' * 50)

a, b, c = 1, 2, 3
print(a, b, c)

a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)
