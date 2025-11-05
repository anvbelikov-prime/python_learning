#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys

args = sys.argv[:]

привет = 'привет!'

print('Hello, world!')
print(привет)

print()

a, b = 1, 2_000

print(
    a,
    b
)

# Comment
print(f'{a} {b:,.2f}') # this is another comment

# Многострочный
# комментарий

print(f'{a + b}', f'{a - b}', sep='\t', end='\n')
print(привет)

try:
    name = input('Enter your name: ')
    print(f'Hello, {name}! Parameters: {args}')
except EOFError:
    print('EOF Exception catched!')
except KeyboardInterrupt:
    print(f'Keyboard Interrupt Exception catched!')
