s = 'abc'

print(len(s))
print(s[1])

# s[1] = 'd'  Ошибка!

print('ab' in s)
print('ac' in s)

s = 'Привет!'

print(s.encode(encoding='utf-8'))
print(s.encode(encoding='cp1251'))

print(type(s.encode(encoding='utf-8')))

print(len(bytes(s, 'utf-8'))) # кол-во байт, а не символов
print(len(s))

b = bytes(s, 'utf-8')
print(b[0])
print(b[1])

# b[1] = 2  Ошибка!

b = bytearray('Hello!', 'utf-8')

b[1] = 50

print(b)

print(bytes('Hello!', 'utf-8').decode('utf-8'))

a = '''Многострочная
строка'''

print(a)

def my_func():
    '''Пустая функция!'''
    pass

print(my_func.__doc__)

print('C:\n')
print(r'C:\n')  # Полезно для регулярных выражений

print(a)
print(a[::-1])
print(a[:5])
print(a[::2])

l = [1, 2, 3]

print(str(l))
print(repr(l))
print(ascii(l))

s = 'Hello, world! Hell!'

print(s.count('Hell'))
print(s.count('abc'))

print(s.find('Hell'))
print(s.find('abc'))

print(s.replace('Hell', 'Hello'))

print('_'.join([str(i) for i in l]))

print('_'.join([str(i) for i in l]).split('_'))

s = '    \t\t\nabc_ABC   \t\t\t\t\t\n\n\n\n\n\n'

print(s.strip())

print(chr(5050))
print(ord(','))
print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))
