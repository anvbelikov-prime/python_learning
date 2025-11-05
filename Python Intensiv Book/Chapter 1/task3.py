import decimal

def my_sum(*args, start=0):
    res = start
    for i in args:
        res += i
    return res

def my_mean(*args):
    return my_sum(*args) / len(args)

def run_timing():
    times = []
    runs = 0
    while time := input("Введите время пробежки: "):
        times.append(float(time))
        runs += 1
    return f'Среднее время пробежки {my_mean(*times):.2f} за {runs} пробежек'

def float_strip(float_num, before, after):
    s = str(float_num).split(".")
    return float(s[0][len(s[0]) - before:len(s[0])] + "." + s[1][:after])

def sum_decimals(s1, s2):
    return float(decimal.Decimal(s1) + decimal.Decimal(s2))

print(sum_decimals("0.1", "0.2"))
