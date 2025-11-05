a = 100
b = 100
print(a is b)
print(a == b)
print(not(a == b))
print(2 in [1, 2, 3])
print(a is not b)
print( 2 <= 5 <= 7)

print('-' * 50)
n = int(input('Введите целое число n: '))
if n < 100:
    print('n < 100')
elif 100 <= n < 1000:
    print('100 <= n < 1000')
else:
    print('n >= 1000')

print('-' * 50)

for c in 'Anton':
    print(c)

print('-' * 50)

for i in range(1, 10, 2):
    print(i, end=' ')
    if i % 2 == 0:
        break
else:
    print()
    print('Только нечетные числа!')

print('-' * 50)

for i in range(0, 10, 2):
    print(i, end=' ')
    if i % 2 == 0:
        break
else:
    print()
    print('Только нечетные числа!')

print('-' * 50)

for i in range(0, 20, 1):
    if i == 5:
        continue
    elif i == 12:
        break
    else:
        print(i, end=' ')
print()


