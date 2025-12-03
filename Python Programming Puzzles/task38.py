import itertools

def find_pairs_summing_to_target(input_nums, target):
    res = set()
    for i in range(len(input_nums)):
        for j in range(i + 1, len(input_nums)):
            if input_nums[i] + input_nums[j] == target:
                res.add((input_nums[i], input_nums[j]))
    res = list(res)
    res.sort(key=lambda x: x[0])
    return res

def find_pairs_summing_to_target_v2(input_nums, target):
    res = list({comb for comb in itertools.combinations(input_nums, 2) if comb[0] + comb[1] == target})
    res.sort(key=lambda x: x[0])
    return res

print(find_pairs_summing_to_target_v2([5, 5, 5, 5], 10))
print(find_pairs_summing_to_target_v2([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(find_pairs_summing_to_target_v2([11, 12, 13, 14, 15], 5))
