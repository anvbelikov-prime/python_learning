def get_parantheses_groups(input_str):
    open_num = 0
    left = 0
    res = []
    input = ''.join([c for c in input_str if c in '()'])
    for i in range(len(input)):
        if input[i] == '(':
            if open_num == 0:
                left = i
            open_num += 1
        if input[i] == ')':
            open_num -= 1
            if open_num == 0:
                res.append(input[left: i + 1])
    return res

print(get_parantheses_groups('(( ))  (( ) ) (  ((     )))'))
print(get_parantheses_groups('( ( ( ( ( ( ) ) ) ) ) ) '))
print(get_parantheses_groups(''))
print(get_parantheses_groups('() (()) ((())) () (())'))
print(get_parantheses_groups('(() (()) ((())) () (()))'))