import itertools

def solve_knapsack_problem(items, knapsack_capacity):
    combinations = []
    
    def is_good_capacity(items_lst):
        res = 0
        for i in items_lst:
            res += i[0]
        return res <= knapsack_capacity

    def sum_value(items_lst):
        res = 0
        for i in items_lst:
            res += i[1]
        return res
    
    for i in range(1, len(items) + 1):
        combs = list(itertools.combinations(items, i))
        combs = filter(is_good_capacity, combs)
        combinations.extend(combs)

    if combinations:
        combinations.sort(key=sum_value, reverse=True)
        max_value = sum_value(combinations[0])
        return max_value
    else:
        return 0
    
print(solve_knapsack_problem([(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)], 5))
print(solve_knapsack_problem([(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)], 0))
print(solve_knapsack_problem([], 5))
