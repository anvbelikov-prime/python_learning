l = [1, 2, 3, 4, 5]
print(l)
l[2] = 7
print(l)

print('-' * 50)

s = 'Hello'

print(s)
print(list(s))

print('-' * 50)

l = []

for i in range(3):
    l.append([])
    l[i].append(i + 1)

print(l)

print('-' * 50)

a, b, c, *d = [1, 2, 3, 4, 5]
print(a, b, c, d)

a, b, *c = [1, 2]
print(a, b, c)

# a, b, *c = [1] Ошибка!
# print(a, b, c)

print('-' * 50)

l = [1, 2, 3, 4, 5]

print(l)
print(l[::-1])
print(l[-1])
print(l[:-1])
print(l[1:])
print(l[1:3])
l[1:3] = [9, 99]
print(l)
print(l + [7, 77, 777])

print('-' * 50)

l = [1, 2, 3, 4, 5]
print(5 in l)
l = [[1, 2, 3], [4, 5, 6, 7]]
print(l)
print([1, 2, 3] in l)
print([1, 2, 3] is l[0])

print('-' * 50)

l = [1, 2, 3, 4, 5, 6, 7, 7, 7]

print(l.index(3))
# print(l.index(9))

print(l.count(7))
print(l.count(9))
print(max(l), min(l))

print('-' * 50)

print(l)
l.insert(0, 999)
print(l)

print('-' * 50)

print(l)
print(l.pop())
print(l)
print(l.remove(7))
print(l)
print(l.remove(7))
print(l)
print(l.remove(999))
print(l)
del l[0]
print(l)

print('-' * 50)

l = [1, 2, 3, 4, 5]

print(l)
l.reverse()
print(l)

# l.reverse()

print('-' * 50)

import random
random.shuffle(l)

print(l)

for i in range(10):
    print(random.choice(l))

print('-' * 50)

for i in range(10):
    print(random.sample(l, 3))

print('-' * 50)

print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l = [-3, -2, -1, 0, 1, 2, 3]
print(l)
l.sort(reverse=True, key=abs)
print(l)

print('-' * 50)

l = [-3, -2, -1, 0, 1, 2, 3]
print(l)
l.sort(reverse=True, key=lambda x: x ** 2)
print(l)

print('-' * 50)

l = [1, 2, 3, 4, 5]
print(l)
print(sorted(l, reverse=True))
print(l)

print('-' * 50)

print(''.join([str(i) for i in l if i % 2 == 0]))
print('*'.join([str(i) for i in l if i % 2 != 0]))

print('-' * 50)

import re

s = 'asdjh sdkjfhd,sodgso, fdsgkjdfgk   ; owiuoiwu    sldkfjdskl'
print(re.split(r'\s*[,;\s]\s*', s))
