def first_last(seq):
    return seq[0::len(seq)-1]

def firstlast(seq):
    return seq[:1] + seq[-1:]

# print(firstlast('abcd'))
# print(firstlast([1, 2, 3, 4, 5]))
# print(firstlast((1, 2, 3, 4, 5)))

def even_odd_sums(seq):
    return [sum(seq[0::2]), sum(seq[1::2])]

# print(even_odd_sums([10, 20, 30, 40, 50, 60]))

def plus_minus(seq):
    return sum(seq[0::2]) - sum(seq[1::2])

# print(plus_minus([10, 20, 30, 40, 50, 60]))

def my_zip(*args):
    return [tuple((arg[i] for arg in args)) for i in range(0, len(args[0]))]
            

print(my_zip([1, 2, 3, 4, 5, 6], ('a', 'b', 'c', 'd', 'e', 'f'), 'qwerty'))
