import collections

def delimiters():
    res = collections.defaultdict(list)
    numbers = [int(i) for i in input('Введите числа: ').strip().split()]
    for number in numbers:
        for i in range(1, number):
            if number % i == 0:
                res[number].append(i)
    return res

print(delimiters())
