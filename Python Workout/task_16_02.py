def create_dict(*args):
    if len(args) % 2 != 0:
        return dict()
    else:
        keys = args[0::2]
        values = args[1::2]
        return dict(list(zip(keys, values)))
    
print(create_dict('a', 1, 'b', 2, 'c', 3))
