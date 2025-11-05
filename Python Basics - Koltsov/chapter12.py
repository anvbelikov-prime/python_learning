import time

print(time.time())
print(time.gmtime(time.time()))
print(time.localtime(time.time()))

print(time.strftime('%d.%m.%Y'))
print(time.strftime('%H:%M:%S'))
print(time.strftime('%d.%m.%Y %H:%M:%S'))

print(time.strptime('2025-09-09 15:07:53', '%Y-%m-%d %H:%M:%S'))

print(time.strftime('%a %A'))

import calendar

c = calendar.LocaleTextCalendar(0)
print(c.formatyear(2025))

c = calendar.TextCalendar(0)
print(c.formatyear(2025))
print()
print(c.formatmonth(2025, 9))
print()

# c = calendar.HTMLCalendar(0)
# print(c.formatyear(2025))

c = calendar.TextCalendar(6) # Sunday is the first day of a week!
print(c.formatyear(2025))

print('sleeping')
time.sleep(2)
print('sleeping is done!')

import timeit

code_to_exec = '''
for i in range(1000000):
    print(i)
'''

t = timeit.Timer(code_to_exec, 'pass')
print(t.timeit(1))

import datetime

a = datetime.datetime(2025, 9, 9)
print(a + datetime.timedelta(days=15))
