def get_column(input_board, j, n=3):
    return [input_board[i][j] for i in range(n)]

def get_row(input_board, i, n=3):
    return input_board[i]

def get_prime_diagonal(input_board, n=3):
    return [input_board[i][i] for i in range(n)]

def get_second_diagonal(input_board, n=3):
    return [input_board[i][n - 1 - i] for i in range(n)]

def get_num_of_different_elements(lst):
    return len(set(lst))

def get_tic_tac_toe_winner(input_board):
    if get_num_of_different_elements(get_prime_diagonal(input_board)) == 1:
        return get_prime_diagonal(input_board)[0]
    elif get_num_of_different_elements(get_second_diagonal(input_board)) == 1:
        return get_prime_diagonal(input_board)[0]
    else:
        for i in range(3):
            if get_num_of_different_elements(get_row(input_board, i)) == 1:
                return get_row(input_board, i)[0]
        for j in range(3):
            if get_num_of_different_elements(get_column(input_board, j)) == 1:
                return get_column(input_board, j)[0]
        return None
    
print(get_tic_tac_toe_winner(
    [
        ['X', 'X', 'X'],
        ['0', 'X', '0'],
        ['X', '0', '0'],
    ]
))

print(get_tic_tac_toe_winner(
    [
        ['X', '0', '0'],
        ['0', '0', ''],
        ['X', '0', '0'],
    ]
))

print(get_tic_tac_toe_winner(
    [
        ['X', '0', '0'],
        ['0', 'X', ''],
        ['X', '0', '0'],
    ]
))
