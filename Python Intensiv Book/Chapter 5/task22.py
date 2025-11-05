import csv
import operator
import random

def passwd_to_csv(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        wr = csv.writer(out_file, delimiter='\t')
        r = csv.reader(in_file, delimiter=':')
        for line in r:
            if len(line) < 3:
                continue
            if line[0].startswith('#'):
                continue
            wr.writerow((line[0], line[2]))
    print('Done!')
    
# passwd_to_csv("passwd_example.txt", "passwd.csv")

def passwd_to_csv_custom(input_file, output_file):
    nums = input("Введите номера колонок: ").split()
    if not len(nums):
        print("Нет колонок!")
        return
    getter = operator.itemgetter(*[int(i) for i in nums])
    delimiter = input("Введите символ разделителя: ")
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        wr = csv.writer(out_file, delimiter=delimiter)
        r = csv.reader(in_file, delimiter=':')
        for line in r:
            if len(line) < 3:
                continue
            if line[0].startswith('#'):
                continue
            wr.writerow(getter(line))
    print('Done!')

# passwd_to_csv_custom("passwd_example.txt", "passwd.csv")

example_dict = {'a':1, 'b':'2', 'c':3.5}

def dict_to_scv(input_dict, output_file):
    if not input_dict:
        return
    with open(output_file, 'w') as out_file:
        wr = csv.writer(out_file)
        wr.writerow(('key', 'value', 'type'))
        for k, v in input_dict.items():
            wr.writerow((k, v, type(v).__name__))
    print('Done!')

# dict_to_scv(example_dict, "dict_to_csv.csv")

def create_num_csv_file(output_file, num_rows=10):
    with open(output_file, 'w') as f:
        wr = csv.writer(f)
        for i in range(0, num_rows):
            wr.writerow((random.randint(10, 100) for j in range(10)))
    print('Done!')

def calc_num_csv_file(input_file):
    with open(input_file, 'r') as f:
        r = csv.reader(f)
        for line in r:
            print(f'Сумма: {sum((int(i) for i in line))}, среднее: {sum((int(i) for i in line)) / len(line)}')

file_name = "calc_nums.csv"
create_num_csv_file(file_name)
calc_num_csv_file(file_name)
