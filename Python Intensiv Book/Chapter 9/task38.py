class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    def __repr__(self):
        return str(self.flavor)

def create_scoops(*flavors):
    return [Scoop(flavor) for flavor in flavors]

scoops = create_scoops('a', 'b', 'c', 'd', 'e')

# for scoop in scoops:
#     print(scoop)

class Beverage:
    def __init__(self, name, temperature=75.0):
        self.name = name
        self.temperature = temperature
    
    def __repr__(self):
        return f'{self.name:7} напиток с температурой {self.temperature}'
    
stock = [
    {'name': 'Juice', 'temperature': 10.5},
    {'name': 'Milk', 'temperature': 15.3},
    {'name': 'Water', 'temperature': 12.7},
]

def create_beverages(stock):
    return [Beverage(d['name'], d['temperature']) for d in stock]

# for bev in create_beverages(stock):
#     print(bev)

# print(Beverage('Test'))
# print(Beverage('Test2', 77.7))

class LogFile:
    def __init__(self, file_name):
        file = open(file_name, 'w')
        self.file = file
    
    def __del__(self):
        self.file.close()

logger = LogFile('log.txt')

logger.file.write('This is a test string for logger!\n')
logger.file.write('This is another test string for logger!\n')

del logger

with open('log.txt', 'r') as f:
    for line in f:
        print(line.strip())
