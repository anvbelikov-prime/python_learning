def sum_sort(lst):
    return sorted(lst, key=sum)

print(sum_sort([[100], [1, 2, 3], [10, 20, 30], [1, 1, 1, 1]]))
