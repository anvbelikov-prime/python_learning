def join_members(range_object):
    return ','.join(str(i) for i in range_object)

# print(join_members(range(15)))

def join_members_ten(range_object):
    return ','.join(str(i) for i in range_object if 0 <= i <= 10)

# print(join_members_ten(range(15)))

def sum_hex(lst):
    return sum(int(i, 16) for i in lst )

print(sum_hex(['0x1', '0x2', '0x10']))

strings = [
    'abc def',
    'jkl ghi'
]

def reverse_words(lst):
    return [' '.join(line.split()[::-1]) for line in lst]

print(reverse_words(strings))
