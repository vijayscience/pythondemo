import itertools

nums = (1, 2, 3, 4, 5, 6, 7)
result = map(lambda x: x ** 2, nums)
print("Triple of said list numbers:", list(result))

# Add three lists using map function and lambda
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(result))

# Power of a number in bases raises to the corresponding number
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ind = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(pow, bases_num, ind)))

# Convert a list of integers
nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)

print(list(map(str, nums_list)))


# Fibonacci numbers:
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y


print("First 10 Fibonacci numbers:")
print(list(itertools.islice(fibonacci_nums(), 10)))



