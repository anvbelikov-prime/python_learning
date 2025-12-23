def safe_int(i):
    try:
        return int(i)
    except:
        return 0
    
def sum_numeric(*args):
    res = 0
    for i in args:
        res += safe_int(i)
    return res

print(sum_numeric(10, 20, 'a', '30', 'bcd'))
