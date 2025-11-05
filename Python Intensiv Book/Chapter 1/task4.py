def hex_to_decimal(hex_num):
    res = 0
    hex_num = str(hex_num)
    hex_num = hex_num.strip()
    hex_num = hex_num.lower()
    hex_num = hex_num.replace('0x', '')
    for n, c in enumerate(reversed(hex_num)):
        if 48 <= ord(c) <= 57:
            digit = ord(c) - 48
        elif 97 <= ord(c) <= 102:
            digit = ord(c) - 97 + 10
        res += digit * (16 ** n)
    return res

def triangle_name():
    name = input("Введите свое имя: ")
    for i in range(0, len(name) + 1):
        print(name[:i])

triangle_name()