a = 0
b = 0
is_incorrect = True
# try:
#     a == 50
# except SyntaxError:
#     print('Syntax Error!')

# print("I'm still here!")

while is_incorrect:
    try:
        a = int(input('Введите первое целое число: '))
        b = int(input('Введите второе целое число: '))
        c = a / b
        is_incorrect = False
    except ValueError as e:
        print('Необходимо ввести целое число!')
        print(e)
    except ZeroDivisionError as e:
        print('Деление на ноль запрещено!')
        print(e)
    else:
        print('Else operator!')
    finally:
        print('Finally operator!')

print(f'Result is {c:^10.2f}')

try:
    x = -5
    assert x >= 0, 'Error'
except AssertionError as msg:
    print(msg)

try:
    raise ValueError('My error message!')
except ValueError as e:
    print(e)
