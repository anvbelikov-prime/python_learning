import collections

def get_code_stats(file_path):
    stats = collections.defaultdict(list)
    ip = ''
    code = ''
    with open(file_path, 'r') as f:
        for line in f:
            ip, rest = line.strip().split(' - - ')
            code, *_ = rest[rest.find(']') + 3 + rest[rest.find(']') + 3:].find('"') + 2:].split()
            stats[code].append(ip)
    for k in stats:
        print(f'{k}: {sorted(list(set(stats[k])))}')

get_code_stats('mini-access-log.txt')
