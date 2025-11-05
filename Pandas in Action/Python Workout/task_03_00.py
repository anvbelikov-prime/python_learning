def run_timing():
    times = []
    num = 0
    while True:
        t = input('Введите время пробежки: ')
        if t == '':
            break
        else:
            try:
                t = float(t)
            except:
                print('Необходимо ввести число!')
                continue
            times.append(t)
            num += 1
    print(f'Среднее время пробежки: {sum(times) / len(times):.2f}, количество пробежек: {num}.')

run_timing()
