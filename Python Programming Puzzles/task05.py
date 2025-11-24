def get_longest_string(input_strs):
    if len(input_strs):
        max_length = 0
        max_str = input_strs[0]
        for s in input_strs:
            if len(s) > max_length:
                max_length = len(s)
                max_str = s
        return max_str
    else:
        return None
    
print(get_longest_string(['cat', 'dog', 'bird', 'lizard']))
print(get_longest_string(['cat', 'dog', 'bird', 'wolf']))
print(get_longest_string(['a', 'b', 'c', 'd']))
