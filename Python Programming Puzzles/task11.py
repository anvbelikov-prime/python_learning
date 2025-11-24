def format_number_with_commas(input_num):
    return f'{input_num:,}'.translate({ord(','): ord('.')})

print(format_number_with_commas(10**6))
print(format_number_with_commas(12345))
print(format_number_with_commas(-99999999))
