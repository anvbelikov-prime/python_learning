class MyError(Exception):
    pass

class SeparatorNotFoundError(MyError):
    pass

class EmptyStringError(MyError):
    pass

def my_split(s, sep):
    if not s:
        raise EmptyStringError('Empty text for splitting')
    if sep not in s:
        raise SeparatorNotFoundError(f'"{sep}" separator is not found in text for splitting')
    
    res = []
    idx = 0
    idx_new = 0

    while (idx_new := s.find(sep, idx)) != -1:
        res.append(s[idx:idx_new])
        idx = idx_new + len(sep)
    res.append(s[idx:])
    
    return res


try:
    print(my_split('a,b,cc,ddd', ';'))
except MyError as e:
    print(e)

try:
    print(my_split('', ';'))
except MyError as e:
    print(e)

print(my_split('a,b,cc,ddd', ','))
print(my_split(',a,b,cc,ddd', ','))
print(my_split(',a,b,cc,ddd,', ','))
print(my_split(',,a,b,cc,,ddd,,', ','))
print(my_split(',;a,;b,;cc,;,;ddd,;,;', ',;'))
