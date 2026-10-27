names = ["john", "jade", "rose", "dave"]
# we can sort the list with the .sort method
# note: this changes the actual order of the list
print(names)
names.sort() # defaults to alphabetical (ALL CAPS first)
print(names)

# sort in reverse order:
names.sort(reverse=True)
print(names)

otherNames = ("karkat", "gamzee", "nepeta", "eridian")

# otherNames.sort() 
# print(otherNames)
# cant change a tuple
# we can sort a tuple IF we use sorted
sortedOtherNames = sorted(otherNames)
# sorted returns a new list, instead of sorting in place
print(sortedOtherNames)
print(dict(enumerate(sortedOtherNames)))
print(dict(zip(["A", "B", "C", "D"], otherNames)))

# sort by length of string:
lenOfNameSorted = sorted(otherNames, key=len)
print(lenOfNameSorted)

countVowels = sorted(otherNames, lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s))))
print(countVowels("dog"))

mostVowels = sorted(otherNames, key = lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s))), reverse=True)

print(mostVowels)

def getLastLetter(word):
    return word [-1]

sortedByLastLetter = sorted(otherNames, key=getLastLetter)
print(sortedByLastLetter)