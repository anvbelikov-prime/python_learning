from collections import defaultdict

def passwd_to_dict(file_path):
    res = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(('#', '\n')):
                continue
            if len(line) == 0:
                continue
            line = line.split(':')
            res[line[0]] = int(line[2])
    return res

# print(passwd_to_dict("passwd_example.txt"))

def passwd_to_shell_dict(file_path):
    res = defaultdict(list)
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue
            line = line.split(':')
            res[line[-1]].append(line[0])
    return res

# print(passwd_to_shell_dict("passwd_example.txt"))

def passwd_to_users_dict(file_path):
    res = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue
            line = line.split(':')
            res[line[0]] = {'id': line[2], 'shell': line[-1], 'home': line[-2]}
    return res

# print(passwd_to_users_dict("passwd_example.txt"))

def delimiters_dict():
    res = defaultdict(list)
    num_line = input("Введите целые числа через пробел: ").strip().split()
    for num in num_line:
        if not num.isdigit():
            continue
        num = int(num)
        for i in range(1, num):
            if num % i == 0 and i != 1:
                res[num].append(i)
    return res

print(delimiters_dict())
