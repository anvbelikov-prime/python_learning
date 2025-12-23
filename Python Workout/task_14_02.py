import datetime

temperatures = {
    '2025-09-09': 9.5,
    '2025-09-10': 10.5,
    '2025-09-11': 11.5,
    '2025-09-12': 12.5,
    '2025-09-13': 13.5,
    '2025-09-14': 14.5,
    '2025-09-15': 15.5,
    '2025-09-16': 16.5,
    '2025-09-17': 17.5,
    '2025-09-18': 18.5,
}

def shift_date(date_iso, days=1):
    dt = datetime.datetime.fromisoformat(date_iso)
    return (dt + datetime.timedelta(days=days)).strftime('%Y-%m-%d')

def get_temperature():
    input_date = input('Введите дату: ')
    if input_date in temperatures:
        print(f'Temperature on {input_date} is {temperatures[input_date]}')
        if shift_date(input_date, -1) in temperatures:
            print(f'Previous data: {shift_date(input_date, -1)}: {temperatures[shift_date(input_date, -1)]}')
        else:
            print('No previous data in database!')
        if shift_date(input_date, +1) in temperatures:
            print(f'Next data: {shift_date(input_date, +1)}: {temperatures[shift_date(input_date, +1)]}')
        else:
            print('No next data in database!')
    else:
        print('No data in database!')

get_temperature()
