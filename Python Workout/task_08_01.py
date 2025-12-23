def convert_string(s):
    return ','.join(sorted(s.strip().split()))

print(convert_string('Tom Dick Harry'))
