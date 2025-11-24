def safe_int(num_str=None):
    '''Safe convert to int (if ValueError or TypeError returns 0)'''
    try:
        return int(num_str)
    except ValueError:
        return 0
    except TypeError:
        return 0

def sum_if_less_than_fifty(num_one, num_two):
    res = safe_int(num_one) + safe_int(num_two)
    if res < 50:
        return res
    else:
        return None
    
print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))
print(sum_if_less_than_fifty(20, 100))
