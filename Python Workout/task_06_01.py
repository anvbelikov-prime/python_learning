def create_sentence(file_path):
    result = []
    with open(file_path, 'r') as f:
        idx = 0
        for line in f:
            result.append(line.strip().split()[idx])
            idx += 1
    return ' '.join(result)

print(create_sentence('test.txt'))
