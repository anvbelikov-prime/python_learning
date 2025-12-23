import collections

def shells(file_path):
    shells_dict = collections.defaultdict(list)
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().startswith('#'):
                continue
            elif len(line.strip()) == 0:
                continue
            else:
                shells_dict[line.strip().split(':')[-1]].append(line.strip().split(':')[0])
    return sorted(list(shells_dict.items()), key=lambda sh: len(sh[1]), reverse=True)

def show_shells(lst):
    for i in lst:
        print(f'{i[0]} with {len(i[1])} times by {sorted(i[1])} users')

show_shells(shells('linux-etc-passwd.txt'))
