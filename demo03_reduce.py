"""
the reduce function is used to reduce a collection into a single value
unlike built in function like map and filter, the reduce function is not
built directly into python
"""
from functools import reduce

grades = [98, 72, 71, 84, 88]

# reduce syntax:
# reduce(function, collection)

def sum(x, y):
    return x + y

totalScores = reduce(sum, grades)
# it's pretty much calling sum(sum(sum(sum(98, 72), 51), 84), 68)
print(totalScores)
totalScores_but_bad = sum(sum(sum(sum(98, 72), 51), 84), 68)
print(totalScores_but_bad)

def allPasses(x, y):
    return x > 70 and y > 70

everybodyPass = reduce(allPasses, grades)
print(everybodyPass)