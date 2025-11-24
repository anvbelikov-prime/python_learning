def filter_type_str(input_list):
    return [e for e in input_list if type(e) == str]

print(filter_type_str(['hello', 1, 2, 'www']))
print(filter_type_str([]))
print(filter_type_str([1, 2, 3, 4, 5]))

def filter_type_str_v2(input_list):
    return [e for e in input_list if isinstance(e, str)]

print(filter_type_str_v2(['hello', 1, 2, 'www']))
print(filter_type_str_v2([]))
print(filter_type_str_v2([1, 2, 3, 4, 5]))

def filter_type_str_v3(input_list):
    return [e for lst in input_list if len(lst) == 4 for e in lst if isinstance(e, str)]

print(filter_type_str_v3([[1, 2, 3], ['a', 4, 5, 6], [7, 'bb', 'ccc', 8], [9], ['dddd', 10]]))
