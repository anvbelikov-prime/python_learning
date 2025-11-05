def my_max(seq):
    res = seq[0]
    for e in seq:
        if e > res:
            res = e
    return res

print(my_max('abc'))
print(my_max([1, 2, 3]))
