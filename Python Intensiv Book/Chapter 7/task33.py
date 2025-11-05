def transform_values(func, d):
    return {k: func(v) for k, v in d.items()}

# print(transform_values(lambda x: x ** 2, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

def transform_values_v2(func1, func2, d):
    return {k: func1(v) for k, v in d.items() if func2(k, v)}

# print(transform_values_v2(lambda x: x ** 3, lambda x, y: x not in 'bc' and y != 5, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 7}))

def create_logins_ids_dict(file_path):
    with open(file_path, 'r') as f:
        return {line.strip().split(':')[0]: line.strip().split(':')[2] for line in f if not line.startswith('#') and len(line.strip().split(':')) > 2}
    
# print(create_logins_ids_dict('passwd_example.txt'))
