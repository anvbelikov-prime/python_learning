def my_func(x, y):
    return f'{x} - {y}'

print(my_func(2, 3))
print(my_func(3, 2))
print(my_func(y=3, x=2))

def my_func(x, y=3):
    return f'{x} - {y}'

print(my_func(2))
print(my_func(2, 4))

def my_func(x=2, y=3):
    return f'{x} - {y}'

print(my_func())
print(my_func(7, 77))

d = {'x': 5, 'y': 10}

print(my_func(**d))

print('-' * 50)

def my_sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))

l = [1, 2, 3]
print(my_sum(*l))

print('-' * 50)

def my_func(x, *args, y):
    print(x, args, y)

my_func(1, y=2)
my_func(1, 2, 3, y=4)

print('-' * 50)

def my_func(*args, **kwargs):
    print(type(args), type(kwargs))
    print(args, kwargs)

my_func(1, 2, 3, name='A', surname='B')

my_add = lambda x, y: x + y

print(my_add(1, 2))

print('-' * 50)

def my_generator(x, y):
    for i in range(x + 1):
        yield i + y

for i in my_generator(5, 2):
    print(i, end=' ')
print()

print('-' * 50)

def fib_gen(lim=10):
    i = 0
    a, b = 0, 1
    while i <= lim:
        if i == 0:
            yield a
        elif i == 1:
            yield b
        else:
            b, a = a + b, b
            yield b
        i += 1

for i in fib_gen(20):
    print(i, end=' ')
print()

print(list(fib_gen(100)))

print('-' * 50)

# Декораторы: https://habr.com/ru/companies/otus/articles/727590/?ysclid=mfb36fz9z7248358949

# В общих чертах декоратор — это вызываемый объект, который принимает на вход вызываемый объект и возвращает другой вызываемый объект.

def null_decorator(func):
    return func

def add_em(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def add_strong(func):
    def wrapper():
        return '<Strong>' + func() + '</Strong>'
    return wrapper

def greet():
    return 'Hello!'

print(greet())

@add_strong
@add_em
def greet():
    return 'Hello!'

print(greet())

def add_something(addition):
    def decorator(func):
        def wrapper():
            return '<' + addition + '>' + func() + '</' + addition + '>'
        return wrapper
    return decorator

@add_something('Strong')
@add_something('em')
def greet():
    return 'Hello!'

print(greet())

print('-' * 50)

import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Call: {func.__name__} function with arguments: {args}, {kwargs} ')
        return func(*args, **kwargs)
    return wrapper

def greet(name):
    '''Greets a person'''
    return f'Greeting, {name}!'

print(greet('Anton'))
print(greet.__name__)
print(greet.__doc__)

print('-' * 50)

@trace
def greet(name):
    '''Greets a person'''
    return f'Greeting, {name}!'

print(greet('Anton'))
print(greet.__name__)
print(greet.__doc__)
