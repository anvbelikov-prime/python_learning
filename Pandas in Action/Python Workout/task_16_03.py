def get_one_letter_keys_or_values(k,v):
    return (len(k) == 1) or (len(v) == 1)

def dict_partition(d, f):
    res1 = {}
    res2 = {}
    for k, v in d.items():
        if f(k,v):
            res1[k] = v
        else:
            res2[k] = v
    return res1, res2

print(dict_partition({'a':'bb', 'b':'ccc', 'cc':'ddd'}, get_one_letter_keys_or_values))
