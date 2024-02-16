# Python program to sort a list of dictionaries using Lambda.
import datetime

models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
models.sort(key=lambda x: x['color'])
print(models)
sorted_models = sorted(models, key=lambda x: x['model'])
print(sorted_models)

#  Filter a list of integers using Lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

now = datetime.datetime.now()
print(now)
Year = lambda x: x.year
Month = lambda x: x.month
Day = lambda x: x.day
Time = lambda x: x.time().replace(microsecond=0)

print(Year(now))
print(Month(now))
print(Day(now))
print(Time(now))

