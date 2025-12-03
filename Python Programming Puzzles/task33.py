def find_primes(input_nums):
    def is_prime(num):
        if num in [1, 2]:
            return True
        else:
            if num <= 0:
                return False
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
    
    return [num for num in input_nums if is_prime(num)]

print(find_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_primes([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(find_primes([2, 3, 5, 7, 11, 13, 17]))
