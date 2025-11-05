d = dict()
print(d)
d = dict(name='A', surname='B')
print(d)
d1 = dict(d)
print(d1)
print(d1 is d)
d = dict([('name', 'A'), ('surname', 'B')])
print(d)

k = ['name', 'surname']
v = ['A', 'B']
d = dict(list(zip(k, v)))
print(d)

d1 = d
print(d1 is d)

import copy

d1 = copy.deepcopy(d)
print(d is d1)

if 'name' in d:
    print(d['name'])

print(len(d))

d['lastname'] = 'B'

print(d)

del d['lastname']

print(d)

for k in d:
    print(f'{k:^10} ---> {d[k]:^10}')

l = list(d.keys())
l.sort(reverse=True)

for k in l:
    print(f'{k:^10} ---> {d[k]:^10}')

d['lastname'] = 'B'

print(d.values())

print(d.items())

print(d)
d.pop('lastname')
print(d)

print(d.get('firstname', 'Not Found!'))

print('-' * 50)

s = set()

s = set('Hello!')
print(s)
s = set([1, 2, 3, 1, 2, 3])
print(s)

for i in s:
    print(i, end=' ')
print()

print(len(s))

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1)
print(s2)

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)

print('-' * 50)

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
print(s1 < s2)

s1 = {1, 2, 3, 7}
print(s1 < s2)

print('-' * 50)

print(s2)
print(s2.pop())
print(s2)

print(s2.discard(2))
print(s2)
print(s2.discard(2))
print(s2)
s2.add(777)
print(s2)
s2.clear()
print(s2)
