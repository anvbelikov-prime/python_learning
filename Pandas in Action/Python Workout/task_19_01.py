import collections

def shell_stats(file_path):
    res = collections.defaultdict(set)
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            user, *_, shell = line.strip().split(':')
            res[shell].add(user)
    return res

print(shell_stats('linux-etc-passwd.txt'))
