def my_zip(input_list_a, input_list_b):
    length = min(len(input_list_a), len(input_list_b))
    return ((input_list_a[i], input_list_b[i]) for i in range(length))

print(list(my_zip([1, 2, 3, 4], [5, 6, 7, 8, 9])))
print(list(my_zip([], [])))
print(list(my_zip(['a', 2, True], [False, [1, 2], ('a', {2}), 'd'])))
