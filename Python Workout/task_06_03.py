def find_errors(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if ' 404 ' in line.strip():
                print(line.split(' - - ')[0])

find_errors('mini-access-log.txt')
