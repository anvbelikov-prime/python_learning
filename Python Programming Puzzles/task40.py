def insertion_sort(input_nums):
    res = []
    for num in input_nums:
        for i in range(len(res)):
            if res[i] > num:
                res.insert(i, num)
                break
        else:
            res.append(num)
    return res

def insertion_sort_v2(input_nums):
    for i in range(1, len(input_nums)):
        value_to_insert = input_nums[i]
        previous_index = i - 1
        while (previous_index >= 0) and (input_nums[previous_index] > value_to_insert):
            input_nums[previous_index + 1] = input_nums[previous_index]
            previous_index -= 1
        input_nums[previous_index + 1] = value_to_insert
    return input_nums

print(insertion_sort_v2([5, 10, 9, 11, 4]))
print(insertion_sort_v2([1, 2, 3, 4, 5]))
print(insertion_sort_v2([-1, -2, -3, -4, -5]))
print(insertion_sort_v2([5, 5, 5, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5]))
