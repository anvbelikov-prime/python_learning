def supervocalic(file_path):
    with open(file_path, 'r') as f:
        return {word for line in f for word in line.strip().split() if {'a', 'e', 'i', 'o', 'u'} < set(word.lower())}
    
# print(len(supervocalic('words.txt')))

def get_different_shells(file_path):
    with open(file_path, 'r') as f:
        return {line.strip().split(':')[-1] for line in f if not line.startswith('#')}
    
# print(get_different_shells('passwd_example.txt'))

def get_different_word_lengths(file_path):
    with open(file_path, 'r') as f:
        return {len(word) for line in f for word in line.strip().split()}
    
# print(get_different_word_lengths('words.txt'))

family = ['Anton', 'Luidmila', 'Tatiyana']

def get_different_letters(lst):
    return {w.lower() for word in lst for w in word if w.isalpha()}

print(get_different_letters(family))
