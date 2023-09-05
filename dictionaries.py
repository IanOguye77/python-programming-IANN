  # Dictionaries
# A dictionary is an unordered set of key-value pairs, separated by comma and enclosed by curly braces. 
# They are very useful for storing information in a specific format. For instance, considering a router, we can store data about the device in the following format:
# Vendor:Cisco, Model:2600, IOS:12.4, Ports:4
# lets create an empty dictionary
dict1 = {}

# check the type
print(type(dict1))

# lets add some data to our dictionary
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports":"4"}

# Each dictionary element consists of a key, a colon, and a value, followed by a comma.

d1 = {1: "First Element", 2: "Second Element"}

# Each dictionary key must be unique and should be of a immutable type -> strings, tuples or numbers but not lists
# on the other hand, values don't have to be unique and can be either a mutable or immutable data type.

# Dictionary Methods
# consider dict1
# First, let's extract the corresponding value of a specified key.
# This can be done similarly to accessing elements inside a list, only that we don't specify an index, we specify the associated key for the value we want to extract.

# extract '12.4'
print(dict1["IOS"])

# extract 'Cisco'
print(dict1["Vendor"])

# lets try to add a new key-value pair. This is done by simply assigning a new value to the new key
# "RAM" : "128"  

dict1["RAM"] = "128"
print(dict1)

# we can modify the value of a dictionary
# 12.4 - 15.8
dict1.update({"IOS":"15.8"})
print(dict1)

dict1["IOS"] = "15.8"
print(dict1)

# We can also delete a pair from a dictionary, using the del command
del dict1["Ports"]

print(dict1)

# we can use the len() function to find out the number of elements in a dictionary
print(len(dict1))

# we can verify t=if a certain string is a key in a dictionary or not
print("IOS" in dict1)
print("Ports" in dict1)

# There are three important methods to deal with keys and values in dictionary
# 1. keys() -> This method is used to obtain a list having the keys in a dictionary as elements.
print(list(dict1.keys()))

# 2. values() -> This method is used to obtain a list having the values in a dictionary as elements.
print(list(dict1.values()))

# 3. items() -> This method returns a list of tuples, each tuple containing the key and value of each dictionary pair.
print(list(dict1.items()))






# a. Create a dictionary of keys a, b and c where each key has as value a list from 1-10, 11-20, and 21-30 respectively. Then print out the dictionary in a nice format.
a = list(range(1, 11))
b = list(range(11, 21))
c = list(range(21, 31))

print({'a': a, 'b': b, 'c': c})

dict2 = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(dict2)

dict3 = {'a': list(range(1, 11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}
print(dict3)
print(dict3["b"][2])

# b. Access the third value of key b from the dictionary
# Expected Output: 13
v = dict2['b'][2]
print(v)

l = dict2["b"]
val_13 = l[2]
print(val_13)



# Next -> Conversions between Data Types