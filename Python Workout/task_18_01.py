def sum_file(file_path):
    res = 0
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                if word.isdigit():
                    res += int(word)
    return res

print(sum_file('test.txt'))
