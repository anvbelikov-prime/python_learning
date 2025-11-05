def passwd_to_dict(file_path):
    res = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or line.strip() == '':
                continue
            name, _, id, *_ = line.strip().split(':')
            res[name] = id
    return res

print(passwd_to_dict('linux-etc-passwd.txt'))
