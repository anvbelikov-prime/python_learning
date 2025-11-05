import datetime

menu = {
    "salad": 100,
    "meat": 350,
    "pasta": 200,
    "fish": 100,
    "tea": 50,
    "coffee": 100
}

def restaurant(menu):
    answer = ''
    order = []
    while True:
        answer = input("Введите ваше блюдо: ")
        if answer == '':
            break
        elif answer not in menu:
            print("Нет такого блюда!")
        else:
            order.append(menu[answer])
            print(f"Вы заказали {answer}, его стоимость {menu[answer]}, общая стоимость заказа: {sum(order)}")
    print(f"Итого: стоимость заказа {sum(order)}")

# restaurant(menu)

passwd = {
    "user1":"passwd1",
    "user2":"passwd2",
    "user3":"passwd3",
}

def authorizitaion(passwd):
    user = input("Login: ")
    if user == '':
        return
    elif user not in passwd:
        print("Нет такого пользователя")
    else:
        password = input("Password: ")
        if passwd[user] == password:
            print("Успешный вход!")
        else:
            print("Невереный пароль!")

# authorizitaion(passwd)

temperatures = {
    "2025-07-07": 27.1,
    "2025-07-08": 28.2,
    "2025-07-09": 29.3,
    "2025-07-10": 30.4,
    "2025-07-11": 31.5,
    "2025-07-12": 32.6,
    "2025-07-13": 33.7,
}

def get_temperature(temperatures):
    while True:
        dt = input("Введите дату: ")
        if dt == '':
            break
        elif dt not in temperatures:
            print("Нет такой даты в данных!")
        else:
            print(f'Температура за указанную дату {dt}: {temperatures[dt]}')
            iso_datetime = datetime.date.fromisoformat(dt)
            delta = datetime.timedelta(days=1)
            if (iso_datetime - delta).isoformat() in temperatures:
                print(f'Температура за предыдущую дату {(iso_datetime - delta).isoformat()}: {temperatures[(iso_datetime - delta).isoformat()]}')
            if (iso_datetime + delta).isoformat() in temperatures:
                print(f'Температура за следующую дату {(iso_datetime + delta).isoformat()}: {temperatures[(iso_datetime + delta).isoformat()]}')

# get_temperature(temperatures)

birthdays = {
    "user1":"2025-07-11",
    "user2":"2025-07-01",
    "user3":"1988-10-02",
}

def calc_days_old(birthdays):
    user = input("Введите имя: ")
    if user == '':
        return
    elif user not in birthdays:
        print("Нет такого человека в базе!")
    else:
        print(f'Возраст в днях: {(datetime.date.today() - datetime.date.fromisoformat(birthdays[user])).days} дней')

calc_days_old(birthdays)
