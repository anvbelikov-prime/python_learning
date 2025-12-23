import random

def guessing_game():
    target = random.randint(0, 100)
    tries = 0
    while True:
        if tries >= 3:
            print('Превышено допустимое число попыток (3)!')
            break
        try:
            answer = int(input('Введите ваш ответ (целое число): '))
        except:
            print('Вы должны ввести целое число!')
            continue
        tries += 1
        if answer == target:
            print('Угадали!')
            break
        elif answer < target:
            print('Больше!')
        else:
            print('Меньше!')

guessing_game()
