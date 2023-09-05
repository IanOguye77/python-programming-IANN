# For Loop


vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# lets see how we can work with a for loop

for each_vendor in vendors:
    print(each_vendor)
    
    
my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

# r = range(10)
# for numbers in r:
#     print(numbers * 2)
    
for x in range(10):
    print(x * 2)

# Lets see a more common use of the range() fubction inside a for statement
# what if we want ti interate over a list using list indexes?
# What do we mean by that?
# We still have the vendors list in memory...
print(vendors)   
# Remember the len() function from earlier? lets apply it to our list
print(len(vendors))

# We know that range(5) returns the intergers starting with 0 up to, but not including 5. Moreover, we can convert this range to a list, using the list() function. lets do this

print(list(range(5)))

# We can look at the elements of this list as being the indexes of each element of ur list, vendors. So the element "Cisco" would be positioned at index 0, "HP" at index 1 and so on.

# This means that if we want to get a list of indexesto iterate over, using a for loop, we can use range(len(vendors)) to obtain that list.
print(list(range(len(vendors))))

for element_index in list(range(len(vendors))):
        print(vendors[element_index])
        
# What we did there is we passed the result of one function, len(), to another function, range()
# The result is a range consisting of all the indexexs in the vendor list. We then assigned each index in the range to the element_index temporary variable and executed a piece pf code for each index
# In translation, we told python to check the length of the vendors list, then create a range using that length as an argument for the range() function
# Finally, Python prints out each elementary its index - vendors[0], vendors[1] and so until the list is exhausted

# Another very useful way to iterate over a sequence is by using both the index and the element value as iterating variables. This can be achieved using the enumarate() function in python.
# for index, element in enumerate(vendors, start = 1):
for index, element in enumerate(vendors):
    # print(index, element)
    print(f"{index + 1}. {element}")