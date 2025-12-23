def plus_minus(seq):
    i = 1
    res = seq[0]
    for e in seq[1:]:
        res += i * e
        i *= -1
    return res

print(plus_minus([10, 20, 30, 40, 50, 60]))
