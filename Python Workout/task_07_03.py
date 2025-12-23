def encode_symbols(url):
    res = ''
    for c in url:
        if not c.isalnum():
            res += ('%' + hex(ord(c)).replace('0x', ''))
        else:
            res += c
    return res

print(encode_symbols('This is a (string)\twith [some] <symbols>'))
