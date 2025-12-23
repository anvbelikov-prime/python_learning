def hex_output(h):
    res = 0
    h = h.replace('0x', '')
    for idx, digit in enumerate(reversed(str(h))):
        res += int(digit, 16) * pow(16, idx)
    return res

print(hex_output('0x50'))
print(hex_output('1'))
print(hex_output('AF'))
