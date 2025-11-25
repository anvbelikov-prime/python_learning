def is_valid_equation(input_equation):
    try:
        expr, result = input_equation.split(' = ')
        if (not expr) or (not result):
            return False
        else:
            first, operation, second = expr.split(' ')
            if (not first) or (not operation) or (not second):
                return False
            elif len(operation) != 1:
                return False
            else:
                my_result = str(eval(expr))
                if my_result == result:
                    return True
                else:
                    return False
    except:
        return False

print(is_valid_equation('2 + 3 = 5'))
print(is_valid_equation('-5 - 6 = -11'))
print(is_valid_equation('-5 + -6 = -11'))
print(is_valid_equation('-5 + -6 = -12'))
print(is_valid_equation('-2 + 3 = 5'))
print(is_valid_equation('-2 + = 5'))
print(is_valid_equation('abc'))
print(is_valid_equation('a'))
print(is_valid_equation('a + b = d'))
