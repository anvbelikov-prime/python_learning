def bitwise_add(num_one, num_two):
    while num_two != 0:
        sum_without_carry = num_one ^ num_two
        carry = (num_one & num_two) << 1
        num_one = sum_without_carry
        num_two = carry
    return num_one

print(bitwise_add(5, 7))
print(bitwise_add(-1, -2))
print(bitwise_add(5, 0))
