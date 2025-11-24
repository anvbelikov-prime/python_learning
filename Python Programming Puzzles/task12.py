def string_to_ascii(input_str):
    return [ord(c) for c in input_str]

def ascii_to_string(input_ascii_codes):
    return ''.join(chr(c) for c in input_ascii_codes)

print(string_to_ascii('Programming Puzzles!'))
print(string_to_ascii(''))
print(string_to_ascii('aA'))

print('------------------------------')
print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103, 32, 80, 117, 122, 122, 108, 101, 115, 33]))
print(ascii_to_string([]))
print(ascii_to_string([97, 65]))
