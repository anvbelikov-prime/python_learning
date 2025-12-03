def matrix_multiply(left_matrix, right_matrix):
    def get_matrix_row(matrix, i):
        return matrix[i]
    
    def get_matrix_col(matrix, j):
        return [matrix[i][j] for i in range(len(matrix))]
    
    def get_scalar_mult(lst1, lst2):
        res = 0
        for i in range(len(lst1)):
            res += (lst1[i] * lst2[i])
        return res
    
    left_rows = len(left_matrix)
    right_rows = len(right_matrix)
    left_cols = len(left_matrix[0])
    right_cols = len(right_matrix[0])
    if left_cols != right_rows:
        return None
    result = [[0 for j in range(right_cols)] for i in range(left_rows)]
    for i in range(left_rows):
        for j in range(right_cols):
            result[i][j] = get_scalar_mult(get_matrix_row(left_matrix, i), get_matrix_col(right_matrix, j))
    return result

print(matrix_multiply([[2, 3], [4, 5]], [[10, 15], [5, 1]]))
print(matrix_multiply([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], [[1, 2], [3, 4], [5, 6], [7,8], [9, 10], [11, 12]]))
print(matrix_multiply([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], [[1, 2, 3]]))
