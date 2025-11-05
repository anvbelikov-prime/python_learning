def get_passwd_stats(file_path):
    res = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            name, _, id, *_, home, shell = line.strip().split(':')
            res[name] = {'id': id, 'home_dir': home, 'shell': shell}
    return res

print(get_passwd_stats('linux-etc-passwd.txt'))
