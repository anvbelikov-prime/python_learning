def filter_strings_containing_a(input_strs):
    return [s for s in input_strs if 'a' in s.lower()]

print(filter_strings_containing_a(['apple', 'banana', 'cherry', 'date']))
print(filter_strings_containing_a([]))
print(filter_strings_containing_a(['bbbb', 'ccccccc']))
print(filter_strings_containing_a(['wAve', 'wave', 'vvvv']))
