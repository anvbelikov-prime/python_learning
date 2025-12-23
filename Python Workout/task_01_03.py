import random

def guessing_game():
    possible_words = ['a', 'bb', 'abc', 'c', 'cc', 'aaaa']
    target = random.choice(possible_words)
    tries = 0
    while True:
        if tries >= 3:
            print('Превышено допустимое число попыток (3)!')
            break
        answer = input(f'Введите ваш ответ ({sorted(possible_words)}): ')
        tries += 1
        if answer == target:
            print('Угадали!')
            break
        elif answer < target:
            print('Больше!')
        else:
            print('Меньше!')

guessing_game()
