thisTuple = ("apple1", "banana1", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry")
print(thisTuple)

print(thisTuple.index('cherry'))
print(thisTuple.count('cherry'))

for i in thisTuple:
    print(i.upper())

# Set Items

thisSet = {"apple", "banana", "cherry", "apple"}
print(thisSet)

thisSet.update(["Hello" + str(i) for i in range(4)])
print(thisSet)

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year1": 1964,
    "year": 2020,
    "fruits": ["apple", "banana", "cherry", "apple"]
}
print(thisDict)
print(thisDict.__len__())
print(thisDict.values())
print(thisDict.keys())
print(thisDict.fromkeys(['year'], 1))
print(thisDict.fromkeys('year', 1))
