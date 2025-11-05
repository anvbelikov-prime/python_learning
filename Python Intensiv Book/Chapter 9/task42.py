class FlexibleDict(dict):
    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        else:
            if type(key) == str and int(key) in self.keys():
                return super().__getitem__(int(key))
            elif type(key) == int and str(key) in self.keys():
                return super().__getitem__(str(key))
            else:
                raise KeyError(key)
            
# d = FlexibleDict()
# d['1'] = 100
# print(d[1])

class StringKeyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key), value)

# d = StringKeyDict()
# d[1] = 1
# d[100] = 100
# d[5] = 'a'
# print(d)

class RecentDict(dict):
    def __init__(self, num):
        super().__init__()
        self.max_members = num
    def __setitem__(self, key, value):
        if len(self) < self.max_members:
            super().__setitem__(key, value)
        else:
            super().pop(list(self.keys())[0])
            super().__setitem__(key, value)

# d = RecentDict(5)
# print(d)
# for i in range(0, 4):
#     d[i+1] = i + 1
# print(d)
# d[5] = 5
# print(d)
# d[6] = 6
# print(d)
# d[7] = 7
# print(d)

def is_iterable(e):
    try:
        iter(e)
        return True
    except:
        return False
    
class FlatList(list):
    def append(self, elem):
        if is_iterable(elem):
            for e in elem:
                super().append(e)
        else:
            super().append(elem)

l = FlatList()
print(l)
l.append(1)
l.append(2)
print(l)
l.append([3, 4, 5])
print(l)
print('-' * 50)
ll = []
ll.append(1)
ll.append(2)
print(ll)
ll.append([3, 4, 5])
print(ll)
