def print_triangle(number_of_levels, symbol):
    if number_of_levels < 1:
        print('')
    else:
        length = number_of_levels * 2 - 1
        for level in range(number_of_levels):
            symbols =  2 * (level + 1) - 1
            spaces = (length - symbols) // 2
            print(' ' * spaces + symbol * symbols + ' ' * spaces)

print_triangle(4, '*')
print('--------------------')
print_triangle(3, '*')
print('--------------------')
print_triangle(1, '|')
print('--------------------')
print_triangle(2, '|')
print('--------------------')
print_triangle(20, '|')
