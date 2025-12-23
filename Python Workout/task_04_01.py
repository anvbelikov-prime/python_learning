def get_hex_digit(d):
    if ord('0') <= ord(d) <= ord('9'):
        return ord(d) - ord('0')
    elif ord('a') <= ord(d) <= ord('f'):
        return ord(d) - ord('a') + 10
    elif ord('A') <= ord(d) <= ord('F'):
        return ord(d) - ord('A') + 10

def hex_output(h):
    res = 0
    h = h.replace('0x', '')
    for idx, digit in enumerate(reversed(str(h))):
        res += get_hex_digit(digit) * pow(16, idx)
    return res

print(hex_output('0x50'))
print(hex_output('1'))
print(hex_output('AF'))
