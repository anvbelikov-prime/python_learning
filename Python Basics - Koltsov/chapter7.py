import re

p = re.compile(r'^[0-9]+$', re.M)

s = '''12333333
45677
789000'''

print(p.search(s))

print(p.findall(s))

s = 'abc123456def'

p = re.compile(r'[0-9]{3}')

print(p.findall(s))

p = re.compile(r'<([a-z]+)>(.*?)</([a-z]+)>', re.S)

s = '<tag>One</tag>, <i>Two</j>, <n>Three</n>, <l>Four<l>, some text here'

print(p.findall(s))

s = 'abc def,bfgj; ekrgjekl,    ldfkglk  ,  fdgjkd   ffll\tggg'

print(re.split(r'\s*[,;\s]\s*', s))
print(re.split(r'\s*([,;\s])\s*', s))
print(re.split(r'(\s*([,;\s])\s*)', s))

s1 = '123'
s2 = '123a'
s3 = 'a123'

p = re.compile(r'[0-9]+')
print(p.match(s1))
print(p.match(s2))
print(p.match(s3))

filenames = ['ch.py', 'o.c', 'hee.ini']

print([name for name in filenames if name.endswith(('.py', '.c'))])

s = 'Сегодня 9/04/2025. Завтра будет 09/10/2025.'

p = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

print(p.findall(s))

print(p.sub(r'\3-\1-\2', s))

def date_transform(m):
    month, day, year = m.groups()
    if len(month) == 1:
        month = '0' + month
    return f'{year}-{month}-{day}'

print(p.sub(date_transform, s))
