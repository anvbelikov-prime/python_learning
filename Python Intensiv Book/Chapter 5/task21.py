import os
import collections
import hashlib
import time
import datetime

def find_longest_word(file_path):
    max_word = ''
    max_length = 0
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                if len(word) > max_length:
                    max_word = word
                    max_length = len(word)
    return (max_word, max_length)

# print(find_longest_word("task21.py"))

def all_longest_words(path):
    res = {}
    items = os.listdir(path)
    for item in items:
        if os.path.isfile(path + '/' + item) and not item.startswith('.'):
            res[item] = find_longest_word(path + '/' + item)[0]
    return res

# print(all_longest_words('./test'))

def get_file_hash(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        m = hashlib.md5()
        m.update(text.encode())
    return m.hexdigest()

# print(get_file_hash("task21.py"))

def hash_files(path):
    return {item: get_file_hash(os.path.join(path,item)) for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')}

# print(hash_files("./test"))

def show_files(path):
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and not file.startswith('.')]
    # return files, time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(os.stat(path).st_mtime))
    return files, f'{(datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.fromtimestamp(os.stat(path).st_mtime)).days} day(s)'

print(show_files("./test"))
