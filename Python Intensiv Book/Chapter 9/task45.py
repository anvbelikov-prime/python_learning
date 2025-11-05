import copy

class TooManyAnimalsInCage(Exception):
    pass

class CageCapacityShortage(Exception):
    pass

class IncongruousAnimalsInCage(Exception):
    pass

class ColorsValueError(Exception):
    pass

class NoAnimalForTransfer(Exception):
    pass

class NoAppropriateTargetCage(Exception):
    pass

class NoRequiredParameters(Exception):
    pass

def is_iterable(e):
    try:
        iter(e)
        return True
    except:
        return False

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
    max_capacity = 300
    
    def __init__(self, id):
        self.animals = []
        self.id = id
    
    def __repr__(self):
        return f'{self.__class__.__name__} with id {self.id} (used space: {self.get_current_capacity()}):\n' + '\n'.join('\t' + animal.__repr__() for animal in self.animals)
    
    def get_current_capacity(self):
        return sum(animal.required_space for animal in self.animals)
    
    def get_combined_animals(self):
        return {t for animal in self.animals for t in combined_animals[type(animal)]}

    def add_animals(self, *animals):
        for animal in animals:
            if self.get_current_capacity() + animal.required_space <= self.max_capacity:
                if type(animal) in self.get_combined_animals() or len(self.animals) == 0:
                    self.animals.append(animal)
                else:
                    raise IncongruousAnimalsInCage
            else:
                raise CageCapacityShortage

class BigCage(Cage):
    max_capacity = 500
    def __init__(self, id):
        super().__init__(id)

class Zoo:
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *cages):
        self.cages.extend(cages)
    
    def __repr__(self):
        return f'Zoo contains of {len(self.cages)} cage(s):\n' + '\n'.join('* ' + cage.__repr__() for cage in self.cages)
    
    def animals_by_color(self, *colors):
        if not colors:
            raise ColorsValueError('Empty colors!')
        else:
            return [animal for cage in self.cages for animal in cage.animals if animal.color in colors]
    
    def animals_by_legs(self, number_of_legs):
        return [animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == number_of_legs]
    
    def number_of_legs(self):
        return sum(animal.number_of_legs for cage in self.cages for animal in cage.animals)
    
    def transfer_animal(self, target_zoo, animal):
        source_cage_index = 0
        source_animal_index = 0
        target_cage_index = 0
        for cage in self.cages:
            animal_types = [type(a) for a in cage.animals]
            if animal in animal_types:
                source_cage_index = self.cages.index(cage)
                source_animal_index = animal_types.index(animal)
                break
        else:
            raise NoAnimalForTransfer
        animal_to_transfer = copy.deepcopy(self.cages[source_cage_index].animals[source_animal_index])
        for cage in target_zoo.cages:
            animal_types = {ct for a in cage.animals for ct in combined_animals[type(a)]}
            if type(animal_to_transfer) in animal_types:
                if cage.get_current_capacity() + animal_to_transfer.required_space <= cage.max_capacity:
                    target_cage_index = target_zoo.cages.index(cage)
                    break
        else:
            raise NoAppropriateTargetCage
        target_zoo.cages[target_cage_index].add_animals(animal_to_transfer)
        del self.cages[source_cage_index].animals[source_animal_index]

    def get_animals(self, **kwargs):
        if not {'color', 'number_of_legs'} & set(kwargs):
            raise NoRequiredParameters
        else:
            colors = kwargs.get('color', {})
            numbers_of_legs = kwargs.get('number_of_legs', {})
            if not is_iterable(colors):
                colors = {colors}
            else:
                colors = set(colors)
            if not is_iterable(numbers_of_legs):
                numbers_of_legs = {numbers_of_legs}
            else:
                numbers_of_legs = set(numbers_of_legs)
            print(colors)
            print(numbers_of_legs)
            return [animal for cage in self.cages for animal in cage.animals if (animal.color in colors) or (animal.number_of_legs in numbers_of_legs)]

    
s1 = Sheep('white1')
s2 = Sheep('white2')
s3 = Sheep('white3')
w1 = Wolf('grey1')
w2 = Wolf('grey2')
w3 = Wolf('grey3')
w4 = Wolf('grey4')
p1 = Parrot('green1')
p2 = Parrot('green2')
p3 = Parrot('green3')
n1 = Snake('black1')
n2 = Snake('black2')
n3 = Snake('black3')

c = Cage(1)
bc = BigCage(2)

c.add_animals(p1, p2, n3)
bc.add_animals(w1, w2, w3, w4, s3)

cc = Cage(3)
bcc = BigCage(4)

cc.add_animals(s1, s2)
bcc.add_animals(p3, n1, n2)

z = Zoo()
zz = Zoo()

z.add_cages(c, bc)
zz.add_cages(cc, bcc)

print(z)
# print('-' * 35)
# print(zz)

# z.transfer_animal(zz, Sheep)
print('*' * 35)

print(z.get_animals(color=['white3', 'black3'], number_of_legs=2))
# print('-' * 35)
# print(zz)
