"""
filter is similar to map but the function returns value to determine true or false
"""

names = ["john", "jade", "rose", "dave", "nepeta"]

def isNotDave(name):
    return name.lower().strip() != "zach"

print(names)
cleanList = list(filter(isNotDave, names)) # returns a filter object
print(cleanList)

evenBetter = list(
    filter(lambda name: name.lower().strip() != "rose", cleanList))
print(evenBetter)

grades = [
    {"student": "kevin", "score": 79},
    {"student": "gordon", "score": 83},
    {"student": "mike", "score": 91},
    {"student": "alyx", "score": 12},
    {"student": "isaac", "score": 4}
]

# filter list to only passing students

passingStudents = list(filter(lambda grade: grade["score"] >= 60, grades))
 
print(passingStudents)