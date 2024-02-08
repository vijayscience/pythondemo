string = "the brown dog jumped over the brown fence and then the brown cat followed the brown dog"
arr = string.split()
arr1=[]
for i in arr:
    if(arr.count(i)>=2):
        if i not in arr1:
           arr1.append(i)
print(arr1)

####################

arr1={}
for i in arr:
    arr1[i]=arr.count(i)

# print(arr1)
#_________________________________________________
arr2 =arr.copy()
arr.extend(["DDSD"])
print(arr)
print(arr2)
#___________________Direct change in Arrary

arr.reverse()
print(arr)
# arr.clear()
# print(arr)
print(arr.index('the')) # Postion of 'the' in list

arr.insert(6,'Zomato')
print(arr)
arr.pop()
print(arr)
arr.sort()
print(arr)
for i in range(2):
    arr.remove('dog')
print(arr)

# ---------------------





