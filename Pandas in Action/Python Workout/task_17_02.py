import collections

def get_unique_codes_by_ip(file_path):
    res = collections.defaultdict(set)
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            ip, code = parts[0], parts[8]
            res[ip].add(code)
    return res

print(get_unique_codes_by_ip('mini-access-log.txt'))
