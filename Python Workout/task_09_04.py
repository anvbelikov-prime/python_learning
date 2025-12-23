def even_odd_sums(seq):
    i = 0
    res_even = 0
    res_odd = 0
    for e in seq:
        if i % 2 == 0:
            res_even += e
        else:
            res_odd += e
        i += 1
    return [res_even, res_odd]

print(even_odd_sums([10, 20, 30, 40, 50, 60]))
