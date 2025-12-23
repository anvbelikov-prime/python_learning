def get_col_sum(file_path):
    res = 0
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue
            part1, part2 = parts
            if part1.isdigit() and part2.isdigit():
                res += (int(part1) * int(part2))
    return res

print(get_col_sum('col_num.txt'))
