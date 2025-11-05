class MyEnumerate:
    def __init__(self, seq, start=0):
        self.seq = seq
        self.start = start
    
    def __iter__(self):
        return MyEnumerateIterator(self.seq, self.start)

class MyEnumerateIterator:
    def __init__(self, seq, start):
        self.seq = seq
        self.start = start
        self.idx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < len(self.seq):
            value = (self.idx + self.start, self.seq[self.idx])
            self.idx += 1
            return value
        else:
            raise StopIteration

def my_enumerate_gen(seq, start=0):
    i = 0
    while i < len(seq):
        yield (i + start, seq[i])
        i += 1
       
# iter_seq = MyEnumerate('abcdefgh', 2)

# for c in iter_seq:
#     print(c)

# print('-' * 50)

# for c in iter_seq:
#     print(c)

for e in my_enumerate_gen('abcdefgh', 1):
    print(e)
