# Ranges
# codeskulptor.org -> python 2

r = range(10)

print(r, type(r))

# apply the list() function to the range()
print(list(r))

# You can also do indexing to ranges
print(r[0])
print(r[5])
print(r[-1])

# You can also verify if a certain element/value is a member of the range by using the 'in' and 'not in'
print(10 in r)
print(1 not in r)

# You can apply, for instance, the index() method to find out the index of a certain element of the range
print(r.index(4))

# Finally, keep in mind that you cannot slice a range, but what you can do is you can convert the range to a list, using the list() function and then apply your slice
print(list(r)[2:5])

# Next -> Dictionaries