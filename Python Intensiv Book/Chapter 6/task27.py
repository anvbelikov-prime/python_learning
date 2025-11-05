import random
import string

def create_password_generator(seq):
    def password_generator(num):
        return ''.join([random.choice(seq) for i in range(num)])
    return password_generator

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

# print(alpha_password(5))
# print(alpha_password(10))
# print(symbol_password(5))
# print(symbol_password(10))

def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def password_checker(s):
        uppercase_count = 0
        lowercase_count = 0
        punctuation_count = 0
        digits_count = 0
        for c in s.strip():
            if c in string.ascii_uppercase:
                uppercase_count += 1
            elif c in string.ascii_lowercase:
                lowercase_count += 1
            elif c in string.punctuation:
                punctuation_count += 1
            elif c in string.digits:
                digits_count += 1
        return (uppercase_count >= min_uppercase) and (lowercase_count >= min_lowercase) and (punctuation_count >= min_punctuation) and (digits_count >= min_digits)
    return password_checker

# print(create_password_checker(2, 5, 1, 1)('Abefcd!1'))

def getitem(k):
    def getter(o):
        return o[k]
    return getter

# print(getitem(1)([1, 7, 9]))

def do_both(f1, f2):
    def func(a):
        return f2(f1(a))
    return func

