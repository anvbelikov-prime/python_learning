def harmonic_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)

print(harmonic_sum(5))
print(harmonic_sum(2))
print(harmonic_sum(0))
