class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'A scoop of a "{self.flavor}" flavor'
    
class Bowl:
    max_scoops = 3

    def __init__(self, *scoops):
        self.scoops = [scoop for scoop in scoops[:self.max_scoops]]

    def add_scoops(self, *args):
        if len(self.scoops) >= self.max_scoops:
            return
        else:
            self.scoops.extend(args[:self.max_scoops - len(self.scoops)])

    def __repr__(self):
        return f'This is a Bowl with {len(self.scoops)} scoop(s)\n' + '\n'.join(scoop.__repr__() for scoop in self.scoops)
    
class BigBowl(Bowl):
    max_scoops = 5

# print(BigBowl.max_scoops)
# print(Bowl.max_scoops)

b, bb = Bowl(), BigBowl()

for i in range(0, 7):
    b.add_scoops(Scoop(str(i)))
    bb.add_scoops(Scoop(str(i)))

# print(b)
# print('-' * 20)
# print(bb)

class Envelope:
    coef = 10
    def __init__(self, weight, was_sent=False, postage=0):
        self.weight = weight
        self.was_sent = was_sent
        self.postage = postage
    def add_postage(self, num):
        self.postage += num
    def postage_needed(self):
        return round(self.weight * self.coef)
    def send(self):
        if self.postage_needed() <= self.postage:
            self.was_sent = True
            print('Envelope is sent!')
        else:
            print('Sending error! You need more postage to complete sending!')

class BigEnvelope(Envelope):
    coef = 15

# e = BigEnvelope(100)
# print(e.postage_needed())
# e.add_postage(1500)
# print(e.postage)
# e.send()

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def dial(self):
        return f'Dialing phone number {self.phone_number}'

class SmartPhone(Phone):
    def run_app(self, app_name):
        return f'Running app "{app_name}" on phone number {self.phone_number}'

class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name) + ' by iPhone!'

# p = Phone('555-999')
# print(p.dial())
# s = SmartPhone('777-999')
# print(s.dial())
# print(s.run_app('Awesome App'))
# i = iPhone('999-999')
# print(i.dial())
# print(i.run_app('Awesome App'))

class Bread:
    def __init__(self):
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8
    def get_nutrition(self, num):
        return {k: v * num for k, v in vars(self).items()}

class WholeWheatBread(Bread):
    def __init__(self):
        self.calories = 55
        self.carbs = 11
        self.sodium = 160
        self.sugar = 0.1
        self.fat = 0.1

class RyeBread(Bread):
    def __init__(self):
        self.calories = 44
        self.carbs = 10
        self.sodium = 150
        self.sugar = 0.7
        self.fat = 0.7


b = Bread()
bb = WholeWheatBread()
bbb = RyeBread()

print(b.get_nutrition(1))
print(bb.get_nutrition(1))
print(bbb.get_nutrition(1))
