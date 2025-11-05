import os

print(os.path.abspath('chapter15.py'))

f = open('test_file.txt', 'w')
f.write('Hello!\n')
f.write('This is a test file!\n')
f.writelines([str(i) for i in range(3)])
f.write('\n')
f.close()

f = open('test_file.txt', 'a')
f.write('This is an addition!\n')
f.close()

with open('test_file.txt', 'r') as f:
    for line in f:
        print(line.strip())

import shutil

shutil.copyfile('test_file.txt', 'test_file2.txt') # копирование только содержимого без прав доступа и мета данных
shutil.copy('test_file.txt', 'test_file3.txt') # копирование с правами доступа без метаданных
shutil.copy2('test_file.txt', 'test_file4.txt') # полное копирование

shutil.move('test_file.txt', 'test_file_move.txt')

os.rename('test_file_move.txt', 'test_file.txt')

os.remove('test_file2.txt')
os.remove('test_file3.txt')
os.remove('test_file4.txt')

print('-' * 50)

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

os.chdir('Python Basics - Koltsov')

print(os.getcwd())

print('-' * 50)

os.mkdir('my_test_dir')
shutil.rmtree('my_test_dir')

print(os.listdir(os.getcwd()))
print(os.path.isfile('chapter9.py'))
print(os.path.isfile('chapter_modules'))
print(os.path.isdir('chapter15.py'))
print(os.path.isdir('chapter_modules'))

print('-' * 50)

for e in os.walk(os.getcwd(), topdown=True):
    print(e)

print('-' * 50)

for e in os.walk(os.getcwd(), topdown=False):
    print(e)

print('-' * 50)

import csv

headers = ['UserID', 'FirstName', 'LastName']
users = [('user1', 'Anton', 'Belikov'), ('user2', 'Luda', 'Artemieva')]

with open('users.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(users)

with open('users.csv', 'r') as f:
    for line in f:
        print(line.strip())

with open('users.csv', 'r') as f:
    f_csv = csv.reader(f)
    for line in f_csv:
        print(line)

print('-' * 50)

import json

data = {'user': 'admin', 'first_name': 'Anton', 'last_name': 'Belikov'}

print(json.dumps(data))

json_s = json.dumps(data)

data1 = json.loads(json_s)

print(data1)

with open('users.json', 'w') as f:
    json.dump(data, f)

with open('users.json', 'r') as f:
    data2 = json.load(f)

print(data2)
