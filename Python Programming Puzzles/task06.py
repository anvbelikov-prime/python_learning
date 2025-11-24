def filter_even_length_string(input_strs):
    return [s for s in input_strs if len(s) % 2 == 0]

print(filter_even_length_string(['cat', 'dog', 'fish', 'elephant']))
print(filter_even_length_string(['q', 'w', 'e', 'r', 't', 'y']))
print(filter_even_length_string(['qq', 'ww', 'ee', 'rr', 't', 'yy']))
