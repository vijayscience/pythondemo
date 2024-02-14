def calculateSq(n):
    return n * n


numbers = (2, 3, 4, 5)
result = map(calculateSq, numbers)
for i, e in enumerate(result):
    print(i, e)

a = [1, 2, 3]
b = [3, 4, 5]
c = [6, 7, 8]
print([*a, *b, *c])
print(a + b + c)
print([z for x in (a, b, c) for z in x])
b.extend(c)
a.extend(b)
print(a)


def extendList(val, list1=[]):
    list1.append(val)
    return list1


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


def div1(x, y):
    print("%s/%s = %s" % (x, y, x / y))


def div2(x, y):
    print("%s//%s = %s" % (x, y, x // y))


div1(5, 2)
div1(5., 2)
div2(5, 2)
div2(5., 2.)

import pandas as pd
import numpy as np

# dictionary of lists
dict1 = {'id': [1, 4, np.nan, 9],
         'Age': [30, 45, np.nan, np.nan],
         'Score': [np.nan, 140, 180, 198]}
# creating a DataFrame
df = pd.DataFrame(dict1)
print(df.isnull().sum())


# id       1
# Age      2
# Score    1
def valid_square(num):
    square = int(num ** 0.5)
    check = square ** 2 == num
    return check


print(valid_square(10))
# False
print(valid_square(36))
# True
print(valid_square(3136))


# True


def factorial_trailing_zeros(n):
    fact = n
    while n > 1:
        fact *= n - 1  # 4*3,12*2,24*1
        n = n - 1
    print(fact)

    result = 0
    for i in str(fact)[::-1]:
        print(i)
        # if i == 0:
        #     result += 1
    print(result)


factorial_trailing_zeros(7)


#  Remove duplicates from sorted array
def removeDuplicates(arr):
    newArr = []
    for i in arr:
        if i not in newArr:
            newArr.append(i)
    return newArr


array_1 = [1, 2, 2, 3, 3, 4]
print(removeDuplicates(array_1))

array_2 = [1, 1, 3, 4, 5, 6, 6]
print(removeDuplicates(array_2))


def find_missing(input_list):
    input_list.sort()
    print(input_list)
    ArryLen = len(input_list)
    for ii in range(1, ArryLen + 1):
        if ii != input_list[ii - 1]:
            print('Missing ', ii, input_list[ii - 1])
            break


list_1 = [1, 5, 6, 3, 4, 2, 8]
find_missing(list_1)



