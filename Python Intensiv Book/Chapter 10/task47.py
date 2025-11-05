class CircleIterator:
    def __init__(self, seq, num):
        self.seq = seq
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.num:
            self.idx += 1
            return self.seq[(self.idx - 1) % len(self.seq)]
        else:
            raise StopIteration

class Circle(CircleIterator):
    def __init__(self, seq, num):
        super().__init__(seq, num)
    
    def __iter__(self):
        return super().__iter__()

# for c in Circle('abc', 6):
#     print(c)

# def circle(seq, num):
#     i = 0
#     l = len(seq)
#     while i < num:
#         yield seq[i % l]
#         i += 1

# for c in circle('abc', 5):
#     print(c)

class MyRangeIterator:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.idx = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        if self.idx < self.end:
            self.idx += self.step
            return self.idx - self.step
        else:
            raise StopIteration

class MyRange(MyRangeIterator):
    def __init__(self, start, end, step=1):
        super().__init__(start, end, step)

    def __iter__(self):
        return super().__iter__()
    
for i in MyRange(0, 15):
    print(i)
