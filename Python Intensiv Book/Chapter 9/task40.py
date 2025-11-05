class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'A scoop of a "{self.flavor}" flavor'
    
class Bowl:
    max_scoops = 3

    def __init__(self, *scoops):
        self.scoops = [scoop for scoop in scoops[:Bowl.max_scoops]]

    def add_scoops(self, *args):
        if len(self.scoops) >= Bowl.max_scoops:
            return
        else:
            self.scoops.extend(args[:Bowl.max_scoops - len(self.scoops)])

    def __repr__(self):
        return f'This is a Bowl with {len(self.scoops)} scoop(s)\n' + '\n'.join(scoop.__repr__() for scoop in self.scoops)
    
# b = Bowl(Scoop('a'), Scoop('b'))
# print(b)
# b.add_scoops(Scoop('c'))
# print(b)
# b.add_scoops(Scoop('d'), Scoop('e'), Scoop('f'))
# print(b)
# b.scoops = []
# print(b)

class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1
    def __repr__(self):
        return f'Person "{self.name}"'
    def __del__(self):
        Person.population -= 1
    
persons = [Person('Name ' + str(i)) for i in range(0, 5)]

# for i in range(0, len(persons)):
#     persons.pop()
#     print(Person.population)

class Transaction:
    total_amount = 0
    def __init__(self, amount):
        self.amount = amount
        Transaction.total_amount += amount
    def __repr__(self):
        return f'Transaction with {self.amount} amount'

t1 = Transaction(1000)
t2 = Transaction(500)
t3 = Transaction(1000)
print(Transaction.total_amount)
