def find_adjacent_nodes(adj_matrix, start_node):
    return [idx for idx, val in enumerate(adj_matrix[start_node]) if val == 1]

print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 0))
print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 1))
print(find_adjacent_nodes([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]], 1))
