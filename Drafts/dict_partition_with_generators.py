def is_one_letter_word(word):
    return True if len(word) == 1 else False

def dict_partition(d, f):
    return {k:v for k,v in d.items() if f(v)}, {k:v for k,v in d.items() if not f(v)}

print(dict_partition({'a':'a', 'b':'bb', 'c':'c', 'd':'ddd'}, is_one_letter_word))
