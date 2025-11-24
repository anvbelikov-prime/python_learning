def remove_vowels(input_str):
    return ''.join([c for c in input_str if c.lower() not in 'aeiou'])

print(remove_vowels('Hello, World!'))
print(remove_vowels('aeiouAEIOU'))
print(remove_vowels('zzzvvvlllkkk'))
