import operator

def calc(s):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }
    if not s:
         return 0
    s = s.split()
    if len(s) < 3:
         return 0
    return operations[s[2]](int(s[0]), int(s[1]))

# print(calc('5 3 /'))

def multiple_calc(s):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }
    if not s:
         return 0
    s = s.split()
    if len(s) < 3:
         return 0
    res = int(s[1])
    for i in s[2:]:
         res = operations[s[0]](res, int(i))
    return res

# print(multiple_calc('/ 100 5 5'))

def apply_to_each(func, seq):
     return [func(i) for i in seq]

# print(apply_to_each(lambda x: x ** 2, range(10)))

def transform_lines(func, input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        lines = in_file.readlines()
        out_file.write(''.join(apply_to_each(func, lines)))
    print('Done!')

transform_lines(lambda x: x.upper(), 'source.txt', 'output.txt')
