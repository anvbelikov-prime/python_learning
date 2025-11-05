it = iter([1, 2, 3])

while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        print('Stoped! No other elements in sequence!')
        break

it = [1, 2, 3].__iter__()

while True:
    try:
        i = it.__next__()
        print(i)
    except StopIteration:
        print('Stoped! No other elements in sequence!')
        break

print('-' * 50)

class MyContainer:
    def __init__(self, val=0, seq=[1, 2, 3]):
        self.val = val
        self.seq = seq
    def __iter__(self):
        return iter(self.seq)
    
obj = MyContainer()

for i in obj:
    print(i, end=' ')
print()

for i in obj:
    print(i, end=' ')
print()

print('-' * 50)

class IterCLass:
    def __init__(self, seq=[1, 2, 3]):
        self.idx = 0
        self.seq = seq
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < len(self.seq):
            self.idx += 1
            return self.seq[self.idx - 1]
        else:
            self.idx = 0
            raise StopIteration
        
obj = IterCLass([1, 2, 3])

for i in obj:
    print(i, end=' ')
print()

for i in obj:
    print(i, end=' ')
print()

print('-' * 50)

def my_range(start=0, stop=10, inc=0.5):
    cur = start
    while cur <= stop:
        yield cur
        cur += inc

for i in my_range(0, 10, 0.5):
    print(i, end=' ')
print()

print('-' * 50)

for i in reversed(range(0, 11)):
    print(i, end=' ')
print()

class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

obj = Countdown(10)

for i in obj:
    print(i,  end=' ')
print()

for i in reversed(obj):
    print(i, end=' ')
print()
