from datetime import date, timedelta, datetime, time

dt = date.today() - timedelta(5)
print('Current Date :', date.today())
print('5 days before Current Date :', dt)

print(
    datetime.fromtimestamp(int("123456789012")).strftime('%Y-%m-%d %H:%M:%S')
)
print(datetime.date(datetime.today()))

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print('Yesterday : ', yesterday)
print('Today : ', today)
print('Tomorrow : ', tomorrow)

dt = date.today()
print("datetime.date = ", date(1233, 3, 2))
print(datetime.max.time())
print(datetime.combine(dt, datetime.min.time()))

for x in range(0, 5):
    print(dt + timedelta(days=x))

x = datetime.now()
y = x + timedelta(0, 5)
print(x.time())
print(y.time())

print(time())
print(date(2015, 6, 16).isocalendar()[1])

import time

print(time.asctime(time.strptime("2015 51 0", "%Y %W %w")))


def all_sundays(year):
    # January 1st of the given year
    dt = date(year, 1, 1)
    print(dt.weekday())
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)


for s in all_sundays(2020):
    print(s)

print(y.time().replace(microsecond=0))

a = date(2000,2,28)
b = date(2001,2,28)
print(b-a)
