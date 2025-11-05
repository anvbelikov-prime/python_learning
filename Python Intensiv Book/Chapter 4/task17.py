import os

def how_many_different_numbers(num_lst):
    return len(set(num_lst))

# print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))

def unique_extensions():
    return {os.path.splitext(file)[-1] for file in os.listdir()}

print(unique_extensions())
