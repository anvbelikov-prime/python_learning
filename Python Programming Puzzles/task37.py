def gcd(num_one, num_two):
    res = 1
    for i in range(1, min(num_one, num_two) + 1):
        if num_one % i == 0 and num_two % i  == 0:
            res = i
    return res

print(gcd(36, 8))
print(gcd(5, 25))
print(gcd(5, 26))
print(gcd(8, 16))
