def my_zip(*seq):
    res = []
    length = len(seq[0])
    for i in range(length):
        res.append(tuple(s[i] for s in seq))
    return res

print(my_zip([1, 2, 3], 'abc'))
