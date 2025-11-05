class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    def __repr__(self):
        return f'Scoop with {self.flavor} flavor'
    
class Bowl:
    def __init__(self, scoop_lst=[]):
        self.scoops = [scoop for scoop in scoop_lst]
    
    def add_scoops(self, *args):
        self.scoops.extend(scoop for scoop in args)
    
    def __repr__(self):
        return 'This is a bowl of:\n' + '\n'.join(scoop.__repr__() for scoop in self.scoops)

def create_scoops(*flavors):
    return [Scoop(flavor) for flavor in flavors]

scoops = create_scoops('a', 'b', 'c', 'd', 'e')

# print(Bowl(scoops))


class Book():
    def __init__(self, name='default_name', author='default_author', price=0.0, width=0.0):
        self.name = name
        self.author = author
        self.price = price
        self.width = width
    
    def __repr__(self):
        return f'A {self.name} book by {self.author} with a price of {self.price} with width of {self.width}'

class ShelfWidthError(Exception):
    pass    

class Shelf():
    def __init__(self, max_width, *args):
        self.books = [arg for arg in args]
        self.max_width = max(max_width, sum(book.width for book in args))
    
    def __repr__(self):
        return f'Shelf with width {self.max_width} contains:\n' + '\n'.join(book.__repr__() for book in self.books)
    
    def add_books(self, *args):
        if self.total_width() + sum(arg.width for arg in args) > self.max_width:
            raise ShelfWidthError('There is no more space in shelf!')
        else:
            self.books.extend(args)

    def total_price(self):
        return sum(book.price for book in self.books)
    
    def total_width(self):
        return sum(book.width for book in self.books)
    
    def has_book(self, name):
        return name in {book.name for book in self.books}
    
shelf = Shelf(40.0, Book('Name1', 'Author1', 10.5, 10.0), Book('Name2', 'Author2', 5.5, 10.0), Book('Name3', 'Author3', 4.0, 10.0))
print(shelf)
print(shelf.books)
print(shelf.total_price())
print(shelf.total_width())
print(shelf.has_book('Name2'))
print(shelf.has_book('Name4'))
shelf.add_books(Book('Name4', 'Author4', 2.5, 10.0))
print(shelf)
print(shelf.total_price())
print(shelf.total_width())
shelf.add_books(Book('Name5', 'Author5', 1.5, 0.5))
