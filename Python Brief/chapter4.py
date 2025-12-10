n = 0
while n < 11:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1
else:
    print('End!')

print('-' * 50)

for i in range(11):
    if i % 2 != 0:
        continue
    if i == 10:
        break
    print(i)
else:
    print('End!')
