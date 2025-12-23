def get_final_line(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f][-1]

def get_final_line_v2(file_path):
    res = ''
    with open(file_path, 'r') as f:
        for line in f:
            res = line.strip()
    return res

print(get_final_line('test.txt'))
print(get_final_line_v2('test.txt'))
