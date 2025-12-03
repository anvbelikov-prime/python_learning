def tower_of_hanoi(num_disks, source, aux, target):
    source_lst = [i for i in range(num_disks, 0, -1)]
    aux_lst = []
    target_lst = []
    steps = 0

    def print_row(i):
        source_element = '' if i > len(source_lst) else str(source_lst[i-1])
        aux_element = '' if i > len(aux_lst) else str(aux_lst[i-1])
        target_element = '' if i > len(target_lst) else str(target_lst[i-1])
        print(f'{source_element:^7}   {aux_element:^7}   {target_element:^7}')
        

    def print_state():
        print(f'Step: {steps}')
        print()
        for i in range(num_disks, 0, -1):
            print_row(i)
        print(f'{source:^7}    {aux:^7}    {target:^7}')
        print()
        print('-' * 20)

    def move_elements(num, start, middle, final):
        if num == 1:
            elem = start[-1]
            start.remove(elem)
            final.append(elem)
            nonlocal steps
            steps += 1
            print_state()
        else:
            move_elements(num - 1, start, final, middle)
            move_elements(1, start, middle, final)
            move_elements(num - 1, middle, start, final)

    print_state()
    move_elements(num_disks, source_lst, aux_lst, target_lst)

tower_of_hanoi(4, 'source', 'aux', 'target')
