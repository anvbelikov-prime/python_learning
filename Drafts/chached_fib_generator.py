import time

class FibGeneratorChached:
    
    def __init__(self, lim=10):
        self.__is_fully_cached = False
        self.__lim = lim
        self.__idx = 0
        self.__chache = []
        self.__first = 0
        self.__second = 1
    
    def __iter__(self):
        if self.__is_fully_cached:
            return iter(self.__chache)
        else:
            return self
    
    def __next__(self):
        if self.__idx >= self.__lim:
            self.__is_fully_cached = True
            self.__first = 0
            self.__second = 1
            self.__idx = 0
            raise StopIteration
        else:
            if self.__idx == 0:
                self.__chache.append(self.__first)
                self.__idx += 1
                return self.__first
            elif self.__idx == 1:
                self.__chache.append(self.__second)
                self.__idx += 1
                return self.__second
            else:
                self.__second, self.__first = self.__first + self.__second, self.__second
                self.__chache.append(self.__second)
                self.__idx += 1
                return self.__second

class FibGenerator:
    
    def __init__(self, lim=10):
        self.__lim = lim
        self.__idx = 0
        self.__first = 0
        self.__second = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__idx >= self.__lim:
            self.__first = 0
            self.__second = 1
            self.__idx = 0
            raise StopIteration
        else:
            if self.__idx == 0:
                self.__idx += 1
                return self.__first
            elif self.__idx == 1:
                self.__idx += 1
                return self.__second
            else:
                self.__second, self.__first = self.__first + self.__second, self.__second
                self.__idx += 1
                return self.__second

gen1 = FibGeneratorChached(1000)
gen2 = FibGenerator(1000)

t1 = time.time()
for i in range(10000):
    list(gen1)
t2 = time.time()

res1 = t2 - t1

t1 = time.time()
for i in range(10000):
    list(gen2)
t2 = time.time()

res2 = t2 - t1

print(round(res1, 4), round(res2, 4), round(res2 / res1, 4))
