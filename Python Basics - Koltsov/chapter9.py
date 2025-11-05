t = (1, 2, 3, 4, 5)
print(t[2])
# t[1] = 777 Ошибка!

t = tuple('Hello')
print(t)

print(t[1:3])
print(t[::-1])
print(t * 2)
print(t + (7, 8, 9))
print(3 in t)
print('e' in t)

print('-' * 50)

print(t.index('e'))
# print(t.index('m')) Ошибка!!!
print(t.count('e'))
print(t.count('l'))
print(len(t))

print('-' * 50)

import itertools

for i in itertools.count():
    if i > 15:
        break
    print(i, end=' ')
print()

j = 0
for i in itertools.count():
    j += 1
    if j > 3:
        break
    print(i, end=' ')
print()

print('-' * 50)

print(tuple(itertools.repeat('*', 10)))
print(list(itertools.repeat('*', 10)))
print(set(itertools.repeat('*', 10)))

print('-' * 50)

print(list(itertools.combinations('abcd', 2)))
print(list(itertools.combinations_with_replacement('abcd', 2)))
print(list(itertools.permutations('abcd', 2)))

print('-' * 50)

j = 0
for i in itertools.cycle(range(3)):
    j += 1
    if j > 9:
        break
    print(i, end=' ')
print()

print('-' * 50)

print(list(itertools.dropwhile(lambda x: x < 5, range(11))))

print('-' * 50)


t = (1, 2, 3, (4, 5, 6))
a, b, c, (d, e, f) = t
print(a, b, c, d, e, f)
_, a, b, *_ = t
print(a, b)

l = [1, 2, 3, 4, 5]
first, *middle, last = l
print(first, middle, last)
