from collections import Counter

def pig_latin_v3(word):
    if word[0].lower() in 'aeiouy':
        if word[-1].isalnum():
            return word + 'way'
        else:
            return word[:-1] + 'way' + word[-1]
    else:
        if word[0].isupper():
            new_begining = word[1:].capitalize()
        else:
            new_begining = word[1:]
        if word[-1].isalnum():
            return new_begining + word[0].lower() + 'ay'
        else:
            return new_begining[:-1] + word[0].lower() + 'ay' + new_begining[-1]
    
def pig_latin_translate(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            print(' '.join([pig_latin_v3(word) for word in line.split()]))

# pig_latin_translate('text.txt')

def func_file(input_file, func):
    with open(input_file, 'r') as f:
        return ' '.join(func(word) for line in f for word in line.split())
    
# print(func_file('text.txt', str.upper))

dict_lst = [{'name':'B', 'age':24}, {'name':'C', 'age':18}, {'name':'D', 'age':10}, {'name':'F', 'age':12}, {'name':'G', 'age':7}]

def dict_lst_to_lst(dict_lst):
    return [(k, v) for d in dict_lst for k, v in d.items()]

# print(dict_lst_to_lst(dict_lst))

dict_lst = [{'name':'B', 'hobbies':['a', 'b', 'c']}, {'name':'C', 'hobbies':['a', 'e']}, {'name':'D', 'hobbies':['hh', 'jj']}, {'name':'F', 'hobbies':['a', 'b']}, {'name':'G', 'hobbies':['jj']}]

def most_popular_hobbies(dict_lst):
    return Counter([hobby for d in dict_lst for k, v in d.items() if k == 'hobbies' for hobby in v]).most_common(3)

print(most_popular_hobbies(dict_lst))
