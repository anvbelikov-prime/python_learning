import calendar

def print_calendar(year=2025):
    c = calendar.TextCalendar(0)
    print(c.formatyear(year))
