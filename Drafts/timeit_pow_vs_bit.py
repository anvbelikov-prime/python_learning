import timeit

t = timeit.Timer('int(0b1 << 100)')

bit = t.timeit()

t = timeit.Timer('pow(2, 100)')

p = t.timeit()

print(bit, p, p / bit)
