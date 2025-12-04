def binary_search(sorted_list, value_to_find):
    if not sorted_list:
        return -1
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (right + left) // 2
        if sorted_list[middle] == value_to_find:
            return middle
        elif sorted_list[middle] > value_to_find:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binary_search([1, 2, 3, 4, 5], 0))