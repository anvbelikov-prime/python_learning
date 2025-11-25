def xor(input_a, input_b):
    res = ''
    for a, b in zip(input_a, input_b):
        if a == b:
            res += '0'
        else:
            res += '1'
    return res

print(xor('1111', '1111'))
print(xor('1111', '0000'))
print(xor('1101', '00010'))
