menu = {
    'bread': 1.00,
    'fish': 2.50,
    'meat': 5.00,
    'salad': 1.50
}

def restaurant():
    order_sums = []
    while True:
        dish = input(f'Заказ ({list(menu.keys())}): ')
        if dish.strip() == '':
            break       
        elif dish.strip() not in menu:
            print('Нет такого блюда!')
            continue
        else:
            order_sums.append(menu[dish.strip()])
            print(f'{dish.strip()} стоит {menu[dish.strip()]}. Общая сумма: {sum(order_sums)}')
    print(f'Общая сумма заказа: {sum(order_sums)}')

restaurant()
