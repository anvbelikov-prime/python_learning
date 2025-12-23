import collections

def shells(file_path):
    shells_lst = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().startswith('#'):
                continue
            elif len(line.strip()) == 0:
                continue
            else:
                shells_lst.append(line.strip().split(':')[-1])
    return collections.Counter(shells_lst).most_common()

def show_shells(lst_counter):
    for i in lst_counter:
        print(f'{i[0]} with {i[1]} times')

show_shells(shells('linux-etc-passwd.txt'))
