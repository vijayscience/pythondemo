thistuple = ("apple1", "banana1", "cherry","apple", "banana", "cherry","apple", "banana", "cherry")
print(thistuple)

print(thistuple.index('cherry'))
print(thistuple.count('cherry'))

# Set Items

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset.update(["Hello"+str(i) for i in range(4)])
print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year1": 1964,
  "year": 2020,
  "fruits":["apple", "banana", "cherry", "apple"]
}
print(thisdict)
print(thisdict.__len__())
print(thisdict.values())
print(thisdict.keys())
print(thisdict.fromkeys(['year'],1))
print(thisdict.fromkeys('year',1))



