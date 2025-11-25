def find_zero_sum_triplets(input_nums):
    result = []
    for i in range(len(input_nums)):
        for j in range(len(input_nums)):
            for k in range(len(input_nums)):
                if (i < j < k) and ((input_nums[i] + input_nums[j] + input_nums[k]) == 0):
                    result.append((i, j, k))
    return result

print(find_zero_sum_triplets([1, 2, 3, 4, 5]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9, -9]))
