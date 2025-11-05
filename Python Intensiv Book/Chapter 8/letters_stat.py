def calculate_letter_stats(word):
    res = dict.fromkeys(['isdigit', 'isalpha', 'isspace'], 0)
    for w in word:
        if w.isdigit():
            res['isdigit'] += 1
        elif w.isalpha():
            res['isalpha'] += 1
        elif w.isspace():
            res['isspace'] += 1
    return res

def func_keys(d, func):
    return {func(key) for key in d.keys()}
