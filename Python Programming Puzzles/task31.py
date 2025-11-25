def param_count(*args):
    return len(args)

print(param_count(1, 2, 3, 4, 5))
print(param_count('hello'))
print(param_count())

def my_zip(*args):
    min_length = min([len(arg) for arg in args])
    return (tuple(arg[i] for arg in args) for i in range(min_length))

print(list(my_zip([1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8], ['1', '2', '3', '4', '5'])))
