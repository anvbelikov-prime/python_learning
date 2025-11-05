a = 0b1110000
b = 0o555
c = 0xfff

print(a)
print(b)
print(c)

a = 0b1

print(a)
print(a << 2)

a = 1e6

print(a)

a = 3 + 4j

print(a)
print(type(a))

import decimal

print(dir(decimal))

print(decimal.Decimal('0.55'))

import fractions

print(fractions.Fraction(7, 15) + fractions.Fraction(7, 15))

a = fractions.Fraction(7, 15) + fractions.Fraction(7, 15)

print(a.numerator)
print(a.denominator)

print(hex(16))

print(int('0o555', 8))

print(int('10', 8))

print(round(2.75))

a = 20000.756970

print(a)

print(format(a, '^10,.2f'))
print(format(a, '^10,.2e'))
print(format(a, '^10,.2E'))

print('-' * 50)

s = '2,000.75'
print(s)
print(s.translate({ord('.'): ord(','), ord(','): ord('.')}))

import math
import cmath # for complex numbers

print(math.pi)

print(dir(cmath))

print(cmath.pi)

import random

print(random.random())
print(random.uniform(-100, 100))
print(random.randrange(0, 100, 1))
print(random.randint(0, 100))

l = [1, 2, 3, 4, 5, 6, 7]

ll = l.copy()

random.shuffle(ll)

print(l)
print(ll)

print(random.choice(ll))

print(random.sample(ll, 3))

print(float('-inf'))
print(float('inf'))
print(float('nan'))

print(math.isnan(float('nan')))
print(math.isinf(float('inf')))
print(math.isinf(float('-inf')))
