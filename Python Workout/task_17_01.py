def get_unique_ips(file_path):
    res = set()
    with open(file_path, 'r') as f:
        for line in f:
            ip, _ = line.strip().split(' - - ')
            res.add(ip)
    return sorted(list(res))

print(get_unique_ips('mini-access-log.txt'))
