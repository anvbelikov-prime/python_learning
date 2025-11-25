def rotate_list_left(input_list, rotate_amount):
    shift = rotate_amount % len(input_list)
    return input_list[shift:] + input_list[:shift]

print(rotate_list_left([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 5))
print(rotate_list_left([1, 2, 3, 4, 5], 7))
print(rotate_list_left([1, 2, 3, 4, 5], 0))
