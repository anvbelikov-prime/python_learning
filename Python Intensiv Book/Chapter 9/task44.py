class TooManyAnimalsInCage(Exception):
    pass

class CageCapacityShortage(Exception):
    pass

class IncongruousAnimalsInCage(Exception):
    pass

class Animal:
    species = 'default_animal'
    noise = 'default_noise'
    
    def __init__(self, color, required_space=100, number_of_legs=4):
        self.color = color
        self.required_space = required_space
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f'{self.noise.capitalize()} -- {self.color} {self.species}, {self.number_of_legs} legs (space {self.required_space})'

class ZeroLeggedAnimal(Animal):
    def __init__(self, color, required_space=10):
        super().__init__(color, required_space, 0)

class TwoLeggedAnimal(Animal):
    def __init__(self, color, required_space=50):
        super().__init__(color, required_space, 2)

class FourLeggedAnimal(Animal):
    def __init__(self, color, required_space=100):
        super().__init__(color, required_space, 4)

class Sheep(FourLeggedAnimal):
    species = 'sheep'
    noise = 'baa'
    
    def __init__(self, color, required_space=100):
        super().__init__(color, required_space)

class Wolf(FourLeggedAnimal):
    species = 'wolf'
    noise = 'woo'
    
    def __init__(self, color, required_space=100):
        super().__init__(color, required_space)

class Snake(ZeroLeggedAnimal):
    species = 'snake'
    noise = 'sh'
    
    def __init__(self, color, required_space=10):
        super().__init__(color, required_space)

class Parrot(TwoLeggedAnimal):
    species = 'parrot'
    noise = 'chik-chirik'
    
    def __init__(self, color, required_space=50):
        super().__init__(color, required_space)

combined_animals = {
    Sheep: (Sheep, Wolf),
    Wolf: (Sheep, Wolf),
    Snake: (Snake, Parrot),
    Parrot: (Snake, Parrot),
}

class Cage:
    # max_animals_count = 3
    max_capacity = 300
    
    def __init__(self, id):
        self.animals = []
        self.id = id
    
    def __repr__(self):
        return f'{self.__class__.__name__} with id {self.id} (used space: {self.get_current_capacity()}):\n' + '\n'.join(animal.__repr__() for animal in self.animals)
    
    def get_current_capacity(self):
        return sum(animal.required_space for animal in self.animals)
    
    def get_combined_animals(self):
        return {t for animal in self.animals for t in combined_animals[type(animal)]}

    def add_animals(self, *animals):
        for animal in animals:
            # if len(self.animals) < self.max_animals_count:
            #     self.animals.append(animal)
            # else:
            #     raise TooManyAnimalsInCage('There is no way to put more animals in full cage!')
            if self.get_current_capacity() + animal.required_space <= self.max_capacity:
                if type(animal) in self.get_combined_animals() or len(self.animals) == 0:
                    self.animals.append(animal)
                else:
                    raise IncongruousAnimalsInCage
            else:
                raise CageCapacityShortage

class BigCage(Cage):
    # max_animals_count = 5
    max_capacity = 500
    def __init__(self, id):
        super().__init__(id)

s = Sheep('white')
w = Wolf('grey')
p = Parrot('green')
n = Snake('black')

c = Cage(1)
bc = BigCage(2)

c.add_animals(p)
c.add_animals(n)
c.add_animals(n)
c.add_animals(p)
print(c)
print('-' * 35)
print(bc)
