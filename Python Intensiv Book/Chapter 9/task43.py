class Animal:
    species = 'default_animal'
    noise = 'default_noise'
    def __init__(self, color, number_of_legs=4):
        self.color = color
        self.number_of_legs = number_of_legs
    def __repr__(self):
        return f'{self.noise.capitalize()} - {self.color} {self.species}, {self.number_of_legs} legs'

class ZeroLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class TwoLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class FourLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Sheep(FourLeggedAnimal):
    species = 'sheep'
    noise = 'baa'
    def __init__(self, color):
        super().__init__(color)

class Wolf(FourLeggedAnimal):
    species = 'wolf'
    noise = 'woo'
    def __init__(self, color):
        super().__init__(color)

class Snake(ZeroLeggedAnimal):
    species = 'snake'
    noise = 'sh'
    def __init__(self, color):
        super().__init__(color)

class Parrot(TwoLeggedAnimal):
    species = 'parrot'
    noise = 'chik chirik'
    def __init__(self, color):
        super().__init__(color)
