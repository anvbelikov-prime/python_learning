def contains_python_chars(input_str):
    for i in range(len(input_str) - len('python') + 1):
        if set(input_str[i: i + len('python')].lower()) == set('python'):
            return True
    return False

print(contains_python_chars('pYTHon'))
print(contains_python_chars('Nohtyp'))
print(contains_python_chars('pythZon'))
