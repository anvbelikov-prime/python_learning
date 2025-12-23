import random

def guessing_game():
    target = random.randint(0, 100)
    while True:
        try:
            answer = int(input('Введите ваш ответ (целое число): '))
        except:
            print('Вы должны ввести целое число!')
            continue
        if answer == target:
            print('Угадали!')
            break
        elif answer < target:
            print('Больше!')
        else:
            print('Меньше!')

guessing_game()
