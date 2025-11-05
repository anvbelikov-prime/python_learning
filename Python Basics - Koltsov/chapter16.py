class SampleClass:
    def __init__(self):
        self.nm = 'SampleClass'
    def printName(self):
        print(self.nm)
    
obj = SampleClass()

obj.printName()
print(obj.nm)
print(type(obj))

print('-' * 50)

print(hasattr(obj, 'nm'))
print(getattr(obj, 'nm'))
setattr(obj, 'new_attr', 'val')
print(obj.new_attr)
delattr(obj, 'new_attr')
print(hasattr(obj, 'new_attr'))

print('-' * 50)

class Parent:
    def __init__(self, a=5, b=3):
        self.a = a
        self.b = b
    def print_parent(self):
        print('Parent!')
    def print_name(self):
        print('Parent!')

class Child(Parent):
    def __init__(self, a=5, b=3, c=7):
        super().__init__(a, b)
        self.c = c
    def print_child(self):
        print('Child!')
    def print_name(self):
        print('Child!')

obj = Child()
obj.print_parent()
obj.print_child()
obj.print_name()
print(obj.a, obj.b, obj.c)

print('-' * 50)

class IterCLass:
    def __init__(self, seq):
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

class StaticSample:
    @staticmethod
    def ssum(x, y):
        return x + y
    def msum(self, x, y):
        return x + y
    
print(StaticSample.ssum(1, 2))
obj = StaticSample()
print(obj.msum(1, 2))
print(obj.ssum(1, 2))

print('-' * 50)

import abc

class Sample:
    @abc.abstractmethod
    def f(self):
        raise NotImplementedError('Not implemented!')

class ChildSample(Sample):
    pass

obj = ChildSample()
try:
    obj.f()
except Exception as e:
    print('Вызов непереопределенного абстрактного метода!')
    print(e)

print('-' * 50)

class ClassWithProperty:
    def __init__(self, a):
        self.a = a
    def get_a(self):
        return self.a
    def set_a(self, a):
        self.a = a
    def del_a(self):
        del self.a
    length = property(get_a, set_a, del_a, "Length")

obj = ClassWithProperty(7)
print(obj.a)
print(obj.length)
obj.length = 777
print(obj.a)
print(obj.length)
del obj.length
print(hasattr(obj, 'a'))
print(hasattr(obj, 'length'))
