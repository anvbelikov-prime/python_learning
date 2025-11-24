def filter_strings_with_vowels(input_strs):
    return [s for s in input_strs if len(set(s.lower()) & set('aeiou')) > 0]

print(filter_strings_with_vowels(['apple', 'banana', 'zyxvb']))
print(filter_strings_with_vowels([]))
print(filter_strings_with_vowels(['q', 'w', 'e', 'r', 't', 'y']))
