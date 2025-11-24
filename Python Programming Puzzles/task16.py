def censor_python(input_strs):
    censor_dict_not_capital = {ord(c): ord('x') for c in 'python'}
    censor_dict_capital     = {ord(c): ord('X') for c in 'python'.upper()}
    return [s.translate(censor_dict_capital).translate(censor_dict_not_capital) for s in input_strs]

print(censor_python(['python', 'hello', 'HELLO', 'PYTHON']))
print(censor_python(['abcdefg']))
print(censor_python([]))

def censor_python_v2(input_strs):
    return [''.join([c if c.lower() not in 'python' else 'X' for c in s]) for s in input_strs]

print('---------------------------------------------')

print(censor_python_v2(['python', 'hello', 'HELLO', 'PYTHON']))
print(censor_python_v2(['abcdefg']))
print(censor_python_v2([]))
