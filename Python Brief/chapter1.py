#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

print('Hello, world!')

a = 3; b = 5; c = a + b;
print(c)

x = a + b \
    * c
print(x)

x = (a + b   # Comment
     * c)
print(x)

print(a, b, c, sep='\t', end='\n\n')

with open('file_text_example.txt', 'w') as file_output:
    for i in range(3):
        print(a, b, c, sep='\t', end='\n\n', file=file_output)

print('-' * 50)

with open('file_text_example.txt', 'r') as file_input:
    for line in file_input:
        print(line, end='')

print('-' * 50)

sys.stdout.write('А это другой способ вывести текст!\n')

try:
    name = input('Enter your name: ')
    print(name)
except:
    print('Error!')

