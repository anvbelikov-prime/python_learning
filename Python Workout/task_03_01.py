def float_cut(f, before, after):
    return float(str(f).split('.')[0][-before:] + '.' + str(f).split('.')[1][:after])

print(float_cut(1234.5678, 2, 3))
print(float_cut(1234.5678, 1, 2))
print(float_cut(1234.5678, 3, 3))
print(float_cut(1234.5678, 10, 10))
