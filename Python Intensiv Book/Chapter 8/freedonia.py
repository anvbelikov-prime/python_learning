freedonia_tax_county = {
    'Chiko': 0.5,
    'Gowcho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}

class WrongAmount(Exception): pass

def calculate_tax(net_price, county, hour):
    return net_price * (1 + freedonia_tax_county[county] * hour / 24)

def calculate_profit_tax(amount):
    if amount <= 0:
        raise WrongAmount('Некорректная сумма дохода!')
    elif 0 < amount <= 1000:
        return 0
    elif 1000 < amount <= 11000:
        return (amount - 1000) * 0.1
    elif 11000 < amount <= 21000:
        return 10000 * 0.1 + (amount - 11000) * 0.2
    elif amount > 21000:
        return  10000 * 0.1 + 10000 * 0.2 + (amount - 21000) * 0.5

