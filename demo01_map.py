"""
the map() function is used to apply a given funciton to every item in a given collection
(collections: list, tuple, set, dictionary)
"""

celsiusTemps = [0, 10, 20, 30, 40]

# convert to a list of fahrenheit
# (c * 9/5) + 32

def c_to_f(temp):
    return (temp * 9/5) + 32

fahrenheitTemps = map(c_to_f, celsiusTemps)
print(fahrenheitTemps) # map object
# converts map object to list
print(list(fahrenheitTemps))

# do the same with lambda
fahrenheitTempsNew = map(lambda temp: (temp * 9/5) + 32, celsiusTemps)
print(fahrenheitTempsNew) # this is a map
fahrenheitTempsNew = list(fahrenheitTempsNew) # this converts to list

# why would we use map??
# - saves time, no long for loops
# - cleaner code
# - works great with lambda
# - efficient

names = [
    {"fname": "john", "lname": "egbert", "age": "14"},
    {"fname": "jade", "lname": "harley", "age": "15"},
    {"fname": "rose", "lname": "lalonde", "age": "16"},
    {"fname": "dave", "lname": "strider", "age": "14"},
    {"fname": "karkat", "lname": "vantas", "age": "14"}
]

# without list comprehension: map these names to be lastnameFirstinitial, zero padded age (14 014)
print(f"{"5".rjust(3, "0")}")

codes = list(map(lambda dict: f"{dict["lname"]}{dict["fname"][0]}{str(dict["age"]).rjust(3,"0")}",names))
print(codes)