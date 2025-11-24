def get_second_largest_number(input_nums):
    if len(input_nums):
        lst = sorted(input_nums, reverse=True)
        max_num = lst[0]
        for num in lst:
            if num < max_num:
                return num
        return None
    else:
        return None
    
print(get_second_largest_number([1, 2, 3, 4, 5]))
print(get_second_largest_number([1]))
print(get_second_largest_number([1, 1]))
print(get_second_largest_number([]))
print(get_second_largest_number([3, 45, 345, 435, 345, 43, 56, 34, 234, 34]))
