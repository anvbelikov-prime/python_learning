import decimal

def correct_sum(s1, s2):
    return decimal.Decimal(s1) + decimal.Decimal(s2)

print(0.1 + 0.2)
print(correct_sum('0.1', '0.2'))
