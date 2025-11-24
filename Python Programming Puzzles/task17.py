def check_if_string_happy(input_str):
    if len(input_str) < 3:
        return True
    else:
        i = 0
        while (i + 3) <= len(input_str):
            if len(set(input_str[i:i+3])) < 3:
                return False
            i += 1
        return True
    
print(check_if_string_happy('abcdefg'))
print(check_if_string_happy('abcabcabcabcabc'))
print(check_if_string_happy('hello'))
