roman_map = {  1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",  90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",  4: "IV", 1: "I" }
reversed_roman_map = {value: key for key, value in roman_map.items()}

def int_to_roman(input_int):
    res = ''
    sorted_keys = sorted(roman_map.keys(), reverse=True)
    while input_int > 0:
        for key in sorted_keys:
            if key <= input_int:
                res += roman_map[key]
                break
        input_int -= key
    return res

print(int_to_roman(4))
print(int_to_roman(27))
print(int_to_roman(4999))

def roman_to_int(input_str):
    res = 0
    i = 0
    key = ''
    while i < len(input_str):
        if (input_str[i] == 'C' and i < len(input_str) - 1 and input_str[i + 1] in 'MD') or \
        (input_str[i] == 'X' and i < len(input_str) - 1 and input_str[i + 1] in 'CL') or \
        (input_str[i] == 'I' and i < len(input_str) - 1 and input_str[i + 1] in 'XV'):
            key = input_str[i:i+2]
            i += 2
        else:
             key = input_str[i]
             i += 1
        res += reversed_roman_map[key]
    return res

print(roman_to_int('IV'))
print(roman_to_int('XXVII'))
print(roman_to_int('MMMMCMXCIX'))

def int_roman_converter(to_convert):
    if isinstance(to_convert, int):
        return int_to_roman(to_convert)
    elif isinstance(to_convert, str):
        return roman_to_int(to_convert)
    else:
        return None
    
for i in range(1, 5000):
    if not (int_roman_converter(int_roman_converter(i)) == i):
        print(f'{i} has error in convertation!')
