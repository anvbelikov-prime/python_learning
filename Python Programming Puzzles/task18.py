def get_number_of_digits(input_num):
    if input_num < 10:
        return 1
    else:
        return 1 + get_number_of_digits(input_num // 10)
    
print(get_number_of_digits(1234))
print(get_number_of_digits(0))
print(get_number_of_digits(123456789))
