def rot13(input_str):
    def get_new_symbol(c, left, right):
        if right - ord(c) >= 13:
            return chr(ord(c) + 13)
        else:
            return chr(left + 13 - right + ord(c) - 1)
        
    def transform_char(c):
        if ord('a') <= ord(c) <= ord('z'):
            return get_new_symbol(c, ord('a'), ord('z'))
        elif ord('A') <= ord(c) <= ord('Z'):
            return get_new_symbol(c, ord('A'), ord('Z'))
        else:
            return c
        
    return ''.join([transform_char(c) for c in input_str])

print(rot13('Hello world!'))
print(rot13('Cool puzzles!'))
print(rot13('12345!@$%'))
print(rot13('Y'))
