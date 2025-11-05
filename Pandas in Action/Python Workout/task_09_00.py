def first_last(seq):
    return seq[::len(seq)-1]

print(first_last('abc'))
print(first_last([1, 2, 3, 4]))
print(first_last((1, 2, 3, 4, 5, 6, 7)))
