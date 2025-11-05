print(10.0 // 2.5)
print(10.0 % 2.5)

print('-' * 50)

print(10 // 3)
print(10 % 3)

print('-' * 50)

from decimal import Decimal

print(0.5 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1)
print(Decimal('0.5') - Decimal('0.1') - Decimal('0.1') - Decimal('0.1') - Decimal('0.1') - Decimal('0.1'))

print('-' * 50)

print([1, 2, 3] + [4, 5])
print((1, 2, 3) + (4, 5))
# print([1, 2, 3] + 1)

print('-' * 50)
print('Калькулятор')

def my_sum(a, b):
    return a + b

def my_sub(a, b):
    return a - b

def my_mult(a, b):
    return a * b

def my_div(a, b):
    return a / b

d = {'+': my_sum, '-': my_sub, '*': my_mult, '/': my_div, 'q': exit}

while True:
    operation = input('Введите операцию: ')
    if operation not in d:
        print('Неизвестная операция')
        continue
    else:
        if operation == 'q':
            d[operation]()
        try:
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))
            if b == 0.0 and operation == '/':
                print('Деление на ноль запрещено!')
                continue
        except:
            print('Ошибка чтения числа')
            continue
        print(f'Результат: {d[operation](a, b)}')
