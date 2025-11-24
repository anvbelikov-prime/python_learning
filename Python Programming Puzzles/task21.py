def fibonacci(sequence_number):
    if sequence_number == 0:
        return 0
    elif sequence_number == 1:
        return 1
    else:
        return fibonacci(sequence_number - 1) + fibonacci(sequence_number - 2)

print(fibonacci(4))
print(fibonacci(0))
print(fibonacci(6))
