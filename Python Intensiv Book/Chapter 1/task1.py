import random

def guessing_game():
    guess = random.randint(0, 100)
    print(guess)
    while True:
        answer = int(input("Введите число: "))
        if answer == guess:
            print("Вы угадали!")
            break
        elif answer > guess:
            print("Ваше число больше, чем нужно :(")
        else:
            print("Ваше число меньше, чем нужно :(")

def guessing_game_v2():
    guess = random.randint(0, 100)
    print(guess)
    tries = 0
    while True:
        tries += 1
        if tries > 3:
            print("Попытки кончились!")
            break
        answer = int(input("Введите число: "))
        if answer == guess:
            print("Вы угадали!")
            break
        elif answer > guess:
            print("Ваше число больше, чем нужно :(")
        else:
            print("Ваше число меньше, чем нужно :(")

def guessing_game_v3():
    guess = random.randint(0, 100)
    guess_base = random.choice([2, 8, 10, 16])
    while True:
        answer = int(input("Введите число: "), guess_base)
        if answer == guess:
            print("Вы угадали!")
            break
        elif answer > guess:
            print("Ваше число больше, чем нужно :(")
        else:
            print("Ваше число меньше, чем нужно :(")

def guessing_game_v4():
    words = ['a', 'b', 'c', 'aa', 'ab', 'ac', 'aaa']
    answer = random.choice(words)
    while True:
        guess = input("Введите слово: ")
        if guess == answer:
            print("Вы угадали!")
            break
        elif guess > answer:
            print("Ваше слово больше, чем нужно :(")
        else:
            print("Ваше слово меньше, чем нужно :(")

guessing_game_v4()