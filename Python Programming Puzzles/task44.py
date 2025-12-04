def partition(input_list, low, high):
    base_index = low - 1
    base = input_list[high]
    for idx in range(low, high):
        if input_list[idx] <= base:
            base_index += 1
            input_list[base_index], input_list[idx] = input_list[idx], input_list[base_index]
    base_index += 1
    input_list[base_index], input_list[high] = input_list[high], input_list[base_index]
    return base_index

def quick_sort(input_list, low, high):
    if low < high:
        base_index = partition(input_list, low, high)
        quick_sort(input_list, low, base_index - 1)
        quick_sort(input_list, base_index + 1, high)
    return input_list

unsorted_list = [5, 7, 8, 1, 2, 4, 99, 77, 56, 43, 12, 98]
print(quick_sort(unsorted_list, 0, len(unsorted_list) - 1))

unsorted_list = [10, 5, -10, -5, 0]
print(quick_sort(unsorted_list, 0, len(unsorted_list) - 1))

unsorted_list = []
print(quick_sort(unsorted_list, 0, 0))
